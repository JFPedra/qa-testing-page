from pytest_bdd import given, when

from tests.conftest import chrome_driver
from tests.pages.TopBar import TopBar

@given('the data is reset')
def reset_data(chrome_driver):
    top_bar = TopBar(chrome_driver)
    top_bar.click_reset_btn()

@when('the user clicks on Properties')
def click_properties(chrome_driver):
    top_bar = TopBar(chrome_driver)
    top_bar.click_property_btn()