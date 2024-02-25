import random
from page_object_pattern_shop.pages.my_account_page import MyAccountPage
import pytest

@pytest.mark.usefixtures("setup")
class TestCreateAccount:

    def test_login_pass(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.login("student@merito.com", "MojeFajneHaslo")

        assert my_account_page.is_logout_displayed()

    def test_login_fail(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.login("student@merito.pl", "MojeFajneHaslo12")

        msg = "ERROR: Incorrect username or password."

        assert msg in my_account_page.get_error_msg()
