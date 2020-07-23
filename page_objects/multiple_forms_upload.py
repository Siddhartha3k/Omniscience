import json
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Test_multiple_form_upload(unittest.TestCase):
    # Element Locators
    group_tab = "(//a[@class='nav-link'])[3]"
    first_group = "(//span[@class='btn-link'])[1]"
    required_group = "//*[text()='Automation_group']"
    first_form = "(//*[@class='btn-link'])[1]"
    page_navigation = "(//*[@class='btn btn-info btn-sm'])[2]"
    actions_drop_down = "//*[@id='actionsMenuButton']"
    view_overall_results = "(//*[@class='dropdown-item'])[5]"
    list_of_all_values = "//*[@class='form-detail-item']"
    view_decision = "//*[text()='View Decision ']"
    create_form_button = "//*[@routerlink='create']"
    browse_form = "//*[@class='custom-file-input']"
    form_provider = "//*[@id='form-provider']"
    save_button = "//button[@class='btn btn-primary']"
    processed_disp = "(//*[@title='Processed'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def click_a_groups_tab(self):
        time.sleep(15)
        self.driver.find_element_by_xpath(self.group_tab).click()  # Clicks on Group tab

    def upload_and_validate_b_multiple_forms(self):

        image_file_path = open("../data/image_path.json", 'r')  # Fetches the image_path json file location
        image_input = image_file_path.read()
        input_body = json.loads(image_input)
        image_data = list(input_body.values())
        no_of_forms = image_data.__len__()  # Fetches no.of images

        for i in range(no_of_forms):
            time.sleep(3)
            # Clicks on Automation Group
            # Please change the xpath while running it in your local
            self.driver.find_element_by_xpath(self.required_group).click()
            time.sleep(8)
            self.driver.implicitly_wait(100)
            self.driver.find_element_by_xpath(self.create_form_button).click()  # Clicks 'Create' button
            time.sleep(5)
            self.driver.implicitly_wait(100)
            # Uploads the Form in to the Web application
            self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(i))
            print(image_data.__getitem__(i))
            name_of_image = image_data.__getitem__(i)
            name_of_image = name_of_image.split('/')
            print(name_of_image[-1])  # Prints the name of the Form
            time.sleep(2)
            self.driver.find_element_by_xpath(self.form_provider).send_keys("Siddhartha")  # Enters Provider name
            time.sleep(2)
            self.driver.find_element_by_xpath(self.save_button).click()  # Clicks 'save' button
            time.sleep(45)
            wait = WebDriverWait(self.driver, 400)
            wait.until(EC.visibility_of_element_located((By.XPATH, self.processed_disp)))  # waits until image Processed
            time.sleep(2)
            self.driver.find_element_by_xpath(self.first_form).click()  # Clicks the form
            time.sleep(35)
            self.driver.find_element_by_xpath(self.actions_drop_down).click()  # Clicks 'Actions' dropdown
            time.sleep(5)
            self.driver.find_element_by_xpath(self.view_overall_results).click()  # Clicks 'View overall results"
            time.sleep(3)
            time.sleep(3)
            # gets all Web Results
            actual_web_key_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
            time.sleep(5)

            # Fetches the location of Json file that contains Expected Key values Json file paths
            json_file_path = open("../data/json_file_paths.json", 'r')
            json_input = json_file_path.read()
            input_body = json.loads(json_input)
            json_data = list(input_body.values())
            self.expected_json_data = json_data.__getitem__(i)
            file1 = open(self.expected_json_data, 'r', encoding="utf8")  # Opens JSON data
            json_input = file1.read()
            input_body = json.loads(json_input)
            json_data = list(input_body.values())
            data_list1 = []

            for data in actual_web_key_values:
                data_list = data.text
                data_list1.append(data_list)  # Gets all Web Results into a List

            for i in range(len(json_data)):
                for j in range(len(data_list1)):
                    if data_list1[j] == json_data[i]:  # Comparing the Actual values with Expected Values
                        data_list1[j] = 0
                        json_data[i] = 0

            print("------------------------------------------------------")
            print("Expected Data: ")
            for i in range(len(json_data)):
                if json_data[i] != 0:  # Prints the Expected Data which was not found in Web Results
                    print(json_data[i].encode("utf-8"))
            print("------------------------------------------------------")
            print("Actual Data:")
            for i in range(len(data_list1)):  # Prints the Actual Results that are Inaccurate or Low Confidence
                if data_list1[i] != 0:
                    if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                        print("VERIFY:  ")
                        print(data_list1[i].encode("utf-8"))
                    else:
                        print("ERROR:  Inaccurate but high confidence  ")
                        print(data_list1[i].encode("utf-8"))
            print("*********************************************************")
            time.sleep(15)
            self.driver.find_element_by_xpath(self.group_tab).click()  # Clicks on Groups tab
