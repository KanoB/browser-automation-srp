from selenium.webdriver.common.by import By

from webtester.BaseElement import BaseElement

class SearchSuggestions(BaseElement):

    def __init__(self, driver) -> None:
        super().__init__(driver, "li.sbct", By.CSS_SELECTOR)

    def find(self):
        elements = self.wait.until(lambda x: len(self.driver.find_elements(*self.locator)) > 5)
        self.web_element = self.driver.find_elements(*self.locator)
        # return super().find()
        return None
    
    def clickSuggestionByIndex(self, index):
        self.getSuggestions()[index-1].click()

    def getSuggestions(self):
        return [x for x in self.web_element if x.text != '']

    def text(self):
        suggestions = []
        for element in self.web_element:
            suggestions.append(element.text)
        return suggestions
