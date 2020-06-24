from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import json

class Test_Cases_page():
    cases_tab = "//*[text()='Cases']"
    first_case = "(//*[@class='case-item-title'])[1]/child::*"
    json_file_path = "/Users/joeyfrmfrnds/Documents/test_project/data/data_names.json"
    list_of_elements = "//tr"



    def __init__(self, driver):
        self.driver = driver

    def click_a_cases(self):
        time.sleep(10)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.cases_tab).click()

    def first_b_case(self):
        time.sleep(5)
        self.driver.implicitly_wait(10)
        first_case1 = self.driver.find_element_by_xpath(self.first_case)
        actions = ActionChains(self.driver)
        actions.move_to_element(first_case1).click().perform()
        time.sleep(2)

    def get_c_list_of_case_values(self):
        time.sleep(2)
        self.driver.implicitly_wait(10)
        GT_values = self.driver.find_elements_by_xpath(self.list_of_elements)
        time.sleep(5)
        file1 = open(self.json_file_path, 'r')
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



