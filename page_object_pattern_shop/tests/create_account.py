import random
from page_object_pattern_shop.pages.my_account_page import MyAccountPage
import pytest

@pytest.mark.usefixtures("setup")
class TestCreateAccount:

    def test_create_account_pass(self):
        mail = str(random.randint(0, 10000)) + "student@merito.com"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(mail, "MojeFajneHaslo")

        assert my_account_page.is_logout_displayed()


    def test_create_account_fail(self):

        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account("student@merito.com", "MojeFajneHaslo")

        msg = "Error: An account is already registered with your email address. Please log in."

        assert msg in my_account_page.get_error_msg()
