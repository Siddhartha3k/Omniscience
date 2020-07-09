from page_objects.Groups_data_page import Test_Groups_page
from page_objects.Login_page import Test_Login_page

import unittest
import HtmlTestRunner
from selenium import webdriver
import os
import sys
import json
from page_objects.multiple_forms_upload import Test_multiple_form_upload
sys.path.append("D:/test")




class Form_upload(unittest.TestCase):

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    DRIVER_BIN = os.path.join(PROJECT_ROOT, "../drivers/chromedriver")
    driver = webdriver.Chrome(executable_path=DRIVER_BIN)
    baseURL = "https://megaocr-ui-rgacf-daiichi.omni.sc"
    file1 = open("../data/Login_credentials.json", 'r')
    json_input = file1.read()
    inputBody = json.loads(json_input)
    json_data = list(inputBody.values())
    username = json_data.__getitem__(0)
    password = json_data.__getitem__(1)

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)        # Opens the Web Application
        cls.driver.maximize_window()       # Maximize the window
        cls.driver.implicitly_wait(100)

    def test_b_login(self):
        lp = Test_Login_page(self.driver)
        lp.enter_user_name(self.username)  # Enters the username
        self.driver.implicitly_wait(10)
        lp.enter_password(self.password)   # Enters the password
        lp = Test_Login_page(self.driver)
        self.driver.implicitly_wait(10)
        lp.click_submit_button()           # Clicks submit button

    def test_c_upload_multiple_forms(self):
        multiple_form=Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()                        # Clicks on Groups tab
        multiple_form.upload_and_validate_b_multiple_forms()      # Validates the Actual with Expected Key values


