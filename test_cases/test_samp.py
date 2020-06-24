from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import os
import time
import json
# D:\Automation\Omni_Test_Automation\data\data_names.json
file1 = open("D:/Automation/Omni_Test_Automation/data/data_names.json", 'r', encoding="utf8")
json_input = file1.read()
inputBody = json.loads(json_input)
json_data = list(inputBody.values())
print("Json_data:")
print(json_data)
