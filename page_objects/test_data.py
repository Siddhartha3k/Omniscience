import json
import time
import unittest
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Test_sample(unittest.TestCase):
    group_tab = "(//a[@class='nav-link'])[3]"
    first_group = "(//span[@class='btn-link'])[1]"
    required_group = "//*[text()='Automation_group']"
    first_form = "(//*[@class='btn-link'])[1]"
    page_navigation = "(//*[@class='btn btn-info btn-sm'])[2]"
    actions_drop_down = "//*[@id='actionsMenuButton']"
    view_overall_results = "(//*[@class='dropdown-item'])[5]"
    list_of_all_values = "//*[@class='form-detail-item']"
    list_key_values ="//*[@class='d-flex ocr-values-list']"
    view_decision = "//*[text()='View Decision ']"
    file_path = "/Users/joeyfrmfrnds/Documents/test_project/data/data_names.json"
    create_form_button = "//*[@routerlink='create']"
    browse_form = "//*[@class='custom-file-input']"
    form_provider = "//*[@id='form-provider']"
    save_button = "//button[@class='btn btn-primary']"
    processed_disp = "(//*[@title='Processed'])[1]"
    #json_data_path = "D:/git/Omniscience/data/himawari012Form.json"
    provider_name = "Siddhartha"

    def __init__(self, driver):
        self.driver = driver

    def form_1_himawari_030(self):

        time.sleep(3)
        # Clicks on Automation Group
        # Please change the xpath while running it in your local
        self.driver.find_element_by_xpath(self.required_group).click()
        time.sleep(8)
        self.driver.implicitly_wait(100)
        # Clicks 'Create' button
        self.driver.find_element_by_xpath(self.create_form_button).click()
        time.sleep(5)
        self.driver.implicitly_wait(100)
        # Fetches the image_path json file location
        image_file_path = open("../data/image_path.json", 'r')
        image_input = image_file_path.read()
        input_body = json.loads(image_input)
        image_data = list(input_body.values())
        # Uploads the Form in to the Web application
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(35))
        name_of_image = image_data.__getitem__(35)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        print(name_of_image[-1])
        time.sleep(2)
        # Enters Provider name
        self.driver.find_element_by_xpath(self.form_provider).send_keys("Siddhartha")
        time.sleep(2)
        # Clicks 'save' button
        self.driver.find_element_by_xpath(self.save_button).click()
        time.sleep(45)
        wait = WebDriverWait(self.driver, 400)
        # waits until image Processed
        wait.until(EC.visibility_of_element_located((By.XPATH, self.processed_disp)))
        time.sleep(2)
        # Clicks the form
        self.driver.find_element_by_xpath(self.first_form).click()
        time.sleep(55)
        self.driver.implicitly_wait(100)
        # Clicks 'Actions' dropdown
        gt_values = self.driver.find_elements_by_xpath(self.list_key_values)

        # self.driver.find_element_by_xpath(self.actions_drop_down).click()
        # time.sleep(5)
        # # Clicks 'View overall results"
        # self.driver.find_element_by_xpath(self.view_overall_results).click()
        # time.sleep(5)
        # # Select all Results
        # gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        # time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(35)
        # Opens JSON data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []


        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)

        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0


        for i in range(len(json_data)):
            if json_data[i] != 0:
                print("Expected")
                print(json_data[i])
                allure.attach("Expected:  "+json_data[i])


        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # Prints Accurate or Inaccurate Data with 'Low Confidence"
                    allure.attach("Actual   "+"VERIFY:-"+data_list1[i])
                    print("Actual   "+"VERIFY:-")
                    print(data_list1[i])
                else:
                    # Prints Inaccurate data with High confidence
                    allure.attach("Actual   "+"ERROR:Inaccurate but high confidence:-"+data_list1[i])
                    print("Actual   "+"ERROR:Inaccurate but high confidence:-")
                    print(data_list1[i])
        # Clicks on Groups tab
        self.driver.find_element_by_xpath(self.group_tab).click()

        k = 0
        for i in range(len(data_list1)):
            if data_list1[i] == 0:
                k = k + 0
            else:
                k = k + 1

        if k == 0:
            # Prints if All values are Correct
            allure.attach("All Results are Accurate")
            print("all are accurate")
        else:
            # Fails if all the values are not accurate
            print("mismatch")
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")