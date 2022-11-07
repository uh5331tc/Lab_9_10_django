from django.shortcuts import redirect, render, get_object_or_404
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

def places_visited(request): #db is querried for visited and returns a template with data from db
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', { 'visited': visited } )

def place_was_visited(request, place_pk): #place_pk is an argument
    if request.method == 'POST':
        #from django.shortcuts import get_object_or_404
         #place = Place.objects.get(pk=place_pk)  
        place = get_object_or_404(Place, pk=place_pk)
        place.visited = True
        place.save()  #must save or it will not save

    return redirect('place_list')  #take me to page when i click the button/submit datalllllllllllllll
    # return redirect('places_visited')


def about(request):
    author = 'Noelle'
    about = 'A website to create a list of places to visit'
    return render(request, 'travel_wishlist/about.html', {'author': author, 'about': about})















