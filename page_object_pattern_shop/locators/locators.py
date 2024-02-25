from selenium.webdriver.common.by import By


class BillingAddressLocators:

    reg_email_input = ("id", "reg_email")
    reg_password_input = ("id", "reg_password")
    register_input = ("name", "register")
    addresses_link = (By.LINK_TEXT, "Addresses")
    edit_link = (By.LINK_TEXT, "Edit")
    billing_first_name_input = ("id", "billing_first_name")
    billing_last_name_input = ("id", "billing_last_name")
    billing_country_select = ("id", "billing_country")
    billing_address_1_input = ("id", "billing_address_1")
    billing_postcode_input = ("id", "billing_postcode")
    billing_city_input = ("id", "billing_city")
    billing_phone_input = ("id", "billing_phone")
    save_address_button = ("name", "save_address")
    msg_div = ("xpath", "//*[@id='page-7']/div/section/div/div/div/div[2]/div")


class MyAccountLocators:
    username_input = ("id", "username")
    password_input = ("id", "password")
    login_button = ("name", "login")

    reg_email_input = ("id", "reg_email")
    reg_password_input = ("id", "reg_password")
    register_button = ("name", "register")

    msg_error_div = ("xpath", "//*[@id='page-7']/div/section/div/div/div[1]/ul/li")
    logout_link = (By.LINK_TEXT, "Logout")

