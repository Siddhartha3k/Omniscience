from page_objects.Login_page import Test_Login_page
import unittest
from selenium import webdriver
import os
import json
from page_objects.individul_forms import Test_individual_form_upload
from page_objects.multiple_forms_upload import Test_multiple_form_upload


class Form_upload(unittest.TestCase):
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    DRIVER_BIN = os.path.join(PROJECT_ROOT, "../drivers/chromedriver")
    driver = webdriver.Chrome(executable_path=DRIVER_BIN)
    baseURL = "https://megaocr-ui-rgacf-daiichi.omni.sc"
    username = os.environ.get('omni_username')
    password = os.environ.get('omni_password')

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)  # Opens the Web Application
        cls.driver.maximize_window()  # Maximize the window
        cls.driver.implicitly_wait(100)

    def test_aa_login(self):
        lp = Test_Login_page(self.driver)
        lp.enter_user_name(self.username)  # Enters the username
        self.driver.implicitly_wait(10)
        lp.enter_password(self.password)  # Enters the password
        lp = Test_Login_page(self.driver)
        self.driver.implicitly_wait(10)
        lp.click_submit_button()  # Clicks submit button

    def test_ab_upload_hanasaku_test_0(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_1_hanasaku_test_0()  # Validates the Actual with Expected Key values

    def test_ac_upload_hanasaku_test_1(self):
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_2_hanasaku_test_1()  # Validates the Actual with Expected Key values

    def test_ad_upload_hanasaku_test_2(self):
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_3_hanasaku_test_2()  # Validates the Actual with Expected Key values

    def test_ae_upload_hanasaku_test_3(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_4_hanasaku_test_3()  # Validates the Actual with Expected Key values

    def test_af_upload_hanasaku_test_4(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_5_hanasaku_test_4()  # Validates the Actual with Expected Key values

    def test_ag_upload_hanasaku_test_8(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_6_hanasaku_test_8()  # Validates the Actual with Expected

    def test_ah_upload_himawari_01_2(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_7_himawari_01_2()  # Validates the Actual with Expected Key values

    def test_ai_upload_himawari_01_3(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_8_himawari_01_3()  # Validates the Actual with Expected Key values

    def test_aj_upload_himawari_03_0(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_9_himawari_03_0()  # Validates the Actual with Expected Key values

    def test_ak_upload_himawari_05_0(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_10_himawari_05_0()  # Validates the Actual with Expected Key values

    def test_al_upload_himawari_05_1(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_11_himawari_05_1()  # Validates the Actual with Expected Key values

    def test_am_upload_himawari_07_1(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_12_himawari_07_1()  # Validates the Actual with Expected Key values

    def test_an_upload_himawari_07_3(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_13_himawari_07_3()  # Validates the Actual with Expected Key values

    def test_ao_upload_DL_HC_High(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_14_DL_HC_High()  # Validates the Actual with Expected Key values

    def test_ap_upload_DL_HC_Left_1(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_15_DL_HC_Left_1()  # Validates the Actual with Expected Key values

    def test_aq_upload_HC_HCDate_2(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_16_HC_HCDate_2()  # Validates the Actual with Expected Key values

    def test_ar_upload_HC_HCDate_3(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_17_HC_HCDate_3()  # Validates the Actual with Expected Key values

    def test_as_upload_HC_HCDate_4(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_18_HC_HCDate_4()  # Validates the Actual with Expected Key values

    def test_at_upload_Feb_18_Medical_Exam_1_1(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_19_Feb_18_Medical_Exam_1_1()  # Validates the Actual with Expected Key values

    def test_au_upload_Feb_18_Medical_Exam_1_2(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_20_Feb_18_Medical_Exam_1_2()  # Validates the Actual with Expected Key values

    def test_av_upload_Feb_18_Medical_Exam_2_0(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_21_Feb_18_Medical_Exam_2_0()  # Validates the Actual with Expected Key values

    def test_aw_upload_Feb_18_Medical_Exam_2_1(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_22_Feb_18_Medical_Exam_2_1()  # Validates the Actual with Expected Key values

    def test_ax_upload_Feb_18_Medical_Exam_3_0(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_23_Feb_18_Medical_Exam_3_0()  # Validates the Actual with Expected Key values

    def test_ay_upload_Feb_18_Medical_Exam_3_1(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_24_Feb_18_Medical_Exam_3_1()  # Validates the Actual with Expected Key values

    def test_az_upload_Feb_18_Medical_Exam_6_1(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_25_Feb_18_Medical_Exam_6_1()  # Validates the Actual with Expected Key values

    def test_ba_upload_Feb_18_Medical_Exam_7_1(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_26_Feb_18_Medical_Exam_7_1()  # Validates the Actual with Expected Key values

    def test_bb_upload_Feb_18_Medical_Exam_7_2(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_27_Feb_18_Medical_Exam_7_2()  # Validates the Actual with Expected Key values

    def test_bc_upload_Feb_18_Medical_Exam_7_3(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_28_Feb_18_Medical_Exam_7_3()  # Validates the Actual with Expected Key values

    def test_bd_upload_accenture_test_4_0(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_29_acc_test_4()  # Validates the Actual with Expected Key values

    def test_be_upload_accenture_test_6_0(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_30_acc_test_6()  # Validates the Actual with Expected Key values

    def test_bf_upload_accenture_test_9_0(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_31_acc_test_9()  # Validates the Actual with Expected Key values

    def test_bg_upload_accenture_test_25_0(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_32_acc_test_25()  # Validates the Actual with Expected Key values

    def test_bh_upload_Feb_18_Medical_Exam_11_0(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_33_Feb_18_Medical_Exam_11_0()  # Validates the Actual with Expected Key values

    def test_bi_upload_HC_1_pdf(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_34_HC_1_pdf()  # Validates the Actual with Expected Key values

    def test_bj_upload_HC_2_pdf(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_35_HC_2_pdf()  # Validates the Actual with Expected Key values

    def test_bk_upload_HC_8_pdf(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_36_HC_8_pdf()  # Validates the Actual with Expected Key values

    def test_bl_upload_HC_9_pdf(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_37_HC_9_pdf()  # Validates the Actual with Expected Key values

    def test_bm_upload_HC_10_pdf(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_38_HC_10_pdf()  # Validates the Actual with Expected Key values

    def test_bn_upload_CA_1(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_39_ca_1()  # Validates the Actual with Expected Key values

    def test_bo_upload_CA_2(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_40_ca_2()  # Validates the Actual with Expected Key values

    def test_bp_upload_CA_3(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_41_ca_3()  # Validates the Actual with Expected Key values

    def test_bq_upload_accenture_test_mobile_9_0(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_42_accenture_test_mobile_9_0()  # Validates the Actual with Expected Key values

    def test_br_upload_accenture_test_mobile_21_0(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_43_accenture_test_mobile_21_0()  # Validates the Actual with Expected Key values

    def test_bs_upload_accenture_test_mobile_25_0(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_44_accenture_test_mobile_25_0()  # Validates the Actual with Expected Key values

    def test_bt_upload_accenture_test_mobile_4_0(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_45_accenture_test_mobile_4_0()  # Validates the Actual with Expected Key values

    def test_bu_upload_NN_8(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_46_NN_8()  # Validates the Actual with Expected Key values

    def test_bv_upload_accenture_test_mobile_6_0(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_47_accenture_test_mobile_6_0()  # Validates the Actual with Expected Key values

    def test_bw_upload_NN_11(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_48_NN_11()  # Validates the Actual with Expected Key values

    def test_bx_upload_NN_12(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_49_NN_12()  # Validates the Actual with Expected Key values

    def test_by_upload_english_demo(self):
        multiple_form = Test_multiple_form_upload(self.driver)
        multiple_form.click_a_groups_tab()  # Clicks on Groups tab
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.form_50_english_demo()  # Validates the Actual with Expected Key values

    def test_by_Results_info(self):
        upload_individual_form = Test_individual_form_upload(self.driver)
        upload_individual_form.total_key_value_data()  # Gets the Key value count
