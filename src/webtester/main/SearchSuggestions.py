from selenium.webdriver.common.by import By

from webtester.common.Locator import Locator
from webtester.common.BaseElement import BaseElement

class SearchSuggestions(BaseElement):

    def __init__(self, driver) -> None:
        locator = Locator(by=By.CSS_SELECTOR, value="li.sbct")
        super().__init__(driver, locator)

    def find(self):
        elements = self.wait.until(lambda x: len(self.driver.find_elements(*self.locator)) > 5)
        self.web_element = self.driver.find_elements(*self.locator)
        # return super().find()
        return None
    
    def clickSuggestionByIndex(self, index):
        self.getSuggestions()[index-1].click()

    def getSuggestions(self):
        return [x for x in self.web_element if x.text != ''][1:] # First one is the searched keyword(s)

    def text(self):
        return [x.text for x in self.getSuggestions()]

