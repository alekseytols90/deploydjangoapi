from django.shortcuts import render
import time
from datetime import datetime, timedelta
import numpy as np
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Create your views here.

main_path = os.path.dirname(os.path.abspath(__file__))
chrome_path = os.path.join(main_path, "chromedriver")

def get_driver():
    driver = webdriver.Chrome(chrome_path)
    return driver

def add_patient():
    driver = get_driver()
    driver.get("https://app.drchrono.com/accounts/login/")
    username = driver.find_element_by_xpath("//input[@id='username']")
    username.send_keys("advichrono")
    password = driver.find_element_by_xpath("//input[@id='password']")
    password.send_keys("Advinowapis1!")
    login = driver.find_element_by_xpath("//input[@id='login']")
    ActionChains(driver).click(login).perform()
    time.sleep(2)
    patient_tab = driver.find_element_by_xpath("//div[@id='toolbar']/div[1]/div[1]/div[1]/ul[1]/li[3]/a")
    # patient_tab = toolbar.find_element_by_xpath(".//")
    ActionChains(driver).click(patient_tab).perform()
    time.sleep(2)
    new_patient = driver.find_element_by_xpath("//div[@id='content']/div[4]/a[1]")
    ActionChains(driver).click(new_patient).perform()
    time.sleep(12)
    driver.switch_to.window(driver.window_handles[1])

    title = driver.find_element_by_xpath("//input[@id='id_title']")
    title.send_keys("test1")
    first_name = driver.find_element_by_xpath("//input[@id='id_first_name']")
    first_name.send_keys("test1")
    nick_name = driver.find_element_by_xpath("//input[@id='id_nick_name']")
    nick_name.send_keys("test1")
    middle_name = driver.find_element_by_xpath("//input[@id='id_middle_name']")
    middle_name.send_keys("test1")
    last_name = driver.find_element_by_xpath("//input[@id='id_last_name']")
    last_name.send_keys("test1")
    prev_name = driver.find_element_by_xpath("//input[@id='id_previous_name']")
    prev_name.send_keys("test1")
    suffix = driver.find_element_by_xpath("//input[@id='id_suffix']")
    suffix.send_keys("test1")
    home_phone = driver.find_element_by_xpath("//input[@id='id_home_phone']")
    home_phone.send_keys("+123456789")
    cell_phone = driver.find_element_by_xpath("//input[@id='id_cell_phone']")
    cell_phone.send_keys("+123456789")
    office_phone = driver.find_element_by_xpath("//input[@id='id_office_phone']")
    office_phone.send_keys("+123456789")
    office_ext = driver.find_element_by_xpath("//input[@id='id_office_phone_extension']")
    office_ext.send_keys("+1234567")
    email = driver.find_element_by_xpath("//input[@id='id_email']")
    email.send_keys("test1@gmail.com")
    alter_email = driver.find_element_by_xpath("//input[@id='id_alternate_email']")
    alter_email.send_keys("alter_test1@gmail.com")
    prefer_commu = Select(
        driver.find_element_by_xpath("//select[@id='id_preferred_confidential_communication_method']"))
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
    follow_up_reason.send_keys("test1")
    last_appoint = driver.find_element_by_xpath("//input[@id='id_date_of_last_appointment']")
    last_appoint.send_keys("01/22/2020")

    save = driver.find_element_by_xpath("//input[@value='Save']")
    ActionChains(driver).click(save).perform()
    time.sleep(7)
    try:
        search = driver.find_element_by_xpath("//input[@id='id_patient_search_name']")
        search.send_keys("test_account_1")
        context = {
            'status': "success"
        }
    except:
        context = {
            'status': "fail"
        }
    return Response(context)


add_patient()



