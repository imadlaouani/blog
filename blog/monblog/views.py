
# Create your views here.
from django.http import Http404
from monblog.models import *
from django.shortcuts import render, get_object_or_404
from monblog.forms import *


def home(request):
	posts = Post.objects.all()
	
    return render(request,'home.html',{'posts': posts})


def create_post(request):
	posts = Post.objects.all()
	if request.method == 'POST':
    	form = PostForm(request.POST or None)
    	
    	if form.is_valid():
        	titre = form.cleaned_data['titre']
        	description = form.cleaned_data['description']
        	post = Post(titre=titre,description=description)
        	post.save()
    else:
        form = PostForm()
    
    return render(request, 'home.html', locals())




def lire(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'monblog/lire.html', {'post':post})



