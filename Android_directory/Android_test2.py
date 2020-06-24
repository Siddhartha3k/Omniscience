import os
import unittest
import time
from appium import webdriver

from selenium.webdriver import DesiredCapabilities

driver = webdriver


class Automation_android(unittest.TestCase):

    menu_tab = "//*[@resource-id='com.omniocr:id/Image_view_menu']"
    home_button = "//*[@text='Home']"
    self_assessment = "//*[@text='Start new assessment']"
    capture_button = "//*[@resource-id='com.omniocr:id/clickme']"
    gallery_button = "//*[@resource-id='com.omniocr:id/clickme_gallary']"
    next_button = "//*[@resource-id='com.omniocr:id/text_access']"
    select_image = "//*[@index='1']"
    select_image2 = "//*[@index='2']"
    send_document = "//*[@text='Send documents for assessment.']"
    results_data1 = "//*[@resource-id='com.omniocr:id/text1' or @resource-id='com.omniocr:id/text2']"
    ar = "//*[@resource-id='com.omniocr:id/text_ar']"
    form_1 = "//*[@resource-id='com.omniocr:id/image_list_rv']/child::*[1]"
    # form_1 = "(//*[@class='android.view.ViewGroup'])[1]"
    delete = "//*[@resource-id='com.omniocr:id/delete']"
    cancel = "//*[@text='Cancel']"
    select = "//*[@text='Select']"
    select_all = "//*[@text='Select All']"
    click_here = "//*[@resource-id='com.omniocr:id/text1']"
    required_attention = "//*[@resource-id='com.omniocr:id/required_attention']"

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def set_desired_capabilities(self):
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )
        dc = DesiredCapabilities.ANDROID
        dc["deviceName"] = "Redmi Note 7S"
        dc["platformVersion"] = "9"
        dc["platformName"] = "Android"
        dc["noReset"] = "true"
        dc["appPackage"] = "com.omniocr"
        dc["appActivity"] = ".MainActivity"
        dc["browserName"] = ""
        dc["automationName"] = "UiAutomator2"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", dc)

    def click_menu_tab(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.menu_tab).click()

    def click_home_button(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.home_button).click()

    def click_start_new_assessment(self):
        time.sleep(2)
        verify_start_button = self.driver.find_element_by_xpath(self.self_assessment).text
        self.assertTrue(verify_start_button == "Start new assessment", "Start New Assessment button is not visible")
        self.driver.find_element_by_xpath(self.self_assessment).click()

    def click_capture_button(self):
        time.sleep(3)
        self.driver.find_element_by_xpath(self.capture_button).click()
        time.sleep(3)

    def click_next_button(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.next_button).click()
        time.sleep(4)
        #self.driver.back()

    def click_next_button1(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.next_button).click()
        time.sleep(2)

    def click_gallery(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.gallery_button).click()

    def click_select_image(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.select_image).click()

    def click_select_image2(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.select_image2).click()

    def click_send_document(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.send_document).click()

    def get_results_text(self):
        self.driver.implicitly_wait(90)
        validate_keys = self.driver.find_element_by_xpath(self.required_attention).text
        self.assertTrue(validate_keys == "Required attention", "User didn't landed on Key value screen")
        data_list1 = []
        time.sleep(2)
        result_data = self.driver.find_elements_by_xpath(self.results_data1)
        for data in result_data:
            data_list = data.text
            data_list1.append(data_list)

        time.sleep(2)

        #self.driver.back()
        self.driver.back()
        # print("Data List1:")
        # self.driver.back
        # self.driver.execute_script("window.history.go(-1)")

        # print("学校学校学校学校学校学校")
        # print(data_list1)

    def click_ar(self):
        time.sleep(4)
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(self.ar).click()
        time.sleep(7)

    def select_a_form(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.form_1).click()

    def delete_a_form(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.delete).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.cancel).click()
        time.sleep(2)

    def click_select_button(self):
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(self.select).click()

    def click_select_all_button(self):
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(self.select_all).click()

    def delete_all_forms(self):
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(self.delete).click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(self.click_here).click()
        time.sleep(1)
        self.driver.back()
        self.driver.back()
        self.driver.back()

    def delete_forms(self):
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(self.delete).click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(self.click_here).click()
        time.sleep(1)


# a= Automation_android()
# a.Set_desired_capabilities()
# a.click_menu_tab()
# a.click_home_button()
# a.click_Start_new_assesment()
# a.click_capture_button()
# a.click_next_button()
# a.click_send_document()
# a.get_results_text()

