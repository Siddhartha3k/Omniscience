import os
import unittest
import time
from appium import webdriver

from selenium.webdriver import DesiredCapabilities

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

desired_caps = DesiredCapabilities.IPHONE
desired_caps['deviceName'] = 'iPad 6'
desired_caps['platformVersion'] = '12.2'
desired_caps['platformName'] = 'iOS'
desired_caps['xcodeOrgId'] = '89DPCZNK6E'
desired_caps['noReset']: 'true'
desired_caps['bundleId']: 'omniscience.MobileOCR'
desired_caps['automationName']: 'XCUITest'
desired_caps['udid'] = '25f53f38592c583f31dbb64e0d511527f19bacd3'
desired_caps['updateWDABundleId']: 'omniscience.MobileOCR'
desired_caps['app'] = PATH('/Users/joeyfrmfrnds/Downloads/MobileOCR.ipa')
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
time.sleep(1)
driver.implicitly_wait(100)
driver.find_element_by_xpath("//*[@type='XCUIElementTypeTextField']").send_keys("abchjk@gmail.com")
driver.find_element_by_xpath("//*[@name='Continue']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@value='Enter password']").send_keys("1234567")
driver.find_element_by_xpath("//*[@name='Log In']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@name='Settings']").click()
driver.find_element_by_xpath("//*[contains(@name,'MegaOCR Region:')]").click()
driver.find_element_by_xpath("//*[@name='QA']").click()
time.sleep(1)
driver.implicitly_wait(100)
driver.find_element_by_accessibility_id("Ok").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@label='Declarations in capture']/following::*[2]").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@name='Home']").click()
driver.find_element_by_xpath("//*[@name='Capture Form']").click()
time.sleep(1)
driver.implicitly_wait(100)
driver.find_element_by_accessibility_id("OK").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@label='Capture']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@label='Accept']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@label='Proceed']").click()
time.sleep(2)
driver.implicitly_wait(100)
driver.find_element_by_xpath("//*[@label='Next']").click()
driver.implicitly_wait(100)
for x in range(5):
    driver.find_element_by_xpath("//*[@label='No']").click()
driver.find_element_by_xpath("//*[@label='Submit Declaration']").click()
