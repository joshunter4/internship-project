from selenium.webdriver.common.by import By
from behave import given, when, then


OFF_PLAN_ICON = (By.CSS_SELECTOR, "address a[href='/off-plan']")


@given('Open the main page')
def open_main_page(context):
    context.app.main_page.open_main()


@when('Click on "off plan" at the left side menu')
def off_plan_icon(context):
    context.app.main_page.click_off_plan_icon()