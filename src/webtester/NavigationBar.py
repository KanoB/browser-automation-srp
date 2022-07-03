from selenium.webdriver.common.by import By

from webtester.BaseElement import BaseElement

class NavAll(BaseElement):
    def __init__(self, driver) -> None:
        super().__init__(driver, "Todos", By.LINK_TEXT)

class Images(BaseElement):
    def __init__(self, driver) -> None:
        super().__init__(driver, "Imágenes", By.LINK_TEXT)

class Videos(BaseElement):
    def __init__(self, driver) -> None:
        super().__init__(driver, "Videos", By.LINK_TEXT)

class News(BaseElement):
    def __init__(self, driver) -> None:
        super().__init__(driver, "Noticias", By.LINK_TEXT)

class Shopping(BaseElement):
    def __init__(self, driver) -> None:
        super().__init__(driver, "Shopping", By.LINK_TEXT)


class NavigationBar(BaseElement):

    def __init__(self, driver) -> None:
        super().__init__(driver, "hdtb-msb", By.ID)
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