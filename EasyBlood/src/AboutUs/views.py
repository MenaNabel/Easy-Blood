from django.shortcuts import render , redirect , get_object_or_404
from . models import AboutUs # Create your views here.
from . forms import AboutUsForm

def all_posts(request):
    all_posts = AboutUs.objects.filter(active = True)
    context = {
    'all_posts' : all_posts ,
    }
    return render(request,'all_posts.html' , context)



def post(request , id):
    #post = AboutUs.objects.get(id=id)
    post = get_object_or_404(AboutUs , id=id)
    context = {
    'post' : post ,
    }
    return render (request , 'details.html' , context)


def create_post(request):
    if request.method == 'POST':
        form = AboutUsForm(request.POST)
        if form.is_valid() :
            new_form = form.save(commit=False)
            new_form.user = request.user
            form.save()
            return redirect('/')
    else :
        form = AboutUsForm()

    context = {
        'form' : form,
    }
    return render(request , 'create.html' , context)


def edit_post(request,id):
    post = get_object_or_404(AboutUs, id=id)
    if request.method == 'POST':
        form = AboutUsForm(request.POST , isinstance = post)
        if form.is_valid() :
            new_form = form.save(commit=False)
            new_form.user = request.user
            form.save()
            return redirect('/')
    else :
        form = AboutUsForm(isinstance = post)

    context = {
        'form' : form,
    }
    return render(request , 'edit.html' , context)

