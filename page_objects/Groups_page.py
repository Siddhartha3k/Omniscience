import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import openpyxl
import os
import requests
import json


class Test_Groups_page():

    def __init__(self, driver):
        self.driver = driver

    def click_a_groups_tab(self):
        self.driver.find_element_by_xpath("//*[text()='Groups']").click()
        time.sleep(2)
        Primary_Count_of_groups = self.driver.find_elements_by_xpath("//div[@class='row entity-main']")
        self.driver.find_element_by_xpath("//*[@class='fa fa-sort-down']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@routerlink='create']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@placeholder='Group Name']").send_keys("Testing Automation")
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@placeholder='Group Description']").send_keys("Description Testing ")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
        time.sleep(2)

        Secondary_Count_of_groups = self.driver.find_elements_by_xpath("//div[@class='row entity-main']")
        if Secondary_Count_of_groups != Primary_Count_of_groups:
            print("Group Created")
        else:
            print("Group not created")
        intial_group_name = self.driver.find_element_by_xpath("(//*[@class='row entity-main'])[last()]/child::*[1]")
        intial_group_name = intial_group_name.text
        time.sleep(2)
        self.driver.find_element_by_xpath("(//*[@type='radio'])[last()]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@class='fa fa-sort-down']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@placeholder='Group Name']").clear()
        self.driver.find_element_by_xpath("//*[@placeholder='Group Description']").clear()
        self.driver.find_element_by_xpath("//*[@placeholder='Group Name']").send_keys("Testing Automation change name")
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@placeholder='Group Description']").send_keys(
            "Change Description Testing ")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
        time.sleep(2)
        after_change_group_name = self.driver.find_element_by_xpath(
            "(//*[@class='row entity-main'])[last()]/child::*[1]")
        after_change_group_name = after_change_group_name.text
        time.sleep(2)
        if after_change_group_name != intial_group_name:
            print("Group name is edited")
        else:
            print("Group name is not edited")
        self.driver.find_element_by_xpath("(//*[@type='radio'])[last()]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@class='fa fa-sort-down']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@data-target='#deleteFormGroup']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@class='btn btn-sm btn-danger']").click()
        after_delete_count_of_group = self.driver.find_elements_by_xpath("//div[@class='row entity-main']")
        if after_delete_count_of_group == Primary_Count_of_groups:
            print("Group Deleted")
        else:
            print("Group not Deleted")
