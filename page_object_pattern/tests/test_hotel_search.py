from selenium import webdriver
import pytest
from page_object_pattern.pages.search_hotel import SearchHotelPage
from page_object_pattern.pages.search_result import SearchResultPage


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

        result_page = SearchResultPage(self.driver)

        hotel_names = result_page.get_hotel_names()

        assert hotel_names[0] == "Jumeirah Beach Hotel"
        assert hotel_names[1] == "Oasis Beach Tower"
        assert hotel_names[2] == "Rose Rayhaan Rotana"
        assert hotel_names[3] == "Hyatt Regency Perth"

        # zadanie domowe - dopisać asercje dla sprawdzenia cen
        # assert hotel_prices[0] == "0"
