class SearchResultPage:

    def __init__(self, driver):
        self.driver = driver
        self.hotel_names_xpath = "//h4[contains(@class, 'list_title')]//b"

    def get_hotel_names(self):
        hotels = self.driver.find_elements("xpath", self.hotel_names_xpath)
        hotels_name = [hotel.get_attribute("textContent") for hotel in hotels]
        return hotels_name

    # zadanie domowe - dopisać analogiczną metodę do pobierania cen
    # get_hotel_prices(self)
    # do konstruktora trzeba dodać atrybut, którym pobierzemy ceny