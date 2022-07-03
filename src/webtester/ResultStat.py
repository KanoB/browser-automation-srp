from selenium.webdriver.common.by import By

from webtester.BaseElement import BaseElement

class ResultStat(BaseElement):

    def __init__(self, driver) -> None:
        super().__init__(driver, "result-stats", By.ID)
