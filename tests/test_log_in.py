import pytest

from locators.locators import LocatorsHomePage
from pages.home_page import HomePage
from pages.login_page import LogInPage


@pytest.mark.usefixtures("setup")
class TestLogIn:

    def test_login_passed(self):
        login = LogInPage(self.driver)
        login.open_page()
        login.click_entrar()
        login.enter_email("email_here")
        login.click_proximo()
        login.enter_password("password_here")
        login.click_login()

        home = HomePage(self.driver)
        home.validate_home()
