from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import random


def test_update_billing_address():

    mail = str(random.randint(0, 10000)) + "student@merito.com"
    # zadanie domowe: napisać funkcję generująca hasło

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://seleniumdemo.com/?page_id=7")
    # utworzenie nowego konta
    driver.find_element("id", "reg_email").send_keys(mail)
    driver.find_element("id", "reg_password").send_keys("MojeFajneHaslo")
    driver.find_element("name", "register").click()
    # przejście do adresu
    driver.find_element(By.LINK_TEXT, "Addresses").click()
    driver.find_element(By.LINK_TEXT, "Edit").click()
    # wypełnianie formularza
    driver.find_element("id", "billing_first_name").send_keys("Natalia")
    driver.find_element("id", "billing_last_name").send_keys("Burda")
    # obsługa znacznika 'select'
    Select(driver.find_element("id", "billing_country")).select_by_visible_text("Poland")
    driver.find_element("id", "billing_address_1").send_keys("Wrocławska 1")
    driver.find_element("id", "billing_postcode").send_keys("12-345")
    driver.find_element("id", "billing_city").send_keys("Kraków")
    driver.find_element("id", "billing_phone").send_keys("123456789")

    # zapisanie zmian
    driver.find_element("name", "save_address").click()

    msg = "Address changed successfully."

    assert msg in driver.find_element("xpath", "//*[@id='page-7']/div/section/div/div/div/div[2]/div").text

