from django.shortcuts import render, get_list_or_404 , redirect
from . models import donator
from . forms import donatorForm
from .forms import forms
# Create your views here.


def donatorForm(request):
    if request.method == 'POST':
        form = donatorForm(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = donatorForm()

    context = {
        'form' : form ,
    }


    return  render(request, 'addDonator.html' , context)

