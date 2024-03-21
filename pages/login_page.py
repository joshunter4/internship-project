from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


from pages.base_page import Page


class LoginPage(Page):
    USERNAME_FIELD = (By.CSS_SELECTOR, '#email-2')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#field')
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[wized='loginButton']")

    def profile_log_in(self):
        self.input_text('jahztps138@yahoo.com', *self.USERNAME_FIELD)
        self.input_text('11111111', *self.PASSWORD_FIELD)
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON),
        ).click()