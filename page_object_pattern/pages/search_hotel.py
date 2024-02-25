import logging
from page_object_pattern.locators.locators import SearchHotelLocators


class SearchHotelPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.search_hotel_span_xpath = SearchHotelLocators.search_hotel_span_xpath
        self.search_hotel_input_xpath = SearchHotelLocators.search_hotel_input_xpath
        self.search_hotel_match_xpath = SearchHotelLocators.search_hotel_match_xpath
        self.checkin_input_name = SearchHotelLocators.checkin_input_name
        self.checkout_input_name = SearchHotelLocators.checkout_input_name
        self.travellers_input_name = SearchHotelLocators.travellers_input_name
        self.adults_input_name = SearchHotelLocators.adults_input_name
        self.child_input_name = SearchHotelLocators.child_input_name
        self.search_button_xpath = SearchHotelLocators.search_button_xpath

    def set_city(self, city):
        self.logger.info("Setting city {}".format(city))
        self.driver.find_element("xpath", self.search_hotel_span_xpath).click()
        self.driver.find_element("xpath", self.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element("xpath", self.search_hotel_match_xpath).click()

    def set_date_range(self, check_in, check_out):
        self.logger.info("Setting checkin {checkin} and checkout {checkout}".format(checkin=check_in, checkout=check_out))
        self.driver.find_element("name", self.checkin_input_name).send_keys(check_in)
        self.driver.find_element("name", self.checkout_input_name).send_keys(check_out)

    def set_travellers(self, adults, kids):
        self.logger.info("Setting travellers: adulds: {adults}, kids: {kids}".format(adults=adults, kids=kids))
        self.driver.find_element("name", self.travellers_input_name).click()
        self.driver.find_element("name", self.adults_input_name).clear()
        self.driver.find_element("name", self.adults_input_name).send_keys("1")
        self.driver.find_element("name", self.child_input_name).clear()
        self.driver.find_element("name", self.child_input_name).send_keys("2")

    def perform_search(self):
        self.logger.info("Performing search... ")
        self.driver.find_element("xpath", self.search_button_xpath).click()
