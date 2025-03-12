from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BaseElement:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    def wait_for_element(self, conditions):
        try:
            return WebDriverWait(self.driver, 10).until(conditions(self.locator))
        except TimeoutError:
            raise TimeoutError(f"Timeout, waiting for element: {self.locator}")

    def is_displayed(self):
        try:
            self.wait_for_element(EC.visibility_of_element_located)
            return True
        except TimeoutError:
            return False

    def send_keys(self, text):
        try:
            self.wait_for_element(EC.element_to_be_clickable)
            element = self.driver.find_element(*self.locator)
            element.clear()
            element.send_keys(text)
        except TimeoutError:
            raise TimeoutError(f"Unable to locate or interact with the element: {self.locator}.")

    def click(self):
        try:
            self.wait_for_element(EC.element_to_be_clickable)
            element = self.driver.find_element(*self.locator)
            element.click()
        except TimeoutError:
            raise TimeoutError(f"Unable to locate or interact with the element to be click: {self.locator}.")

    def dropdown_select(self, text):
        try:
            element = self.wait_for_element(EC.presence_of_element_located)
            select = Select(element)
            select.select_by_visible_text(text)
        except TimeoutError:
            raise TimeoutError(f"Unable to locate or interact with the element to be selected: {self.locator}.")

    def hover_over(self):
        try:
            element = self.wait_for_element(EC.visibility_of_element_located)
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
        except TimeoutError:
            raise TimeoutError("Element not found for hover operation")

    def get_text(self):
        try:
            element = self.wait_for_element(EC.visibility_of_element_located)
            return element.text
        except TimeoutError:
            raise TimeoutError(f"Element not found to get text: {self.locator}")

    def get_attribute(self, attribute):
        try:
            element = self.wait_for_element(EC.visibility_of_element_located)
            return element.get_attribute(attribute)
        except TimeoutError:
            raise TimeoutError(f"Element not found to get attribute selection: {self.locator}")