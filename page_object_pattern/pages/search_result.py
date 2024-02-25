import logging
from page_object_pattern.locators.locators import SearchResulLocators


class SearchResultPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.hotel_names_xpath = SearchResulLocators.hotel_names_xpath

    def get_hotel_names(self):
        hotels = self.driver.find_elements("xpath", self.hotel_names_xpath)
        hotels_name = [hotel.get_attribute("textContent") for hotel in hotels]

        self.logger.info("Hotels are:")
        for hotel in hotels_name:
            self.logger.info(hotel)

        return hotels_name

    # zadanie domowe - dopisać analogiczną metodę do pobierania cen
    # get_hotel_prices(self)
    # do konstruktora trzeba dodać atrybut, którym pobierzemy ceny