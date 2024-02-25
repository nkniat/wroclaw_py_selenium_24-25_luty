from page_object_pattern_shop.locators import locators


class MyAccountPage:

    def __init__(self, driver):
        self.driver = driver

        self.username_input = locators.MyAccountLocators.username_input
        self.password_input = locators.MyAccountLocators.password_input
        self.login_button = locators.MyAccountLocators.login_button

        self.reg_email_input = locators.MyAccountLocators.reg_email_input
        self.reg_password_input = locators.MyAccountLocators.reg_password_input
        self.register_button = locators.MyAccountLocators.register_button

        self.msg_error_div = locators.MyAccountLocators.msg_error_div
        self.logout_link = locators.MyAccountLocators.logout_link

    def open_page(self):
        self.driver.get("http://seleniumdemo.com/?page_id=7")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def create_account(self, email, password):
        self.driver.find_element(*self.reg_email_input).send_keys(email)
        self.driver.find_element(*self.reg_password_input).send_keys(password)
        self.driver.find_element(*self.register_button).click()

    def is_logout_displayed(self):
        return self.driver.find_element(*self.logout_link).is_displayed()

    def get_error_msg(self):
        return self.driver.find_element(*self.msg_error_div).text
