from selenium.webdriver.common.by import By
from behave import given, when, then


FIRST_PRODUCT = (By.CSS_SELECTOR, ".project-image")


@when('Click on the first product')
def click_first_product(context):
    context.app.off_plan_page.wait_element_clickable_click(FIRST_PRODUCT)