from email.mime import image
from pyexpat import model
# from typing_extensions import Self
from unicodedata import category, name
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=True)


    def _str_ (self):
        return self.name

class Photo(models.Model):
    # name = models.CharField(max_length =30,null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)

    # image = models.ImageField(default='DEFAULT VALUE')
    description = models.TextField()

    def __str__(self):
        return self.description 

    
    # get all images
    def update_image(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category
        self.save()             

# get image by id
    @classmethod
    def get_image_by_id(cls, id):
        image = Photo.objects.get(id=id)
        return image

    @classmethod
    def filter_by_category(cls, category_id):
        images = Photo.objects.filter(category_id=category_id)
        return images
    

    @classmethod
    def search_by_category(cls,search_term):
        searched_photos=cls.objects.filter(category__category__contains=search_term)
        return searched_photos


