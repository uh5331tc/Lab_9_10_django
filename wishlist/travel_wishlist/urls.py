##new urls.py
from django.urls import path, include
from . import views

#request a path to the homepage and hanle with function
urlpatterns = [
    path('', views.place_list, name='place_list'),
    path('', include('travel_wishlist.urls'))

]