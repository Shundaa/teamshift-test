import logging

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import LocatorsHomePage


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def validate_home(self):
        self.logger.info("Validating Home")
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(LocatorsHomePage.home_button_xpath))
        assert "HOME" in self.driver.find_element(*LocatorsHomePage.home_button_xpath).text
