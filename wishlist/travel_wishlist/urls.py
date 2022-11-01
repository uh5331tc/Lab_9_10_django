##new urls.py

from django import path
from . import views

#request a path to the homepage and hanle with function
urlpatterns = [
    path('', views.place_list, name='place_list'),

]