from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import os
import time
import json



class Test_abc():

    @pytest.fixture()
    def setup(self):
        global driver
        PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
        DRIVER_BIN = os.path.join(PROJECT_ROOT, "/Users/joeyfrmfrnds/Downloads/chromedriver")
        self.driver = webdriver.Chrome(executable_path=DRIVER_BIN)



    def test_a_get_home_page(self, setup):
        self.driver.get("https://gtlite.omni.sc")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        time.sleep(5)

    def test__b_login_Gtlite(self, setup):
        time.sleep(5)
        self.driver.find_element_by_xpath("//input[@id='okta-signin-username']").send_keys("siddhartha.p@3ktechnologies.com",
                                                                                      Keys.TAB)
        time.sleep(3)
        self.driver.find_element_by_xpath("//input[@id='okta-signin-password']").send_keys("Sidhu@420")
        time.sleep(4)
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        time.sleep(10)
        self.driver.find_element_by_xpath("(//a[@class='nav-link'])[3]").click()
        self.driver.find_element_by_xpath("(//*[@class='btn-link'])[1]").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("(//*[@class='btn-link'])[1]").click()
        time.sleep(13)
        self.driver.find_element_by_xpath("(//*[@class='btn btn-info btn-sm'])[2]").click()
        time.sleep(10)
        self.driver.find_element_by_xpath("//*[@id='actionsMenuButton']").click()
        time.sleep(2)

    def test_dropdown(self):
        self.driver.find_element_by_xpath("(//*[@class='dropdown-item'])[5]").click()
        time.sleep(3)
        GT_values = self.driver.find_elements_by_xpath("//*[@class='form-detail-item']")
        time.sleep(5)
        file1 = open("/Users/joeyfrmfrnds/Documents/test_project/data/data_names.json", 'r')
        json_input = file1.read()
        inputBody = json.loads(json_input)
        json_data = list(inputBody.values())
        print("Json_data:")
        # print(json_data)
        data_list1 = []
        for data in GT_values:
            data_list = data.text
            data_list1.append(data_list)
        data_list1.pop(0)
        print("Data List1:")
        print(data_list)
        found_data = []
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0

        for i in range(len(json_data)):
            if json_data[i] != 0:
                print("Expected Data: " + json_data[i])

        print("------------------------------------------------------")
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                print("Actual Data: " + data_list1[i])

        time.sleep(5)
        self.driver.find_element_by_xpath("//*[text()='View Decision ']").click()
