import os
import unittest
import time
from appium import webdriver

from selenium.webdriver import DesiredCapabilities

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
driver = webdriver.Remote("http://localhost:4723/wd/hub", dc)
time.sleep(5)
driver.find_element_by_xpath("//*[@resource-id='com.omniocr:id/Image_view_menu']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@text='Home']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@text='Start new assessment']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@resource-id='com.omniocr:id/clickme_gallary']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@index='1']").click()
