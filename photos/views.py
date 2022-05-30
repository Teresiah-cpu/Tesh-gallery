from multiprocessing import context
from sre_parse import CATEGORIES
from unicodedata import category
from django.shortcuts import redirect, render
from .models import Category, Photo
# Create your views here.

def gallery(request):
    # user = request.user
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.filter
    else:
        photos = Photo.objects.filter(category__name__contains=category)

    categories = Category.objects.filter()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'photos/gallery.html', context)
# def gallery(request):
#     categories = Category.objects.all()
#     photos =Photo.objects.all()
#     context = {'categories': categories, 'photos': photos}
#     return render(request, 'photos/gallery.html', context)

def viewphoto(request):
    photo = Photo.objects.all()
    return render(request, 'photos/photo.html', {'photo': photo})

# def viewphoto(request, pk):
#     photo = Photo.objects.get(id=pk)
#     return render(request, 'photos/photo.html', {'photo': photo})

# def addphoto(request):
#     return render(request, 'photos/add.html')  


def addphoto(request):
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')

    context = {'categories': CATEGORIES}
    return render(request, 'photos/add.html', context)              