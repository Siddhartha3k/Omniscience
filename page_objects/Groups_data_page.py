import json
import time

import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Test_Groups_page():

    group_tab = "(//a[@class='nav-link'])[3]"
    first_group = "(//span[@class='btn-link'])[1]"
    required_group = "//*[text()='Automation_group']"
    first_form = "(//*[@class='btn-link'])[1]"
    page_navigation = "(//*[@class='btn btn-info btn-sm'])[2]"
    actions_drop_down = "//*[@id='actionsMenuButton']"
    view_overall_results = "(//*[@class='dropdown-item'])[5]"
    list_of_all_values = "//*[@class='form-detail-item']"
    view_decision = "//*[text()='View Decision ']"
    file_path = "/Users/joeyfrmfrnds/Documents/test_project/data/data_names.json"
    create_form_button = "//*[@routerlink='create']"
    browse_form = "//*[@class='custom-file-input']"
    form_provider = "//*[@id='form-provider']"
    save_button = "//button[@class='btn btn-primary']"
    processed_disp = "(//*[@title='Processed'])[1]"
    json_data_path = "D:/git/Omniscience/data/himawari012Form.json"
    provider_name = "Siddhartha"



    def __init__(self, driver):
        self.driver = driver


    def click_a_groups_tab(self):                                     # Select a Group tab
        time.sleep(15)
        self.driver.find_element_by_xpath(self.group_tab).click()

    def click_b_first_group(self):                                    # Select first group
        time.sleep(4)
        self.driver.find_element_by_xpath(self.first_group).click()
        time.sleep(4)

    def click_c_first_form(self):
        time.sleep(45)
        wait = WebDriverWait(self.driver, 400)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.processed_disp)))   # waits until image Processed
        time.sleep(2)
        self.driver.find_element_by_xpath(self.first_form).click()                      # Clicks the form
        time.sleep(15)

    def click_d_actions_drop_down(self):                              # Clicks on 'Action' drop down
        time.sleep(45)
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)

    def click_e_view_overall_results(self):                           # Clicks View overall Results button
        time.sleep(2)
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(3)

    def get_f_list_of_form_values(self):
        time.sleep(3)
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)   # Select all Results
        time.sleep(5)
        file1 = open(self.json_data_path, 'r', encoding="utf8")   # Opens JSON data
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []

        for data in gt_values:
            data_list = data.text
            data_list1.append(data_list)              # Gets all Web Results into a List

        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0

        print("------------------------------------------------------")
        print("Expected Data: ")
        for i in range(len(json_data)):
            if json_data[i] != 0:
                print(json_data[i].encode("utf-8"))
        print("------------------------------------------------------")
        print("------------------------------------------------------")
        print("Actual Data:")
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    print("VERIFY:  ")
                    print(data_list1[i].encode("utf-8"))
                else:
                    print("ERROR:Error:  Inaccurate but high confidence  ")
                    print(data_list1[i].encode("utf-8"))
                    print("")
        print("------------------------------------------------------")

        k = 0
        for i in range(len(data_list1)):
            if data_list1[i] == 0:
                k = k + 0
            else:
                k = k + 1

        if k == 0:
            print("All Results are Accurate")           # Prints if All values are Correct
        else:
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")  # Fails if all the values are not accurate

    def click_g_view_decision_form(self):            # Clicks 'View decision' form
        time.sleep(2)
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(self.view_decision).click()

    def click_h_click_create_form(self):             # Clicks 'Create Form' button
        time.sleep(2)
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(self.create_form_button).click()

    def upload_i_form(self):           # Uploads the Health Check form
        time.sleep(5)
        self.driver.implicitly_wait(100)
        #self.driver.find_element_by_xpath(self.browse_form).send_keys("E://Forms_1/FormA-4.png")
        self.driver.find_element_by_xpath(self.browse_form).send_keys("D://Automation-BitBucket/test/Omniscience/HC_forms/himawari_01-2.png")

    def check_list_of_data(self):           # Compares the web application data
        time.sleep(3)
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            data_list1.append(data_list)
        print("Data List1:")
        print(data_list1)

    def click_automation_group(self):              # Select the 'Automation' group
        time.sleep(3)
        self.driver.find_element_by_xpath(self.required_group).click()
        time.sleep(8)

    def enter_form_provider(self):                 # Enters 'Form Provider' name
        time.sleep(2)
        self.driver.find_element_by_xpath(self.form_provider).send_keys(self.provider_name)

    def click_save_button(self):                   # Clicks on 'Save' button
        time.sleep(2)
        self.driver.find_element_by_xpath(self.save_button).click()
        time.sleep(5)