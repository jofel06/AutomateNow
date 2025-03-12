from lib2to3.pgen2.driver import Driver

from conftest import driver
from pages.base_element.Base_Element import BaseElement
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.homepage_link = BaseElement(driver, (By.CSS_SELECTOR, "a[class='logo logo-left with-image l m px ']"))
        self.javascript_delays_link = BaseElement(driver, (By.LINK_TEXT, "JavaScript Delays"))
        self.form_fields_link = BaseElement(driver, (By.LINK_TEXT, "Form Fields"))
        self.popups_link = BaseElement(driver, (By.LINK_TEXT, "Popups"))

    def click_homepage_icon(self):
        self.homepage_link.click()

    def open_javascript_delays_page(self):
        self.javascript_delays_link.click()

    def open_form_fields_page(self):
        self.form_fields_link.click()

    def open_popups_link_page(self):
        self.popups_link.click()



