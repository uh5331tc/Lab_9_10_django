from django.shortcuts import redirect, render
from .models import Place
from .forms import NewPlaceForm
# Create your views here.

def place_list(request):

    #create new place
    form = NewPlaceForm(request.POST)  #creating a form from the data thats in the request
    place = form.save()  #creating a model object from form
    if form.is_valid():  # validation agaisnst DB constraints
        place.save()   # saves place to the DB 
        return redirect('place_list')  #reloads homepage


    places = Place.objects.filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm()
    return render (request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})

def about(request):
    author = 'Noelle'
    about = 'A website to create a list of places to visit'
    return render(request, 'travel_wishlist/about.html', {'author': author, 'about': about})















