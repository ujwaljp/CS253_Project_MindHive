
from selenium import webdriver
from selenium.webdriver.common.by import By
class TestNewuserfromsigninpage():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_newuserfromsigninpage(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.maximize_window()
    self.driver.find_element(By.ID, "signin").click()
    self.driver.find_element(By.LINK_TEXT, "Sign up").click()
    self.driver.find_element(By.ID, "id_username").click()
    self.driver.find_element(By.ID, "id_username").send_keys("frokie")
    self.driver.find_element(By.ID, "id_name").click()
    self.driver.find_element(By.ID, "id_name").send_keys("yash verma")
    self.driver.find_element(By.ID, "id_email").click()
    self.driver.find_element(By.ID, "id_email").send_keys("yverma@iitk.ac.in")
    self.driver.find_element(By.ID, "id_password1").click()
    self.driver.find_element(By.ID, "id_password1").send_keys("wsxc1234")
    self.driver.find_element(By.ID, "id_password2").click()
    self.driver.find_element(By.ID, "id_password2").send_keys("wsxc1234")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.ID, "id_username").click()
    self.driver.find_element(By.ID, "id_username").send_keys("yverma@iitk.ac.in")
    self.driver.find_element(By.ID, "id_password").click()
    self.driver.find_element(By.ID, "id_password").send_keys("wsxc1234")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
  
testClass = TestNewuserfromsigninpage()

testClass.setup_method("")
testClass.test_newuserfromsigninpage()
testClass.teardown_method("")