from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BaseElement:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None

    def wait_for_element(self, conditions):
        try:
            return WebDriverWait(self.driver, 10).until(conditions(self.locator))
        except:
            raise Exception(f"Timeout, waiting for element: {self.locator}")

    def locate_element(self):
        self.web_element = self.wait_for_element(EC.visibility_of_element_located)

    def is_displayed(self):
        self.locate_element()
        return self.web_element.is_displayed()

    def input_text(self, text):
        try:
            self.web_element = self.wait_for_element(EC.element_to_be_clickable)
            self.web_element.clear()
            self.web_element.send_keys(text)
        except:
            raise Exception(f"Unable to locate or interact with the element: {self.locator}.")

    def button_click(self):
        try:
            self.web_element = self.wait_for_element(EC.element_to_be_clickable)
            self.web_element.click()
        except:
            raise Exception(f"Unable to locate or interact with the element to be click: {self.locator}.")

    def dropdown_select(self, text):
        try:
            self.web_element = self.wait_for_element(EC.presence_of_element_located)
            select = Select(self.web_element)
            select.select_by_visible_text(text)
        except:
            raise Exception(f"Unable to locate or interact with the element to be selected: {self.locator}.")

    def hover_over(self):
        try:
            self.web_element = self.wait_for_element(EC.visibility_of_element_located)
            action = ActionChains(self.driver)
            action.move_to_element(self.web_element).perform()
        except:
            raise Exception("Element not found for hover operation")

