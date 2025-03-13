
from conftest import driver
from pages.base_element.Base_Element import BaseElement
from selenium.webdriver.common.by import By

class FormFieldsPage:
    def __init__(self, driver):
        self.driver = driver
        self.start_timer_btn = BaseElement(driver, (By.ID, "start"))
        self.countdown_field = BaseElement(driver, (By.ID, "delay"))

    def click_start_timer_liftoff_btn(self):
        self.start_timer_btn.click()

    def wait_for_liftoff(self):
        return self.countdown_field.wait_for_text("Liftoff!")
