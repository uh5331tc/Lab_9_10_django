from selenium.webdriver.chrome import WebDriver
from django.test import LifeServerTestCse

class TittleTest(LifeServerTestCse): 
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10) #browser response wait time to wait for the page (its slow)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super.tearDownClass()  #close server funning when test is donw

        #write test
    def test_tittle_on_home_page(self):
        self.selenium.get(self.live_server_url)
        


