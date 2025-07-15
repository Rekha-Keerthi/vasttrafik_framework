from selenium.webdriver.common.by import By

from utilities.baseclass import BaseClass


class LoginPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.logga_in = (By.CSS_SELECTOR, "#secondary-menu-desktop-login-menu-button")
        self.private_login = (By.LINK_TEXT, "Logga in: privatkund")
        self.business_loogin = (By.LINK_TEXT, "Logga in: företagskund")
        self.email_post = (By.CSS_SELECTOR, "#nav-username")
        self.email_id = (By.CSS_SELECTOR, "#usernameField")
        self.user_password = (By.CSS_SELECTOR, "#password")

    def user_login(self):

        self.driver.find_element(*self.logga_in).click()
        self.driver.find_element(*self.private_login).click()
        self.driver.find_element(*self.email_post).click()
        self.driver.find_element(*self.email_id).send_keys("rekha.nkk5@gmail.com")
        self.driver.find_element(*self.user_password).send_keys("rekhaewwer")
