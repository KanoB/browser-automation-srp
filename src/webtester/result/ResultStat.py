from selenium.webdriver.common.by import By

from webtester.common.Locator import Locator
from webtester.common.BaseElement import BaseElement

class ResultStat(BaseElement):

    def __init__(self, driver) -> None:
        locator = Locator(by=By.ID, value="result-stats")
        super().__init__(driver, locator)
