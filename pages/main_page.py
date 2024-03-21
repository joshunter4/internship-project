from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    OFF_PLAN_ICON = (By.CSS_SELECTOR, "address a[href='/off-plan']")

    def open_main(self):
        self.open('https://soft.reelly.io/')

    def click_off_plan_icon(self):
        self.wait_element_clickable_click(*self.OFF_PLAN_ICON)