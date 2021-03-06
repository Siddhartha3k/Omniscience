from selenium.webdriver.common.keys import Keys
import unittest


class Test_Login_page(unittest.TestCase):
    username = "//input[@id='okta-signin-username']"
    password = "//input[@id='okta-signin-password']"
    submit_button = "//input[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def enter_user_name(self, username):
        self.driver.find_element_by_xpath(self.username).send_keys(username, Keys.TAB)    # Enter User Name

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password).send_keys(password, Keys.TAB)    # Enter Password

    def click_submit_button(self):
        self.driver.find_element_by_xpath(self.submit_button).click()                     # Click Submit button



