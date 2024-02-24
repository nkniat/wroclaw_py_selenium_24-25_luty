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

# wybór z lewego menu "Tag list"
tagList = driver.find_element("xpath", "//*[@id='leftmenuinnerinner']/a[67]")
tagList.click()

# wybór z menu "Input"
inputTag = driver.find_element("xpath", "//*[@id='leftmenuinnerinner']/div/a[59]")
inputTag.click()

# wybór z menu "disable"
disable = driver.find_element("xpath", "//*[@id='main']/table[2]/tbody/tr[8]/td[1]/a")
disable.click()

# klikniecie 'try it yourself'
tryIt = driver.find_element("xpath", "//*[@id='main']/div[2]/a")
tryIt.click()

print("Aktualne okno:", driver.title)

# obecna zakładka
currentWindows = driver.current_window_handle

# wszystkio okna
windowsNames = driver.window_handles

for window in windowsNames:
    if window != currentWindows:
        driver.switch_to.window(window)

print("Aktualne okno - po przełączeniu:", driver.title)

# przełączenie się do iframe - czyli strony w środku strony
driver.switch_to.frame(driver.find_element("id", "iframeResult"))

# wprowadź imie
name = driver.find_element("id", "fname")
name.send_keys("Natalia")

time.sleep(200)
driver.quit()
