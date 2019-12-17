from django import forms
from . models import needy

class neddyForm(forms.ModelForm) :
    class Meta:
        model = needy
        fields = ['name' , 'city' , 'hospital' , 'blood_Type' , 'age' , 'donation_type' , 'phone' , 'desciption']