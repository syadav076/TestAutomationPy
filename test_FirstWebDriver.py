import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class LoginVerify(unittest.TestCase):

    abc = webdriver.Chrome()


    def test_loadurl(self):
        #self.driver = webdriver.Chrome()
        self.abc.maximize_window()
        self.abc.get("https://celebration.qa1.carestackqa.com")
        self.abc.implicitly_wait(10)
        self.abc.search_login = "//INPUT[@type='submit'][@value='Log In']"
        loginbutton = self.abc.find_element_by_xpath(self.abc.search_login).get_attribute('value')

        try:
            self.assertIn("Log In",loginbutton)
        except:
            print("LoadURL failed")
        else:
            print("LoadURL Passed")

    def test_login(self):
        self.abc.search_username = "//input[@type='text'][@name='username']"
        self.abc.search_password = "//input[@type='password'][@name='password']"
        self.abc.search_login = "//INPUT[@type='submit'][@value='Log In']"
        self.abc.find_element_by_xpath(self.abc.search_username).send_keys('syadav')
        self.abc.find_element_by_xpath(self.abc.search_password).send_keys('Abc@123')
        self.abc.find_element_by_xpath(self.abc.search_login).click()

    def test_logout(self):
        actions = ActionChains(self.abc)
        self.abc.search_userIcon = "//I[@class='fa fa-fw fa-user']"
        hover_mouse = self.abc.find_element_by_xpath(self.abc.search_userIcon)
        actions.move_to_element(hover_mouse).perform()
        try:
            search_logout = self.abc.find_element_by_xpath("//SPAN[@class='dropm-text'][text()='Logout']")
            search_logout.click()
        except:
            print("Failed to find Logout Option")
        else:
            print("Logout Passed")
        self.abc.implicitly_wait(10)
        self.abc.close()


    # def test_LoadURL_Verify(self):
    #     self.driver.get("https://www.google.co.in")
    #     #self.driver.implicitly_wait(5)
    #     self.driver.maximize_window()
    #
    # def test_login(self):
    #      self.Search_Button = "//INPUT[@type='submit'][@value='Google Search']"
    #      self.Search_textbox = "//input[@type='text'][@id='lst-ib']"
    # #     # self.Search_Password = "//input[@type='password'][@name='password']"
    #      self.driver.find_element_by_xpath(self.Search_textbox).send_keys('chinchu')
    # #     self.driver.find_element_by_xpath("//input[@type='password'][@name='password']").send_keys('Abc@123')
    #      self.driver.find_element_by_xpath(self.Search_Button).click()
# self.Search_password_label = "//LABEL"
        # checkpoint_login_page = self.Search_password_label.__getattribute__("text")
        #

    #def tearDown(self):
       # self.driver.close()