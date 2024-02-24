from selenium import webdriver
import time

# inicjalizacja przeglądarki Chrome
driver = webdriver.Chrome()

# otwarcie okna przeglądarki z konkretnym adresem
driver.get("https://www.google.com")

# zatrzymanie skryptu na x sekund
time.sleep(10)

# zakończenie pracy przeglądarki
driver.quit()
