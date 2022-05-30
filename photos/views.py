from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from .models import Category, Photo
# Create your views here.

def gallery(request):
    categories = Category.objects.all()
    photos =Photo.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)

def viewphoto(request):
    photo = Photo.objects.all()
    return render(request, 'photos/photo.html', {'photo': photo})

# def viewphoto(request, pk):
#     photo = Photo.objects.get(id=pk)
#     return render(request, 'photos/photo.html', {'photo': photo})

def addphoto(request):
    return render(request, 'photos/add.html')            