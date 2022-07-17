import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from webtester.common.Locator import Locator
from webtester.common.BaseElement import BaseElement

class SearchWidget(BaseElement):

    def __init__(self, driver) -> None:
        locator = Locator(by=By.NAME, value="q")
        super().__init__(driver, locator)
    
    def enter(self, data) -> None:
        self.web_element.clear()
        for character in data:
            self.web_element.send_keys(character)
            # Intentional delay to emulate human input
            time.sleep(0.03)

    def search(self, data) -> None:
        self.enter(data)
        self.web_element.send_keys(Keys.ENTER)