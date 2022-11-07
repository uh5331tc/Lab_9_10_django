##new urls.py
# this is routing 
from django.urls import path
from . import views

#request a path to the homepage and hanle with function
#each url path is matched with a view function that can be called to that request
urlpatterns = [  #capture parameters 
    path('', views.place_list, name='place_list'),
    path('visited', views.places_visited, name='places_visited'),
    path('place/<int:place_pk>/was_visited', views.place_was_visited, name='place_was_visited'), #this will make a place holder
    path('place/<int:place_pk>', views.place_details, name='place_details'), #this will make a place holder
    path('place/<int:place_pk>/delete', views.delete_place, name='delete_place'), #this will make a place holder

]