import unittest
import HtmlTestRunner
from selenium import webdriver
import os
import sys
import time

# sys.path.append("/Users/joeyfrmfrnds/PycharmProjects/Omni_Test_Automation")
sys.path.append("D:/Automation/Omni_Test_Automation")
from page_objects.Login_page import Test_Login_page


class Login_test(unittest.TestCase):
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
        cls.driver.implicitly_wait(10)
        time.sleep(5)

    def test_login(self):
        lp = Test_Login_page(self.driver)
        lp.enter_user_name(self.username)
        self.driver.implicitly_wait(10)
        lp.enter_password(self.password)
        self.driver.implicitly_wait(10)
        lp.click_submit_button()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='D:/Automation/Omni_Test_Automation/reports'))
