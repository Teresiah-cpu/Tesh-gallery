from importlib.resources import path
from django.urls import path, re_path as url
from . import views

urlpatterns= [
    url(r'^$',views.gallery,name='gallery'),
    path('photo/<str:pk>/',views.viewphoto, name='photo'),
    url('add/', views.addphoto, name='add'),
    url('search/', views.search_results, name='search_results'),
    url(r'^location/(\d+)', views.get_location, name='get_location')
]
