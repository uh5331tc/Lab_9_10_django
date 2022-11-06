from django.test import TestCase
from django.urls import reverse

from .models import Place
#keep tests seperate and use iniduvidual test cases for each test
#django loads a new DB everytime the test runs
class TestHomePage(TestCase):

    def test_home_page_shows_emp_list_forO_empt_database(self):  #what is self mean here?
        home_page_url = reverse('place_list')  #makes the request by reversing the url
        response = self.client.get(home_page_url) #saves the response
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')  #must use response, 
        self.assertContains(response, 'You have no placrs in your WishList') # make assertions on the response

class TestWishList(TestCase):  #class to test Fixtures
    fixtures = ('test_places')  

    def test_wishlist_contains_not_visited_places(self):
        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')  #must use response, 
        self.assertContains(response, 'Tokyo') 
        self.assertContains(response, 'New York') # checks for NewYork
        self.assertNotContains(response, 'Iraq') 
        self.assertNotContains(response, 'Egypt') # check egypt is not there


class TestWishList(TestCase):  #class to test check to see if the visited page shows the empty message

    def test_visited_page_shows_empty_list_mesage_for_emppty_datavase(self):
        response = self.client.get(reverse('places_visited')) #get from urls.py path-> 'name'
        self.assertTemplateUsed(response, 'travel_wishlist/visited.html')   
        self.assertContains(response, 'You have not visited any places yet') #use visited_message from visited.html, 

class Visited_list(TestCase):
    fixtures = ['test_places']
    
    def test_visited_list_shows_visited_places(self):
        response = self.client.get(reverse('places_visited')) #get from urls.py path-> 'name'
        self.assertTemplateUsed(response, 'travel_wishlist/visited.html')   
        self.assertNotContains(response, 'Egypt') # does NOT 
        self.assertNotContains(response, 'Iraq') # does NOT
        self.assertContains(response, 'Tokyo') # case sensitive


#test for adding a new place
class TestAddNewPlace(TestCase):
    def test_add_new_unvisited_place(self):
        add_place_url  =  reverse('place_list')  #in urls.py 
        new_place_data = {'name': 'Tokyo', 'visited': False}      #disctonary data

        response = self.client.post(add_place_url, new_place_data, follow=True)

        self.assertTemplateUsed(response, 'travel_wishlist.html/wishlist.html')
#context is a dictornary
        response_places = response.context('places')  
        self.assertEqual(1, len(response_places))  #length of response places checks only one place
        tokyo_from_response = response_places[0]
        tokyo_from_database = Place.objects.get(name="Tokyo", visited= False)  #how is there not an easier way to do that

        self.assertEqual(tokyo_from_database, tokyo_from_response)

class TestVisitPlace(TestCase):
    fixtures = ['test_places']

    def test_visit_place(self):
        visit_place_url = reverse('place_was_visited', args=(2) )  #checks the test_places.json file for the "pk": 2 value
        response = self.client.post(visit_place_url, folllow=True)  #not setting any data here
#USE THE template for where you want to go 
        self.assertTemplateUsed(response, 'travel_wishlist.html/wishlist.html')
        self.assertNotContains(response, 'New York') # checks for not NewYork
        self.assertContains(response, 'Tokyo') # checks for tokyo is still in the list

        new_york = Place.objects.get(pk=2)
        self.assertTrue(new_york.visited)

    def test_non_existent_place(self):  #try to post something that does exist
        visit_nonexistent_place_url = reverse('place_was_visited', args=(123456, ))  #not real place
        response = self.client.post(visit_nonexistent_place_url, follow=True)  #looking for response
        self.assertEqual(404, response.status_code) #send a real error message 