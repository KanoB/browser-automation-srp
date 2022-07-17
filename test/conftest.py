import os
import pytest
import tempfile
import shutil

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


HEADLESS = os.environ.get("HEADLESS") == "true"

@pytest.fixture(scope="session")
def driver():
    driver_location = r"C:\tools\webdriver\chromedriver.exe"
    service = Service(executable_path=driver_location, log_path="./chromedriver.log")
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("incognito")
    options.add_argument("disable-extensions")
    options.add_argument("disable-popup-blocking") # Pop up blocking
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")

    # References:
    # https://peter.sh/experiments/chromium-command-line-switches/
    # https://stackoverflow.com/questions/57298901/unable-to-hide-chrome-is-being-controlled-by-automated-software-infobar-within
    options.add_experimental_option('excludeSwitches', 
        [
            'enable-logging', # Disable USB kind of errors
            'enable-automation', # Disable banner warning chrome is running with automation
        ],
    )

    # Change default download directory
    tempdir = tempfile.mkdtemp(prefix="webtester-")
    prefs = {"download.default_directory" : tempdir}
    options.add_experimental_option("prefs", prefs)

    if HEADLESS:
        options.add_argument("headless")

    driver = webdriver.Chrome(options=options, service=service)

    yield driver
    
    # time.sleep(2)
    shutil.rmtree(tempdir)
    driver.quit()
