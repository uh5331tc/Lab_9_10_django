#functional tests are much more realistic but slower. tests to see if its functional, but not if its coreectly functioning
#unit/integration tests more server code, not UI

from selenium.webdriver.chrome.webdriver import WebDriver 
from django.test import LifeServerTestCse

class TitleTest(LifeServerTestCse): 
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()  #conecting
        cls.selenium.implicitly_wait(10) #browser response wait time to wait for the page (its slow)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super.tearDownClass()  #close server funning when test is donw

        #write test
    def test_tittle_on_home_page(self):
        self.selenium.quit()
        super().tearDownClass() #call the constructor function 

    def test_title_on_homepage(self):
        self.selenium.get(self.live_server_url)  #connecting to the browsesr
        self.assertIn('Travel Wishlist', self.selenium.title)  #testing travel wishlist


class AddPlacesTest(LifeServerTestCse):  
    fixtures = ['test_places']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()  #conecting
        cls.selenium.implicitly_wait(10) #browser response wait time to wait for the page (its slow)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super.tearDownClass()  #close server funning when test is donw

        #write test
    def test_add_new_place(self):
        self.selenium.get(self.live_server_url)
        input_name = self.selenium.fine_element_by_id('id_name')
        input_name.send_keys('Denver')    
        
        add_button = self.selenium.find_element_by_id('add-new-place')  #using the id we assigned in wishlist.html
        add_button.click() #would be the same as running the website and clicking the submit button

        denver = self.selenium.find_element_by_id('place-name-5')  
#in fixtures there is 4 existing places, the test starts with a brand new database 
#with auto incrementing integers, so the next place its added should be primarty key #5. 
#sooooo when writing tests do I have to know that the next place was 5? can it be automated to find it on its own?

        self.assertEqual('Denver', denver.text) #get text from the element
        #two tests should pass at this point

        #check if any text is on the page in general for these places
        self.assertIn('Denver', self.selenium.page_source)
        self.assertIn('New York', self.selenium.page_source)
        self.assertIn('Tokyo', self.selenium.page_source)
        

