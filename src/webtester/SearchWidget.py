import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from webtester.BaseElement import BaseElement

class SearchWidget(BaseElement):

    def __init__(self, driver) -> None:
        super().__init__(driver, "q", By.NAME)
    
    def enter(self, data) -> None:
        self.web_element.clear()
        for character in data:
            self.web_element.send_keys(character)
            # Intentional delay to emulate human input
            time.sleep(0.03)

    def search(self, data) -> None:
        self.enter(data)
        self.enter(Keys.ENTER)