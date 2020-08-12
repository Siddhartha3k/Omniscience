import json
import time
import unittest
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Test_individual_form_upload(unittest.TestCase):
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

    def form_1_hanasaku_test_0(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(0))
        name_of_image = image_data.__getitem__(0)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(0)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_2_hanasaku_test_1(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(1))
        name_of_image = image_data.__getitem__(1)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(1)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_3_hanasaku_test_2(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(2))
        name_of_image = image_data.__getitem__(2)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(2)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_4_hanasaku_test_3(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(3))
        name_of_image = image_data.__getitem__(3)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(3)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_5_hanasaku_test_4(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(4))
        name_of_image = image_data.__getitem__(4)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(4)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_6_hanasaku_test_8(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(5))
        name_of_image = image_data.__getitem__(5)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(5)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_7_himawari_01_2(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(6))
        name_of_image = image_data.__getitem__(6)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(6)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_8_himawari_01_3(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(7))
        name_of_image = image_data.__getitem__(7)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(7)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_9_himawari_03_0(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(8))
        name_of_image = image_data.__getitem__(8)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(8)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_10_himawari_05_0(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(9))
        name_of_image = image_data.__getitem__(9)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(9)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                          + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Missing Key Values:- "
                          + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_11_himawari_05_1(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(10))
        name_of_image = image_data.__getitem__(10)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(10)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_12_himawari_07_1(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(11))
        name_of_image = image_data.__getitem__(11)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(11)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_13_himawari_07_3(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(12))
        name_of_image = image_data.__getitem__(12)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(12)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_14_DL_HC_High(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(13))
        name_of_image = image_data.__getitem__(13)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(13)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_15_DL_HC_Left_1(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(14))
        name_of_image = image_data.__getitem__(14)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(14)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_16_HC_HCDate_2(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(15))
        name_of_image = image_data.__getitem__(15)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(15)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_17_HC_HCDate_3(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(16))
        name_of_image = image_data.__getitem__(16)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        time.sleep(65)
        self.driver.implicitly_wait(100)
        # Clicks 'Actions' dropdown
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(16)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_18_HC_HCDate_4(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(17))
        name_of_image = image_data.__getitem__(17)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(17)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_19_Feb_18_Medical_Exam_1_1(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(18))
        name_of_image = image_data.__getitem__(18)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(18)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_20_Feb_18_Medical_Exam_1_2(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(19))
        name_of_image = image_data.__getitem__(19)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(19)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_21_Feb_18_Medical_Exam_2_0(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(20))
        name_of_image = image_data.__getitem__(20)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        time.sleep(65)
        self.driver.implicitly_wait(100)
        # Clicks 'Actions' dropdown
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(20)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_22_Feb_18_Medical_Exam_2_1(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(21))
        name_of_image = image_data.__getitem__(21)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(21)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_23_Feb_18_Medical_Exam_3_0(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(22))
        name_of_image = image_data.__getitem__(22)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(22)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_24_Feb_18_Medical_Exam_3_1(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(23))
        name_of_image = image_data.__getitem__(23)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        time.sleep(65)
        self.driver.implicitly_wait(100)
        # Clicks 'Actions' dropdown
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(23)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_25_Feb_18_Medical_Exam_6_1(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(24))
        name_of_image = image_data.__getitem__(24)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(24)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_26_Feb_18_Medical_Exam_6_2(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(25))
        name_of_image = image_data.__getitem__(25)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(25)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_27_Feb_18_Medical_Exam_7_1(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(26))
        name_of_image = image_data.__getitem__(26)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(26)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_28_Feb_18_Medical_Exam_7_2(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(27))
        name_of_image = image_data.__getitem__(27)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(27)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_29_Feb_18_Medical_Exam_7_3(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(28))
        name_of_image = image_data.__getitem__(28)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        time.sleep(65)
        self.driver.implicitly_wait(100)
        # Clicks 'Actions' dropdown
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(28)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_30_acc_test_4(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(29))
        name_of_image = image_data.__getitem__(29)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(29)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_31_acc_test_6(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(30))
        name_of_image = image_data.__getitem__(30)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(30)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_32_acc_test_9(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(31))
        name_of_image = image_data.__getitem__(31)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(31)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_33_acc_test_25(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(32))
        name_of_image = image_data.__getitem__(32)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(32)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_34_Feb_18_Medical_Exam_11_0(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(33))
        name_of_image = image_data.__getitem__(33)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(33)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_35_HC_1_pdf(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(34))
        name_of_image = image_data.__getitem__(34)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(34)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_36_HC_2_pdf(self):

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
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(35)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_37_HC_8_pdf(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(36))
        name_of_image = image_data.__getitem__(36)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(36)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_38_HC_9_pdf(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(37))
        name_of_image = image_data.__getitem__(37)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(37)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_39_HC_10_pdf(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(38))
        name_of_image = image_data.__getitem__(38)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(38)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_40_ca_1(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(39))
        name_of_image = image_data.__getitem__(39)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(39)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_41_ca_2(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(40))
        name_of_image = image_data.__getitem__(40)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(40)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

    def form_42_ca_3(self):

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
        self.driver.find_element_by_xpath(self.browse_form).send_keys(image_data.__getitem__(41))
        name_of_image = image_data.__getitem__(41)
        name_of_image = name_of_image.split('/')
        # Prints the name of the Form
        allure.attach(name_of_image[-1])
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
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)
        # Clicks 'View overall results"
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(5)
        # Select all Results
        gt_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)

        json_file_path = open("../data/json_file_paths.json", 'r')
        json_input = json_file_path.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        self.expected_json_data = json_data.__getitem__(41)
        # Opens JSON(Original Form) data
        file1 = open(self.expected_json_data, 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        json_data = list(input_body.values())
        data_list1 = []
        for data in gt_values:
            data_list = data.text
            # Gets all Web Results into a List
            data_list1.append(data_list)
        # Compares the Actual data with Expected data
        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0
        expected_data = []
        actual_data = []
        actual_data2 = []
        for i in range(len(json_data)):
            if json_data[i] != 0:
                expected_data.append(json_data[i])

        expected_key_values = expected_data
        expected_data1 = expected_data
        next_line = '\n'
        split_list = next_line.join(expected_data1)
        split_expected_data = split_list.split()
        # Fetching the English Keys data
        file1 = open("../data/all_keys_english.json", 'r', encoding="utf8")
        json_input = file1.read()
        input_body = json.loads(json_input)
        english_data = list(input_body.values())
        english_keys = []
        for i in english_data:
            for j in split_expected_data:
                if j == i.partition(next_line)[2]:
                    # Getting all the english data in to a list
                    english_keys.append(i)
        # Eliminating the Duplicate keys
        english_keys = list(set(english_keys))
        english_keys1 = []
        for item1 in enumerate(english_keys, 1):
            english_keys1.append(item1)
        english_keys = str(english_keys1)
        english_keys = english_keys.replace(",", ".")
        # Printing the Expected Keys in English
        allure.attach("Issues :- " + english_keys.replace("\\n", " "))

        expected_data2 = []
        for item1 in enumerate(expected_data, 1):
            expected_data2.append(item1)
        expected_data = str(expected_data2)
        expected_data = expected_data.replace(",", ".")
        expected_data = expected_data.replace('\\n', ' ')
        # Printing the Expected Key values
        allure.attach("EXPECTED KEY VALUES :-  " + expected_data)
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                if data_list1[i].__contains__("Low Confidence. Please Verify this Key's Values"):
                    # VERIFY:Prints Accurate or Inaccurate Data with 'Low Confidence"
                    actual_data.append(data_list1[i])
                else:
                    # ERROR: Prints Inaccurate data with High confidence
                    actual_data2.append(data_list1[i])
        actual_key_values = actual_data + actual_data2
        actual_key_values = list(set(actual_key_values))
        word = ["Low Confidence. Please Verify this Key's Values"]
        output = []
        for i in range(0, len(actual_key_values)):
            for j in range(0, len(word)):
                a = actual_key_values[i].find(word[j])
                if a != -1:
                    actual_key_values[i] = actual_key_values[i].replace(word[j], '')
            actual_key_values[i] = actual_key_values[i].strip()
            if actual_key_values[i] != '':
                output.append(actual_key_values[i])

        dummy_list1 = []
        dummy_list2 = []
        dummy_list3 = []
        missing_key_values = []
        for i in expected_key_values:
            res1 = i.partition(next_line)[0]
            dummy_list1.append(res1)
        for j in dummy_list1:
            for k in output:
                if j in k:
                    dummy_list2.append(j)
        for i in range(len(dummy_list1)):
            for j in range(len(dummy_list2)):
                if dummy_list2[j] == dummy_list1[i]:
                    dummy_list1[i] = 0
                    dummy_list2[j] = 0

        for i in range(len(dummy_list1)):
            if dummy_list1[i] != 0:
                dummy_list3.append(dummy_list1[i])
        for i in expected_key_values:
            for j in dummy_list3:
                if j in i:
                    missing_key_values.append(i)

        dummy_list1.clear()
        dummy_list2.clear()
        dummy_list3.clear()
        missing_key_values1 = []
        for item1 in enumerate(missing_key_values, 1):
            missing_key_values1.append(item1)
        missing_key_values1 = str(missing_key_values1)
        missing_key_values1 = missing_key_values1.replace(",", ".")
        missing_key_values1 = missing_key_values1.replace('\\n', ' ')

        actual_data5 = []
        for item1 in enumerate(actual_data, 1):
            actual_data5.append(item1)
        actual_data = str(actual_data5)
        actual_data = actual_data.replace(",", ".")
        actual_data = actual_data.replace('\\n', ' ')
        actual_data = actual_data.replace("Low Confidence. Please Verify this Key's Values", ' ')
        actual_data6 = []

        wrong_key_values = []
        for i in range(len(expected_key_values)):
            for j in range(len(actual_data2)):
                if actual_data2[j] == expected_key_values[i]:
                    expected_key_values[i] = 0
                    actual_data2[j] = 0

        for i in range(len(actual_data2)):
            if output[i] != 0:
                wrong_key_values.append(actual_data2[i])

        for item1 in enumerate(wrong_key_values, 1):
            actual_data6.append(item1)
        wrong_key_values1 = actual_data6
        wrong_key_values1 = str(wrong_key_values1)
        wrong_key_values1 = wrong_key_values1.replace(",", ".")
        wrong_key_values1 = wrong_key_values1.replace('\\n', ' ')
        # Prints Web data from Results screen
        if wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() == 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- " + actual_data)
        elif wrong_key_values1.__len__() > 2 and missing_key_values1.__len__() == 2:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data
                + " Wrongly Predicted Key values:-  " + wrong_key_values1)
        elif wrong_key_values1.__len__() == 2 and missing_key_values1.__len__() > 2:
            allure.attach("ACTUAL: " + "Low Confidence Key Values:- "
                          + actual_data + " Missing Key Values:- " + missing_key_values1)
        else:
            allure.attach(
                "ACTUAL: " + "Low Confidence Key Values:- " + actual_data + " Wrongly Predicted Key values:-  "
                + wrong_key_values1 + " Missing Key Values:- " + missing_key_values1)
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
        elif wrong_key_values1.__len__() > 2 or missing_key_values1.__len__() > 2:
            # Assertion Fails if all the values are not accurate
            assert str(expected_data) == str(wrong_key_values1)

        else:
            # Fail if if there is a Mismatch in Web data with Expected data
            pytest.xfail("Test Case Fail due to Mismatch in Key value data")

