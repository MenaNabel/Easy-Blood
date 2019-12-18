from django.shortcuts import render, get_list_or_404 , redirect
from . models import donator
from . forms import donatorForm
from .forms import forms
# Create your views here.


def addDonator(request):
    if request.method == 'POST':
        form = donatorForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            form.save()
    else :
        form = donatorForm()

    context = {
        'form' : form ,
    }


    return  render(request, 'addDonator.html' , context)

