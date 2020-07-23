import unittest
import HtmlTestRunner
from selenium import webdriver
import os
import sys
from Android_directory.Android_test2 import Automation_android, driver


class Android_Runner_class(unittest.TestCase):
    auto_android = Automation_android(driver)

    @classmethod
    def setUpClass(cls):
        print("test starts")

    def test_a_desired_capabilities(self):
        self.auto_android.set_desired_capabilities()

    def test_b_capture_image_standard_scenario(self):
        self.auto_android.click_menu_tab()
        self.auto_android.click_home_button()
        self.auto_android.click_start_new_assessment()
        self.auto_android.click_capture_button()
        self.auto_android.click_next_button()
        self.auto_android.click_send_document()
        self.auto_android.get_results_text()

    def test_c_capture_ar_scenario(self):
        self.auto_android.click_start_new_assessment()
        self.auto_android.click_ar()
        self.auto_android.click_next_button()
        self.auto_android.click_send_document()
        self.auto_android.get_results_text()

    def test_d_standard_delete_one_image(self):
        self.auto_android.click_start_new_assessment()
        self.auto_android.click_capture_button()
        self.auto_android.click_capture_button()
        self.auto_android.click_next_button()
        self.auto_android.select_a_form()
        self.auto_android.delete_a_form()
        self.auto_android.click_send_document()
        self.auto_android.get_results_text()

    def test_e_standard_delete_all_images(self):
        self.auto_android.click_start_new_assessment()
        self.auto_android.click_capture_button()
        self.auto_android.click_capture_button()
        self.auto_android.click_next_button()
        self.auto_android.click_select_button()
        self.auto_android.click_select_all_button()
        self.auto_android.delete_all_forms()

    # def test_f_gallery_scenario(self):

    #     self.auto_android.click_start_new_assessment()
    #     self.auto_android.click_gallery()
    #     self.auto_android.click_select_image()
    #     self.auto_android.click_next_button()
    #     self.auto_android.click_send_document()
    #     self.auto_android.get_results_text()

    # def test_g_gallery_delete_a_image(self):

    #     self.auto_android.click_start_new_assessment()
    #     self.auto_android.click_gallery()
    #     self.auto_android.click_select_image()
    #     self.auto_android.click_gallery()
    #     self.auto_android.click_select_image2()
    #     self.auto_android.click_next_button()
    #     self.auto_android.select_a_form()
    #     self.auto_android.delete_a_form()
    #     self.auto_android.click_send_document()
    #     self.auto_android.get_results_text()

    # def test_h_gallery_delete_all_images(self):

    #     self.auto_android.click_start_new_assessment()
    #     self.auto_android.click_gallery()
    #     self.auto_android.click_select_image()
    #     self.auto_android.click_gallery()
    #     self.auto_android.click_select_image2()
    #     self.auto_android.click_next_button()
    #     self.auto_android.click_select_button()
    #     self.auto_android.click_select_all_button()
    #     self.auto_android.delete_all_forms()

    def test_i_standard_capture_multiple_images(self):
        self.auto_android.click_start_new_assessment()
        self.auto_android.click_capture_button()
        self.auto_android.click_capture_button()
        self.auto_android.click_next_button()
        self.auto_android.click_send_document()
        self.auto_android.get_results_text()

    def test_j_delete_image_ar_scenario(self):
        self.auto_android.click_start_new_assessment()
        self.auto_android.click_ar()
        self.auto_android.click_ar()
        self.auto_android.click_next_button()
        self.auto_android.select_a_form()
        self.auto_android.delete_a_form()
        self.auto_android.click_send_document()
        self.auto_android.get_results_text()

    def test_k_delete_all_images_ar_scenario(self):
        self.auto_android.click_start_new_assessment()
        self.auto_android.click_ar()
        self.auto_android.click_ar()
        self.auto_android.click_next_button()
        self.auto_android.click_select_button()
        self.auto_android.click_select_all_button()
        self.auto_android.delete_all_forms()

    def test_l_delete_and_capture_standard_scenario(self):
        self.auto_android.click_start_new_assessment()
        self.auto_android.click_capture_button()
        self.auto_android.click_capture_button()
        self.auto_android.click_next_button()
        self.auto_android.click_select_button()
        self.auto_android.click_select_all_button()
        self.auto_android.delete_forms()
        self.auto_android.click_capture_button()
        self.auto_android.click_next_button()
        self.auto_android.click_send_document()
        self.auto_android.get_results_text()

    def test_m_delete_and_capture_ar_scenario(self):
        self.auto_android.click_start_new_assessment()
        self.auto_android.click_ar()
        self.auto_android.click_ar()
        self.auto_android.click_next_button1()
        self.auto_android.click_select_button()
        self.auto_android.click_select_all_button()
        self.auto_android.delete_forms()
        self.auto_android.click_ar()
        self.auto_android.click_next_button1()
        self.auto_android.click_send_document()
        self.auto_android.get_results_text()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='D:/Automation/Omni_Test_Automation/reports'))
