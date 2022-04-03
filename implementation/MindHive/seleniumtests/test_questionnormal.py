
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestQuestionnormal():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_questionnormal(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.maximize_window()
    self.driver.find_element(By.ID, "signin").click()
    self.driver.find_element(By.ID, "id_username").send_keys("tharsh20@iitk.ac.in")
    self.driver.find_element(By.ID, "post_form").click()
    self.driver.find_element(By.ID, "id_password").click()
    self.driver.find_element(By.ID, "id_password").send_keys("wsxc1234")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.ID, "askButton").click()
    self.driver.find_element(By.ID, "id_title").click()
    self.driver.find_element(By.ID, "id_title").send_keys("test question")
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.CSS_SELECTOR, "p").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".cke_editable")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = 'this is for test dont touch it'}", element)
    self.driver.switch_to.default_content()
    self.driver.find_element(By.ID, "right").click()
    self.driver.find_element(By.ID, "id_tags_1").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(10)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(3) #dropdownMenuButton").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
testClass = TestQuestionnormal()

testClass.setup_method("")
testClass.test_questionnormal()
testClass.teardown_method("")
