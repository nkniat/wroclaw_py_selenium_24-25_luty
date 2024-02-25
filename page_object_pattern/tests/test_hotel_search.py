from selenium import webdriver
import pytest
from page_object_pattern.pages.search_hotel import SearchHotelPage


class TestHotelSearch:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_hotel_search(self, setup):
        self.driver.get("http://www.kurs-selenium.pl/")
        search_hotel_page = SearchHotelPage(self.driver)

        search_hotel_page.set_city("Dubai")
        search_hotel_page.set_date_range("25/02/2024", "28/02/2024")
        search_hotel_page.set_travellers("1", "2")
        search_hotel_page.perform_search()
