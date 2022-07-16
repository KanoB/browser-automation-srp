from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseElement():
    def __init__(self, driver, locator) -> None:
        self.driver = driver
        self.locator = locator

        self.wait = WebDriverWait(driver, 10)
        self.web_element = None
        self.find()

    def find(self):
        element = self.wait.until(EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def click(self):
        self.wait.until(EC.element_to_be_clickable(self.locator))
        self.web_element.click()
        return None

    @property
    def text(self):
        text = self.web_element.text
        return text

    # @text.setter
    # def text(self, value):
    #     text = self.web_element.enter_keys(value)