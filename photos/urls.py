from django.urls import re_path as url
from . import views

urlpatterns=[
    url(r'^$',views.gallery,name='gallery'),
    url('photo/<str:pk>/',views.viewphoto, name='photo'),
    url('add/', views.addphoto, name='add'),
]
