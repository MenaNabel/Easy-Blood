from django import forms
from . models import donator

class donatorForm(forms.ModelForm) :
    class Meta:
        model = donator
        fields = ['firstName' , 'lastName' , 'email' , 'phone' , 'password' , 'bloodType' , 'dateOfLastDanation' , 'age' , 'weight' , 'city' , 'gender']