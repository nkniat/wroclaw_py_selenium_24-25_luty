from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.pl")
driver.maximize_window()

# zaakceptuj zgody
accept = driver.find_element("id", "L2AGLb")
accept.click()

# znajdz pole wyszukiwania
search = driver.find_element("name", "q")

# wprowadzenie hasła
search.send_keys('Kto ma dzisiaj imieniny')

# wcisniecie 'Enter'
search.send_keys(Keys.RETURN)

time.sleep(200)
driver.quit()
