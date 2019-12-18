from django import forms
from . models import donator

class donatorForm(forms.ModelForm) :
    class Meta:
        model = donator
        fields = ['firstName', 'lastName', 'email', 'phone', 'password' , 'bloodType'  , 'age' , 'weight' , 'city' , 'gender']