class SearchHotelLocators:
    search_hotel_span_xpath = "//span[text()='Search by Hotel or City Name']"
    search_hotel_input_xpath = "//*[@id='select2-drop']/div/input"
    search_hotel_match_xpath = "//*[@id='select2-drop']/ul/li/ul/li/div"
    checkin_input_name = "checkin"
    checkout_input_name = "checkout"
    travellers_input_name = "travellers"
    adults_input_name = "adults"
    child_input_name = "child"
    search_button_xpath = "//*[@id='hotels']/form/div[5]/button"

class SearchResulLocators:
    hotel_names_xpath = "//h4[contains(@class, 'list_title')]//b"
