from assertpy import assert_that
from pytest_bdd import given, then

from tests.pages.PropertiesPage import PropertiesPage

@given("the user is in the properties page")
def navigate_properties_page(chrome_driver):
    properties_page = PropertiesPage(chrome_driver)
    properties_page.navigate_properties_page()

@then("the following properties are listed:")
def validate_properties_listed(datatable, chrome_driver):
    properties_page = PropertiesPage(chrome_driver)
    properties_list = properties_page.get_properties()
    for property in datatable:
        assert_that(properties_list, f"property '{property[0]}' was not listed").contains(property)
