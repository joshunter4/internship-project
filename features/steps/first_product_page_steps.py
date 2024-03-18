from selenium.webdriver.common.by import By
from behave import given, when, then


ARCHITECTURE_ELEMENT = (By.CSS_SELECTOR, '#w-tabs-0-data-w-tab-0')
INTERIOR_ELEMENT = (By.CSS_SELECTOR, '#w-tabs-0-data-w-tab-1')


@then('Verify the two options of visualization are “architecture”, “interior”')
def verify_visual(context):
    context.app.first_product_page.wait_element_visible(ARCHITECTURE_ELEMENT)
    context.app.first_product_page.wait_element_visible(INTERIOR_ELEMENT)


@then('Verify the visualization options are clickable')
def verify_clickable(context):
    context.app.first_product_page.wait_element_clickable(ARCHITECTURE_ELEMENT)
    context.app.first_product_page.wait_element_visible(INTERIOR_ELEMENT)