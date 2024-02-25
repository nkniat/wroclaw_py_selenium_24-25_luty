class SearchHotelPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_hotel_span_xpath = "//span[text()='Search by Hotel or City Name']"
        self.search_hotel_input_xpath = "//*[@id='select2-drop']/div/input"
        self.search_hotel_match_xpath = "//*[@id='select2-drop']/ul/li/ul/li/div"
        self.checkin_input_name = "checkin"
        self.checkout_input_name = "checkout"
        self.travellers_input_name = "travellers"
        self.adults_input_name = "adults"
        self.child_input_name = "child"
        self.search_button_xpath = "//*[@id='hotels']/form/div[5]/button"

    def set_city(self, city):
        self.driver.find_element("xpath", self.search_hotel_span_xpath).click()
        self.driver.find_element("xpath", self.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element("xpath", self.search_hotel_match_xpath).click()

    def set_date_range(self, check_in, check_out):
        self.driver.find_element("name", self.checkin_input_name).send_keys(check_in)
        self.driver.find_element("name", self.checkout_input_name).send_keys(check_out)

    def set_travellers(self, adults, kids):
        self.driver.find_element("name", self.travellers_input_name).click()
        self.driver.find_element("name", self.adults_input_name).clear()
        self.driver.find_element("name", self.adults_input_name).send_keys("1")
        self.driver.find_element("name", self.child_input_name).clear()
        self.driver.find_element("name", self.child_input_name).send_keys("2")

    def perform_search(self):
        self.driver.find_element("xpath", self.search_button_xpath).click()
