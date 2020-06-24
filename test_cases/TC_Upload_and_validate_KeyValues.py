import unittest
import HtmlTestRunner
from selenium import webdriver
import os
import sys
import time
sys.path.append("D:/Automation/Omni_Test_Automation")

from page_objects.Groups_data_page import Test_Groups_page
from page_objects.Login_page import Test_Login_page



class Form_upload(unittest.TestCase):

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    DRIVER_BIN = os.path.join(PROJECT_ROOT, "D:/Chrome_driver/chromedriver_win32 (1)/chromedriver")
    driver = webdriver.Chrome(executable_path=DRIVER_BIN)
    baseURL = "https://megaocr-ui-rgacf-daiichi.omni.sc"
    baseURL1 = "https://gtlite.omni.sc"
    username = "siddhartha.p@3ktechnologies.com"
    password = "Sidhu@420"

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(100)

    def test_b_login(self):
        lp = Test_Login_page(self.driver)
        lp.enter_user_name(self.username)
        self.driver.implicitly_wait(10)
        lp.enter_password(self.password)
        lp = Test_Login_page(self.driver)
        self.driver.implicitly_wait(10)
        lp.click_submit_button()

    def test_c_upload_form(self):
        gp = Test_Groups_page(self.driver)
        gp.click_a_groups_tab()
        gp.click_automation_group()
        gp.click_h_click_create_form()
        gp.upload_i_form()
        gp.enter_form_provider()
        gp.click_save_button()

    def test_d_groups(self):
        gp = Test_Groups_page(self.driver)
        gp.click_c_first_form()
        gp.click_d_actions_drop_down()
        gp.click_e_view_overall_results()
        #gp.check_list_of_data()
        gp.get_f_list_of_form_values()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='D:/Automation/Omni_Test_Automation/reports'))