import unittest

import HtmlTestRunner
from selenium import webdriver
import os
import sys
import time
import json

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

    def test_a_login(self):
        a = "中性脂肪\n今回\n85\n前回\n123"
        a = a.encode('utf-8')
        b = a.decode('utf-8')
        print(a)



if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='D:/Automation/Omni_Test_Automation/reports'))