import time
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

# Create your views here.

main_path = os.path.dirname(os.path.abspath(__file__))
chrome_path = os.path.join(main_path, "chromedriver")

def get_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {"profile.default_content_settings.cookies": 2})
    chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})
    chrome_options.add_experimental_option("prefs", {"profile.block_third_party_cookies": True})
    chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(chrome_path, chrome_options=chrome_options)
    return driver

@api_view(['POST'])
def add_patient(request):
    driver = get_driver()
    driver.get("https://app.drchrono.com/accounts/login/")
    username = driver.find_element_by_xpath("//input[@id='username']")
    username.send_keys("advichrono")
    password = driver.find_element_by_xpath("//input[@id='password']")
    password.send_keys("Advinowapis1!")
    login = driver.find_element_by_xpath("//input[@id='login']")
    ActionChains(driver).click(login).perform()
    time.sleep(5)
    driver.get("https://advichrono.drchrono.com/patients/new/")
    title = driver.find_element_by_xpath("//input[@id='id_title']")
    title.send_keys("test_account_1")
    first_name = driver.find_element_by_xpath("//input[@id='id_first_name']")
    first_name.send_keys("test_account_1")
    nick_name = driver.find_element_by_xpath("//input[@id='id_nick_name']")
    nick_name.send_keys("test_account_1")
    middle_name = driver.find_element_by_xpath("//input[@id='id_middle_name']")
    middle_name.send_keys("test_account_1")
    last_name = driver.find_element_by_xpath("//input[@id='id_last_name']")
    last_name.send_keys("test_account_1")
    prev_name = driver.find_element_by_xpath("//input[@id='id_previous_name']")
    prev_name.send_keys("test_account_1")
    suffix = driver.find_element_by_xpath("//input[@id='id_suffix']")
    suffix.send_keys("test_account_1")
    home_phone = driver.find_element_by_xpath("//input[@id='id_home_phone']")
    home_phone.send_keys("+123456789")
    cell_phone = driver.find_element_by_xpath("//input[@id='id_cell_phone']")
    cell_phone.send_keys("+123456789")
    office_phone = driver.find_element_by_xpath("//input[@id='id_office_phone']")
    office_phone.send_keys("+123456789")
    office_ext = driver.find_element_by_xpath("//input[@id='id_office_phone_extension']")
    office_ext.send_keys("+1234567")
    email = driver.find_element_by_xpath("//input[@id='id_email']")
    email.send_keys("test_account_1@gmail.com")
    allow_email = driver.find_element_by_xpath("//input[@id='id_allow_duplicate_email']")
    ActionChains(driver).click(allow_email).perform()
    alter_email = driver.find_element_by_xpath("//input[@id='id_alternate_email']")
    alter_email.send_keys("alter_test_account_1@gmail.com")
    prefer_commu = Select(driver.find_element_by_xpath("//select[@id='id_preferred_confidential_communication_method']"))
    prefer_commu.select_by_value("Work")
    decline_summary = driver.find_element_by_xpath("//input[@id='id_decline_clinical_summary']")
    ActionChains(driver).click(decline_summary).perform()
    medication_hist_consent = Select(driver.find_element_by_xpath("//select[@id='id_medication_history_consent']"))
    medication_hist_consent.select_by_value("Y")
    payment_profile = Select(driver.find_element_by_xpath("//select[@id='id_patient_payment_profile']"))
    payment_profile.select_by_value("Cash")
    patient_copay = driver.find_element_by_xpath("//input[@id='id_copay']")
    patient_copay.send_keys("100")
    follow_up_date = driver.find_element_by_xpath("//input[@id='id_date_of_next_follow_up']")
    follow_up_date.send_keys("01/22/2020")
    follow_up_reason = driver.find_element_by_xpath("//input[@id='id_follow_up_appointment_reason']")
    follow_up_reason.send_keys("test_account_1")
    last_appoint = driver.find_element_by_xpath("//input[@id='id_date_of_last_appointment']")
    last_appoint.send_keys("01/22/2020")

    save = driver.find_element_by_xpath("//input[@value='Save']")
    ActionChains(driver).click(save).perform()
    time.sleep(5)
    try:
        search = driver.find_element_by_xpath("//input[@id='id_patient_search_name']")
        search.send_keys("test_account_1")
        context = {
            'status': "success"
        }
        return Response(context, status.HTTP_200_OK)
    except:
        context = {
            'status': "fail"
        }
        return Response(context, status.HTTP_400_BAD_REQUEST)





