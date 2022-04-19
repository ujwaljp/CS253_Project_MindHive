
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestLikedisliketest():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_likedisliketest(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.set_window_size(1848, 1053)
    self.driver.find_element(By.ID, "signin").click()
    self.driver.find_element(By.ID, "id_password").send_keys("wsxc1234")
    self.driver.find_element(By.ID, "id_username").send_keys("tharsh20@iitk.ac.in")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.ID, "askButton").click()
    self.driver.find_element(By.ID, "id_title").click()
    self.driver.find_element(By.ID, "id_title").send_keys("Model question")
    element = self.driver.find_element(By.ID, "cke_13_text")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.CSS_SELECTOR, "p").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".cke_editable")
    self.driver.execute_script("if(arguments[0].contentEditable === 'true') {arguments[0].innerText = '<p>question to check likes and dislikes<br></p>'}", element)
    self.driver.switch_to.default_content()
    self.driver.find_element(By.ID, "id_tags_1").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(10)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fa-thumbs-up").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fa-thumbs-down").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(3) #dropdownMenuButton").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
    self.driver.find_element(By.ID, "signin").click()
    self.driver.find_element(By.ID, "id_password").send_keys("wsxc1234")
    self.driver.find_element(By.ID, "id_username").send_keys("subu@iitk.ac.in")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(1) h5").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fa-thumbs-up").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(3) #dropdownMenuButton").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
    self.driver.find_element(By.ID, "signin").click()
    self.driver.find_element(By.ID, "id_password").send_keys("wsxc1234")
    self.driver.find_element(By.ID, "id_username").send_keys("tharsh20@iitk.ac.in")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(1) h5").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(3) #dropdownMenuButton").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
  
testClass = TestLikedisliketest()

testClass.setup_method("")
testClass.test_likedisliketest()
testClass.teardown_method("")