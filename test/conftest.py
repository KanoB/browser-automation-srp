import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

HEADLESS = os.environ.get("HEADLESS", 0) == 1

@pytest.fixture
def driver():
    driver_location = r"C:\tools\webdriver\chromedriver.exe"
    service = Service(executable_path=driver_location, log_path="./chromedriver.log")
    options = Options()
    options.add_argument("start-maximized")

    # References:
    # https://peter.sh/experiments/chromium-command-line-switches/
    # https://stackoverflow.com/questions/57298901/unable-to-hide-chrome-is-being-controlled-by-automated-software-infobar-within
    options.add_experimental_option('excludeSwitches', 
        [
            'enable-logging', # Disable USB kind of errors
            'enable-automation', # Disable banner warning chrome is running with automation
        ],
    )
    
    if HEADLESS:
        options.add_argument("--headless")

    driver = webdriver.Chrome(options=options, service=service)

    yield driver
    
    # time.sleep(2)
    driver.quit()
