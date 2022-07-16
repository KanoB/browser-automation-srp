from selenium.webdriver.common.by import By

from webtester.common.Locator import Locator
from webtester.common.BaseElement import BaseElement

class NavAll(BaseElement):
    def __init__(self, driver) -> None:
        locator = Locator(by=By.LINK_TEXT, value="Todos")
        super().__init__(driver, locator)

class Images(BaseElement):
    def __init__(self, driver) -> None:
        locator = Locator(by=By.LINK_TEXT, value="Imágenes")
        super().__init__(driver, locator)

class Videos(BaseElement):
    def __init__(self, driver) -> None:
        locator = Locator(by=By.LINK_TEXT, value="Videos")
        super().__init__(driver, locator)

class News(BaseElement):
    def __init__(self, driver) -> None:
        locator = Locator(by=By.LINK_TEXT, value="Noticias")
        super().__init__(driver, locator)

class Shopping(BaseElement):
    def __init__(self, driver) -> None:
        locator = Locator(by=By.LINK_TEXT, value="Shopping")
        super().__init__(driver, locator)


class NavigationBar(BaseElement):

    def __init__(self, driver) -> None:
        locator = Locator(by=By.ID, value="hdtb-msb")
        super().__init__(driver, locator)
        self.imagesBtn = Images(driver)
        self.videosBtn = Videos(driver)
        self.newsBtn = News(driver)
        self.shoppingBtn = Shopping(driver)

    def goToImages(self):
        self.imagesBtn.click()

    def goToVideos(self):
        self.videosBtn.click()

    def goToNews(self):
        self.newsBtn.click()

    def goToShopping(self):
        self.shoppingBtn.click()