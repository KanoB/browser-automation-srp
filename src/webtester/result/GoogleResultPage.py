from webtester.main.GoogleMainPage import GoogleMainPage

from .NavigationBar import NavigationBar
from .ResultStat import ResultStat

   
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