from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


from pages.base_page import Page


class OffPlanPage(Page):
    FIRST_PRODUCT = (By.CSS_SELECTOR, ".cards-properties")

    def wait_element_clickable_click(self, FIRST_PRODUCT):
        self.wait.until(
            EC.element_to_be_clickable(FIRST_PRODUCT),
            message=f'Element by {FIRST_PRODUCT} is not clickable'
        ).click()