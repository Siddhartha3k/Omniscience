import json
import time
from selenium.webdriver.common.action_chains import ActionChains

class Test_Groups_page():

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

    def __init__(self, driver):
        self.driver = driver

    def click_a_groups_tab(self):
        time.sleep(15)
        self.driver.find_element_by_xpath(self.group_tab).click()


    def click_b_first_group(self):
        time.sleep(4)
        self.driver.find_element_by_xpath(self.first_group).click()
        time.sleep(4)


    def click_c_first_form(self):
        time.sleep(20)
        self.driver.refresh()
        time.sleep(20)
        self.driver.find_element_by_xpath(self.first_form).click()
        time.sleep(15)

    def click_d_actions_drop_down(self):
        time.sleep(4)
        self.driver.find_element_by_xpath(self.page_navigation).click()
        time.sleep(15)
        self.driver.find_element_by_xpath(self.actions_drop_down).click()
        time.sleep(5)


    def click_e_view_overall_results(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.view_overall_results).click()
        time.sleep(3)

    def check_list_of_data(self):
        time.sleep(3)
        GT_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)
        data_list1 = []
        for data in GT_values:
            data_list = data.text
            #print(data_list)
            data_list1.append(data_list)
        # data_list1.pop(0)
        print("Data List1:")
        print(data_list1)

    def get_f_list_of_form_values(self):
        time.sleep(3)
        GT_values = self.driver.find_elements_by_xpath(self.list_of_all_values)
        time.sleep(5)
        file1 = open("D:/Automation/Omni_Test_Automation/data/data_names.json", 'r', encoding="utf8")
        json_input = file1.read()
        inputBody = json.loads(json_input)
        json_data = list(inputBody.values())
        data_list1 = []
        for data in GT_values:
            data_list = data.text
            data_list1.append(data_list)

        for i in range(len(json_data)):
            for j in range(len(data_list1)):
                if data_list1[j] == json_data[i]:
                    data_list1[j] = 0
                    json_data[i] = 0

        print("------------------------------------------------------")
        print("Expected Data: ")
        for i in range(len(json_data)):
            if json_data[i] != 0:
                print(json_data[i])
        print("------------------------------------------------------")
        print("------------------------------------------------------")
        print("Actual Data:")
        for i in range(len(data_list1)):
            if data_list1[i] != 0:
                print(data_list1[i])
        print("------------------------------------------------------")


    def click_g_view_decision_form(self):
        time.sleep(2)
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(self.view_decision).click()

    def click_h_click_create_form(self):
        time.sleep(2)
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(self.create_form_button).click()

    def upload_i_form(self):
        time.sleep(5)
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_xpath(self.browse_form).send_keys("E://Forms_1/FormA-4.png")

    def click_automation_group(self):
        time.sleep(3)
        self.driver.find_element_by_xpath(self.required_group).click()
        time.sleep(8)

    def enter_form_provider(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.form_provider).send_keys("Siddhartha")

    def click_save_button(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.save_button).click()
        time.sleep(5)



