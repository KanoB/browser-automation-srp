from webtester.BasePage import BasePage
from webtester.SearchWidget import SearchWidget
from webtester.SearchSuggestions import SearchSuggestions
from webtester.NavigationBar import NavigationBar
from webtester.ResultStat import ResultStat

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
    
class GoogleResultPage(GoogleMainPage):

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self._navbar = None
        self._stat = None

    def getNavigationBar(self):
        self._navbar = NavigationBar(self.driver)
        return self._navbar
    
    def getResultStat(self):
        self._stat = ResultStat(self.driver)
        return self._stat