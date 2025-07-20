from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import logging

@pytest.fixture
def chrome_driver():
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.headless = True
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()
