
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestAskques():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_askques(self):
    self.driver.get("http://127.0.0.1:8000/questions/askform/")
    self.driver.set_window_size(1848, 1053)
    self.driver.find_element(By.ID, "id_title").click()
    self.driver.find_element(By.ID, "id_title").send_keys("test")
    element = self.driver.find_element(By.ID, "cke_13_text")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.CSS_SELECTOR, "html").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".cke_editable")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>new <br></p>'}", element)
    self.driver.switch_to.default_content()
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .form-check:nth-child(1)").click()
    self.driver.find_element(By.ID, "id_tags_0").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(10)").click()
testClass = TestAskques()

testClass.setup_method("")
testClass.test_askques()
testClass.teardown_method("")