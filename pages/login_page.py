import logging

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import LocatorsLoginPage


class LogInPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def open_page(self):
        self.logger.info("Opening website")
        self.driver.get("https://teamshift-qa.crossknowledge.com/")

    def enter_email(self, email):
        self.logger.info("Setting Email")
        self.driver.find_element(*LocatorsLoginPage.email_id).clear()
        self.driver.find_element(*LocatorsLoginPage.email_id).send_keys(email)

    def enter_password(self, password):
        self.logger.info("Setting Password")
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(LocatorsLoginPage.password_id))
        self.driver.find_element(*LocatorsLoginPage.password_id).clear()
        self.driver.find_element(*LocatorsLoginPage.password_id).send_keys(password)

    def click_entrar(self):
        self.logger.info("Clicking on button Entrar")
        self.driver.find_element(*LocatorsLoginPage.entrar_btn_xpath).click()

    def click_proximo(self):
        self.logger.info("Clicking on button Proximo")
        self.driver.find_element(*LocatorsLoginPage.proximo_btn_xpath).click()

    def click_login(self):
        self.logger.info("Clicking on button Login")
        self.driver.find_element(*LocatorsLoginPage.login_btn_xpath).click()