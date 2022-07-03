class BasePage():
    """Base webpage class
    
    Derive all your pages from here
    """

    url = None

    def __init__(self, driver) -> None:
        # super().__init__()
        self.driver = driver

    def go(self):
        if self.url is not None:
            self.driver.get(self.url)

    def refresh(self):
        self.driver.refresh()