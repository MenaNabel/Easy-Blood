from django.shortcuts import render, get_list_or_404 , redirect
from . models import needy
from . forms import neddyForm
from .forms import forms
# Create your views here.


def addNeedy(request):
    if request.method == 'POST':
        form = neddyForm(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = neddyForm()

    context = {
        'form' : form ,
    }
    return  render(request, 'addNeedy.html' , context)



def allNeedies(request):
    allNeedies = needy.objects.all()
    context = {
        'allNeedies': allNeedies,
    }
    # Your View Body and Actions
    return redirect('index.html', context)