
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestAddingcomment():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_addingcomment(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.maximize_window()
    self.driver.find_element(By.ID, "signin").click()
    self.driver.find_element(By.ID, "id_password").send_keys("wsxc1234")
    self.driver.find_element(By.ID, "id_username").send_keys("tharsh20@iitk.ac.in")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.ID, "askButton").click()
    self.driver.find_element(By.ID, "id_title").click()
    self.driver.find_element(By.ID, "id_title").send_keys("comment check")
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".cke_editable")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>question for comment check<br></p>'}", element)
    self.driver.switch_to.default_content()
    self.driver.find_element(By.ID, "id_tags_1").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(10)").click()
    self.driver.find_element(By.NAME, "comment_text").click()
    self.driver.find_element(By.NAME, "comment_text").send_keys("first")
    self.driver.find_element(By.NAME, "comment_text").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(3) #dropdownMenuButton").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
    self.driver.find_element(By.ID, "signin").click()
    self.driver.find_element(By.ID, "id_username").send_keys("subu@iitk.ac.in")
    self.driver.find_element(By.ID, "id_password").click()
    self.driver.find_element(By.ID, "id_password").send_keys("wsxc1234")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(1) h5").click()
    self.driver.find_element(By.NAME, "comment_text").click()
    self.driver.find_element(By.NAME, "comment_text").send_keys("second")
    self.driver.find_element(By.NAME, "comment_text").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(3) #dropdownMenuButton").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
  
testClass = TestAddingcomment()

testClass.setup_method("")
testClass.test_addingcomment()
testClass.teardown_method("")
