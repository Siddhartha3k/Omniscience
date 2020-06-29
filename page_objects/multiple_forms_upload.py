import json
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Test_multiple_form_upload(unittest.TestCase):

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

    def __init__(self, driver):
        self.driver = driver

    def click_a_groups_tab(self):
        time.sleep(15)
        self.driver.find_element_by_xpath(self.group_tab).click()


    def upload_b_multiple_forms(self):

        for i in range(2):
            time.sleep(3)
            self.driver.find_element_by_xpath(self.required_group).click()
            time.sleep(8)
            time.sleep(2)
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_xpath(self.create_form_button).click()
            time.sleep(5)
            self.driver.implicitly_wait(100)
            image_file_path = open("D:/git/Omniscience/data/image_path.json", 'r')
            image_input = image_file_path.read()
            input_body = json.loads(image_input)
            image_data = list(input_body.values())

            self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(i))
            time.sleep(2)
            self.driver.find_element_by_xpath(self.form_provider).send_keys("Siddhartha")
            time.sleep(2)
            self.driver.find_element_by_xpath(self.save_button).click()
            time.sleep(5)
            time.sleep(45)
            wait = WebDriverWait(self.driver, 400)
            wait.until(EC.visibility_of_element_located((By.XPATH, self.processed_disp)))  # waits until image Processed
            time.sleep(2)
            self.driver.find_element_by_xpath(self.first_form).click()  # Clicks the form
            time.sleep(35)
            self.driver.find_element_by_xpath(self.actions_drop_down).click()
            time.sleep(5)
            self.driver.find_element_by_xpath(self.view_overall_results).click()
            time.sleep(3)
            time.sleep(3)
            gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)  # Select all Results
            time.sleep(5)

            json_file_path = open("D:/git/Omniscience/data/json_file_paths.json", 'r')
            json_input = json_file_path.read()
            input_body = json.loads(json_input)

            json_data = list(input_body.values())
            self.abc = json_data.__getitem__(i)
            file1 = open(self.abc, 'r', encoding="utf8")  # Opens JSON data
            json_input = file1.read()
            input_body = json.loads(json_input)
            json_data = list(input_body.values())
            data_list1 = []

            for data in gt_values:
                data_list = data.text
                data_list1.append(data_list)  # Gets all Web Results into a List

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
            time.sleep(15)
            self.driver.find_element_by_xpath(self.group_tab).click()






