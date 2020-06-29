from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import os
import time
import json
# D:\Automation\Omni_Test_Automation\data\data_names.json
# file1 = open("D:/Automation/Omni_Test_Automation/data/data_names.json", 'r', encoding="utf8")
# json_input = file1.read()
# inputBody = json.loads(json_input)
# json_data = list(inputBody.values())
# print("Json_data:")
# print(json_data)

abc=[]
xyz=[]
file1 = open("D:/git/Omniscience/data/json_file_paths.json", 'r', encoding="utf8")
json_input = file1.read()
inputBody = json.loads(json_input)
json_data = list(inputBody.values())

for i in range(len(json_data)):

    file1 = open("D:/git/Omniscience/data/json_file_paths.json", 'r', encoding="utf8")
    json_input = file1.read()
    inputBody = json.loads(json_input)
    json_data = list(inputBody.values())
    abc = json_data.__getitem__(i)

    file1 = open(abc, 'r',encoding="utf8")  # Opens JSON data
    json_input = file1.read()
    input_body = json.loads(json_input)
    json_data = list(input_body.values())
    print(json_data)

    file2 = open("D:/git/Omniscience/data/image_path.json", 'r', encoding="utf8")
    json_input1 = file2.read()
    inputBody1 = json.loads(json_input1)
    json_data1 = list(inputBody1.values())
    xyz = json_data1.__getitem__(i)
    #print(xyz)






