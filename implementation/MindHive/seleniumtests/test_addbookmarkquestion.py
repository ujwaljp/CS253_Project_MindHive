
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestAddbookmarkquestion():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_addbookmarkquestion(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.maximize_window()
    self.driver.find_element(By.ID, "signin").click()
    self.driver.find_element(By.ID, "id_password").send_keys("wsxc1234")
    self.driver.find_element(By.ID, "id_username").send_keys("tharsh20@iitk.ac.in")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.ID, "askButton").click()
    self.driver.find_element(By.ID, "id_title").click()
    self.driver.find_element(By.ID, "id_title").send_keys("question for bookmark test")
    element = self.driver.find_element(By.ID, "cke_13_text")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".cke_editable")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>Bokkmark test<br></p>'}", element)
    self.driver.switch_to.default_content()
    self.driver.find_element(By.ID, "id_tags_0").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(10)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".bookmark > .fa-regular").click()
    self.driver.find_element(By.ID, "bookmarksButton").click()
  
testClass = TestAddbookmarkquestion()

testClass.setup_method("")
testClass.test_addbookmarkquestion()
testClass.teardown_method("")