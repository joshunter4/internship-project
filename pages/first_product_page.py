from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page


class FirstProductPage(Page):
    VERIFY_ELEMENTS = (By.CSS_SELECTOR, "[class*='tabs-menu-project']")

    def wait_element_visible(self, VERIFY_ELEMENTS):
        self.wait.until(
            EC.visibility_of_element_located(VERIFY_ELEMENTS),
            message=f'Element by {VERIFY_ELEMENTS} is not visible'
        )

    def wait_element_clickable(self, VERIFY_ELEMENTS):
        self.wait.until(
            EC.element_to_be_clickable(VERIFY_ELEMENTS),
            message=f'Element by {VERIFY_ELEMENTS} is not clickable'
        )