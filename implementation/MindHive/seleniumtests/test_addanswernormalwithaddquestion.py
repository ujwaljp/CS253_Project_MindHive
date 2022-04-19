
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAddanswernormalwithaddquestion():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_addanswernormalwithaddquestion(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.maximize_window()
    self.driver.find_element(By.ID, "signin").click()
    self.driver.find_element(By.ID, "id_username").send_keys("tharsh20@iitk.ac.in")
    self.driver.find_element(By.ID, "id_password").send_keys("wsxc1234")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.ID, "askButton").click()
    self.driver.find_element(By.ID, "id_title").click()
    self.driver.find_element(By.ID, "id_title").send_keys("test question")
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.CSS_SELECTOR, "p").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".cke_editable")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>testt question for testing answer<br></p>'}", element)
    self.driver.switch_to.default_content()
    self.driver.find_element(By.ID, "id_tags_1").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(10)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(3) #dropdownMenuButton").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
    self.driver.find_element(By.ID, "signin").click()
    self.driver.find_element(By.ID, "id_username").send_keys("subu@iitk.ac.in")
    self.driver.find_element(By.ID, "id_password").click()
    self.driver.find_element(By.ID, "id_password").send_keys("wsxc1234")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(1) h5").click()
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".cke_editable")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = 'Is the answer working fine'}", element)
    self.driver.switch_to.default_content()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(9)").click()
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".cke_editable")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = 'You dont know me'}", element)
    self.driver.switch_to.default_content()
    self.driver.find_element(By.ID, "id_anonymous").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(9)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(3) #dropdownMenuButton").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
    self.driver.find_element(By.ID, "signin").click()
    self.driver.find_element(By.ID, "id_password").send_keys("wsxc1234")
    self.driver.find_element(By.ID, "id_username").send_keys("tharsh20@iitk.ac.in")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(1) h5").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(3) #dropdownMenuButton").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
  
testClass = TestAddanswernormalwithaddquestion()

testClass.setup_method("")
testClass.test_addanswernormalwithaddquestion()
testClass.teardown_method("")
