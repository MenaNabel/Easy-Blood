from django.shortcuts import render
from needy.models import needy
# Create your views here.

def index(requst):
    context = {
        'index' : index ,
    }
    return render(requst , 'index.html' , context)

def all_needy(request):
    all_needy = needy.objects.all()
    context = {
    'all_needy' : all_needy ,
    }
    return render(request,'all_posts.html' , context)

