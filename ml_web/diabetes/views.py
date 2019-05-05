from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import os, re, json
from . import ML
from .forms import DiabetesData
from django.http import Http404
import random
# Create your views here.
def index(request):
    return render(request, "diabetes/index.html", {})

def home(request):
    template = loader.get_template("diabetes/home.html")
    return HttpResponse(template.render({}, request))
    #return render(request, "diabetes/home.html", {})

def algorithm(request):
    template = loader.get_template("diabetes/algorithm.html")
    return HttpResponse(template.render({}, request))    

def image(request, img_name):
    print("requested: "+img_name)
    dir = "{}/diabetes/media/".format(os.getcwd())
    listFile = os.listdir(dir)
    
    for i in listFile:
        if (re.match(r"{}\.(.*)".format(img_name), i)):
            img_name = i
    img_name = os.path.join(dir, img_name)
    print("request image {}: {}".format(img_name, os.access(img_name, os.R_OK)))
    if (os.access(img_name, os.R_OK)):
        with open(img_name, "rb") as read:
            return HttpResponse(read)
    print(img_name)
    return HttpResponse("No IMG")

def checkit(request):
    if (request.method=="POST"):
        pass
    template = loader.get_template("diabetes/checkit.html")
    return HttpResponse(template.render({}, request))

def jquery(request):
    with open(os.path.join(os.getcwd(), "diabetes", "jquery.min.js"), "rb") as baca:
        return HttpResponse(baca)

def finish(request):
    if (request.method=="POST"):
        form = DiabetesData(request.POST)
        print("Predicting...")
        try:
            data = [float(form.data["Pregnancies"]), float(form.data["Glucose"]), float(form.data["BloodPressure"]),float(form.data["SkinThickness"]), float(form.data["Insulin"]), float(form.data["BMI"]), float(form.data["DiabetesPedigreeFunction"]), float(form.data["Age"])]
        except Exception as e:
            print("Wrong input: ", str(e))
            data = [6, 148, 72, 35, 0, 33.6, 0.627, 50] if (bool(random.randint(0, 1)))  else [1, 85, 66, 29, 0, 26.6, 0.351, 31]

        result, accuracy = ML.getResult("/media/kevin/data/programming/AI/Diabetes/ml_web/diabetes/diabetes.csv", data)
        dicti = {"diabetes": str(result), "accuracy": str(accuracy)}
        print("result: ", dicti)
        return HttpResponse(str(json.dumps(dicti)))    
    else:
        raise Http404("Invalid Data")
    