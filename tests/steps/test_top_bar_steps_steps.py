from pytest_bdd import given, scenarios

from tests.conftest import chrome_driver
from tests.pages.TopBar import TopBar

@given('the data is reset')
def reset_data(chrome_driver):
    top_bar = TopBar(chrome_driver)
    top_bar.click_reset_btn()