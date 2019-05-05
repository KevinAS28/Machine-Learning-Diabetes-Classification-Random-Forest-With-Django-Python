from django.conf.urls import url, include
from django.urls import path, re_path
from django.contrib import admin
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    re_path(r'^.*/(?P<img_name>.*)\.png$', views.image),
    re_path(r'(?P<img_name>.*)\.png$', views.image),
    re_path(r'algorithm', views.algorithm),
    path("home/", views.home, name="home"),
    path("checkit/", views.checkit),
    path("checkit/finish/", views.finish),
    path("checkit/jquery.min.js", views.jquery),
    

]
