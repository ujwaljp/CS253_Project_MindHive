
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestWrongusernamepasswordforgotpassword():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_wrongusernamepasswordforgotpassword(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.set_window_size(1434, 978)
    self.driver.find_element(By.ID, "signin").click()
    self.driver.find_element(By.ID, "id_username").send_keys("rat@iitk.ac.in")
    self.driver.find_element(By.ID, "id_password").click()
    self.driver.find_element(By.ID, "id_password").send_keys("wsxc1234")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.LINK_TEXT, "Forgot Password?").click()
    self.driver.find_element(By.ID, "id_email").click()
    self.driver.find_element(By.ID, "id_email").send_keys("tharsh20@iitk.ac.in")
    self.driver.find_element(By.NAME, "reset_password_button").click()
    self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(3)").click()
  
testClass = TestWrongusernamepasswordforgotpassword()

testClass.setup_method("")
testClass.test_wrongusernamepasswordforgotpassword()
testClass.teardown_method("")