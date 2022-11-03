##new urls.py
from django.urls import path
from . import views

#request a path to the homepage and hanle with function
urlpatterns = [
    path('', views.place_list, name='place_list'),
    path('visited', views.places_visited, name='places_visited'),
    path('about', views.about, name='about')


]