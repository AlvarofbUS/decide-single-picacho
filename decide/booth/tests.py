from base.tests import BaseTestCase
from django.contrib.auth.models import User

# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By

class BoothTestCase(BaseTestCase):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def get_or_create_user(self, pk):
        user, _ = User.objects.get_or_create(pk=pk)
        user.username = 'user{}'.format(pk)
        user.set_password('qwerty')
        user.save()
        return user

    def testGetVotings(self):
        userNuevo = self.get_or_create_user(1)
        data = {
            User: userNuevo
        }
        response = self.client.post('/booth/votaciones/', data)
        self.assertEqual(response.status_code, 200)

    def testBooth(self):
        userNuevo = self.get_or_create_user(1)
        data = {
            User: userNuevo
        }
        self.login(user = userNuevo.username)
        response = self.client.get('/booth/', data)
        self.assertEqual(response.status_code, 200)
    
'''
class TestLoginBoothSelenium():

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.vars = {}

    def tearDown(self):
        self.driver.quit()
  
    def test_nuevoTestCompleto(self):
        self.driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
        self.driver.set_window_size(1440, 773)
        self.driver.find_element(By.ID, "id_username").click()
        self.driver.find_element(By.ID, "id_username").send_keys("decide")
        self.driver.find_element(By.ID, "id_password").send_keys("decide123")
        self.driver.find_element(By.CSS_SELECTOR, ".submit-row > input").click()
        self.driver.find_element(By.LINK_TEXT, "Votings").click()
        elements = self.driver.find_elements(By.LINK_TEXT, "Votación de Prueba")
        self.driver.find_element(By.LINK_TEXT, "Home").click()
        self.driver.find_element(By.LINK_TEXT, "Censuss").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".row1:nth-child(1) a")
        assert len(elements) > 0
        self.driver.find_element(By.ID, "result_list").click()
        self.driver.find_element(By.CSS_SELECTOR, ".row1:nth-child(1) > .field-voter_id").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".row1:nth-child(1) > .field-voter_id")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".row1:nth-child(1) > .field-voter_id")
        assert len(elements) > 0
        self.driver.get("http://127.0.0.1:8000/booth/")
        self.driver.set_window_size(1440, 773)
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").send_keys("usuarioSelenium")
        self.driver.find_element(By.ID, "password").send_keys("decide123")
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        self.driver.implicitly_wait(10)
        assert self.driver.find_element(By.LINK_TEXT, "Votacion de Prueba: Votacion - FINALIZADA").text == "Votacion de Prueba: Votacion - FINALIZADA"
    
'''