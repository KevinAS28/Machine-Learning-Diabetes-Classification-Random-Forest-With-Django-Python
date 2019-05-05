from django import forms

class DiabetesData(forms.Form):
    Pregnancies = forms.FloatField()
    Glucose = forms.FloatField()
    BloodPressure = forms.FloatField()
    SkinThickness = forms.FloatField()
    Insulin = forms.FloatField()
    BMI = forms.FloatField()
    DiabetesPedigreeFunction =  forms.FloatField()
    Age = forms.FloatField()
    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        Pregnancies = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')

