from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest

from tests.pages.TopBar import TopBar


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

def pytest_bdd_after_scenario(request):
    driver = request.getfixturevalue("chrome_driver")
    top_bar = TopBar(driver)
    top_bar.click_reset_btn()