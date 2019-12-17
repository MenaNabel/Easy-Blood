from django import forms
from . models import AboutUs

class AboutUsForm(forms.ModelForm):
    #class Meta:
        model = AboutUs
        fildes = ['title']
