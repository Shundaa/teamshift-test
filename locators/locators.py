from selenium.webdriver.common.by import By


class LocatorsLoginPage:
    # LoginPage elements
    email_id = (By.ID, "login-form__login")
    password_id = (By.ID, "login-form__password")
    entrar_btn_xpath = (By.XPATH, "(//*[contains(text(),'Entrar')])[1]")
    proximo_btn_xpath = (By.XPATH, "//*[contains(text(),'Próximo')]")
    login_btn_xpath = (By.XPATH, "//*[contains(text(),'Login')]")

class LocatorsHomePage:
    # LoginPage elements
    home_button_xpath = (By.XPATH, "//*[contains(text(),'Home')]")
