from selenium.webdriver.common.by import By
from behave import given, when, then


USERNAME_FIELD = (By.CSS_SELECTOR, '#email-2')
PASSWORD_FIELD = (By.CSS_SELECTOR, '#field')
LOGIN_BUTTON = (By.CSS_SELECTOR, "[wized='loginButton']")


@when('Log in to the page')
def click_cart(context):
    context.app.login_page.profile_log_in()