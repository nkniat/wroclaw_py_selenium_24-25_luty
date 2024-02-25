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
