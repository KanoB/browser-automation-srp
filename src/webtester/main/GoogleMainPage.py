from webtester.common.BasePage import BasePage

from .SearchWidget import SearchWidget
from .SearchSuggestions import SearchSuggestions

class GoogleMainPage(BasePage):
    """Google main search page"""

    url = "https://www.google.com"

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self._search = None
        self._suggestions = None

    def getSearchWidget(self):
        self._search = SearchWidget(self.driver)
        return self._search

    def getSearchSuggestions(self):
        self._suggestions = SearchSuggestions(self.driver)
        return self._suggestions
    