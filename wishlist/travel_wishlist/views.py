from django.shortcuts import redirect, render, get_object_or_404
from .models import Place
from .forms import NewPlaceForm
from django.contrib.auth.decorators import login_required  #requires password 
from django.http import HttpResponseForbidden  #checks to see if the user is allowed to make that request
# Create your views here.


#users can only see their places so they need to log in, using a log in decorator
@login_required
def place_list(request):

    #create new place
    form = NewPlaceForm(request.POST)  #creating a form from the data thats in the request
    place = form.save(commit=False)  #creating a model object from form get data but dont' save yet
    place.user = request.user

    if form.is_valid():  # validation agaisnst DB constraints
        place.save()   # saves place to the DB 
        return redirect('place_list')  #reloads homepage

#filters
    places = Place.objects.filter(user=request.user).filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm()
    return render (request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})

@login_required
def places_visited(request): #db is querried for visited and returns a template with data from db
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', { 'visited': visited } )


@login_required  
def place_was_visited(request, place_pk): #place_pk is an argument
    if request.method == 'POST':
        #from django.shortcuts import get_object_or_404
         #place = Place.objects.get(pk=place_pk)  
        place = get_object_or_404(Place, pk=place_pk)
        if place.user == request.user:  #checks to see if the person who wants the info is the one logged in 
            place.visited = True
            place.save()  #must save or it will not save
        else: 
            return HttpResponseForbidden()
    
    return redirect('place_list')  #take me to page when i click the button/submit datalllllllllllllll
    # return redirect('places_visited')


def about(request):
    author = 'Noelle'  #who is the author
    about = 'A website to create a list of places to visit'
    return render(request, 'travel_wishlist/about.html', {'author': author, 'about': about})


@login_required  
def place_details(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)

    #does this place belong to the current user, data privacy
    if place.user != request.user:
        return HttpResponseForbidden()
#is this a GET request (show data +form) or a POST Request(update Place object)?
#if POST validate form data and update
    if request.method == 'POST':
        form = TripReviewForm(request.POST, request.FILES, isinstance=place)
        if form.is_valid():
            form.save()
            messages.info(request, 'Trip Information Updated!')
        else: 
            messages.error(request, form.errors) #temp rewrite later
        return redirect('place_details', place_pk=place_pk)
    
#if GET  show place info and form  
    else:
        if place.visited: 
            review_form = TripReviewForm(instance=place)
        return render(request, 'travel_wishlist/place_detail.html', {'place': place, 'review_form': review_form })
    else: #not sending the form 
        return render(request, 'travel_wishlist/place_detail.html', {'place': place})


@login_required
def delete_place(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)
    if place.user == request.user:
        place.delete()
        return redirect('place_list')  

    else:
        return HttpResponseForbidden()














