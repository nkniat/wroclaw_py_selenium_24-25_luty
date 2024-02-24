from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# implicity wait - oczekiwanie na pojawienie sie KAŻDEGO elementu na stronie
driver.implicitly_wait(10)

driver.get("https://www.w3schools.com/")
driver.maximize_window()

# zaakceptuj ciasteczka
accept = driver.find_element("id", "accept-choices")
accept.click()

# wybranie menu "Tutorials"
menu = driver.find_element("id", "navbtn_tutorials")
# klikanie w element
menu.click()

# wybranie tutoriala "HTML"
tutorial = driver.find_element("xpath", "//a[@title='HTML Tutorial']")
tutorial.click()

# wybór z lewego menu "Input types"
inputTypes = driver.find_element("xpath", "//*[@id='leftmenuinnerinner']/a[43]")
inputTypes.click()

time.sleep(200)
driver.quit()
