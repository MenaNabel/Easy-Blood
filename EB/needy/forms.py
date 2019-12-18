from django import forms
from . models import needy
from ckeditor.widgets import CKEditorWidget


class neddyForm(forms.ModelForm) :
    class Meta:
        model = needy
        desciption = forms.CharField(widget=CKEditorWidget())
        fields = ['name' , 'city' , 'hospital' , 'blood_Type' , 'age' , 'donation_type' , 'phone' , 'desciption']