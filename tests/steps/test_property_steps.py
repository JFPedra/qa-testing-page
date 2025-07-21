from assertpy import assert_that, soft_assertions
from pytest_bdd import given, when, then, parsers

from tests.pages.CreatePropertyPage import CreatePropertyPage
from tests.pages.PropertiesPage import PropertiesPage

@given("the user is in the Properies Page")
def navigate_properties_page(chrome_driver):
    properties_page = PropertiesPage(chrome_driver)
    properties_page.navigate_properties_page()

@then("the user is in the Properies Page")
def validate_properties_page(chrome_driver):
    properties_page = PropertiesPage(chrome_driver)
    properties_page.wait_until_url_is(properties_page.URL)
    assert_that(properties_page.get_page_title()).is_equal_to('Properties List')

@when("the user clicks on +Create Property")
def click_create_property(chrome_driver):
    properties_page = PropertiesPage(chrome_driver)
    properties_page.click_create_property_btn()

@when(parsers.parse("the user enters '{name}' as Property Name"))
def enter_property_name(chrome_driver, name):
    create_properties_page = CreatePropertyPage(chrome_driver)
    create_properties_page.enter_property_name(name)

@when(parsers.parse("the user enters '{address}' as Address"))
def enter_address(chrome_driver, address):
    create_properties_page = CreatePropertyPage(chrome_driver)
    create_properties_page.enter_property_address(address)

@when(parsers.parse("the user enters '{price}' as Price"))
def enter_property_price(chrome_driver, price):
    create_properties_page = CreatePropertyPage(chrome_driver)
    create_properties_page.enter_property_price(price)

@when(parsers.parse("the user enters '{size}' as Size"))
def enter_property_size(chrome_driver, size):
    create_properties_page = CreatePropertyPage(chrome_driver)
    create_properties_page.enter_property_size(size)

@when(parsers.parse("the user selects '{company}' as Company"))
def select_company(chrome_driver, company):
    create_properties_page = CreatePropertyPage(chrome_driver)
    create_properties_page.select_property_company(company)

@when('the user clicks on Create Property')
def click_create_property_btn(chrome_driver):
    create_properties_page = CreatePropertyPage(chrome_driver)
    create_properties_page.click_create_property_btn()

@when(parsers.parse("the user clicks on delete the property '{property_name}'"))
@then(parsers.parse("the user clicks on delete the property '{property_name}'"))
def delete_property(property_name, chrome_driver):
    properties_page = PropertiesPage(chrome_driver)
    properties_page.delete_property(property_name)


@then("the following properties are listed:")
def validate_properties_listed(datatable, chrome_driver):
    properties_page = PropertiesPage(chrome_driver)
    properties_list = properties_page.get_properties()
    with soft_assertions():
        for property in datatable:
            assert_that(properties_list, f"property '{property[0]}' was not listed").contains(property)

@then("the following properties are not listed:")
def validate_properties_not_listed(datatable, chrome_driver):
    properties_page = PropertiesPage(chrome_driver)
    properties_list = properties_page.get_properties()
    with soft_assertions():
        for property in datatable:
            assert_that(properties_list, f"property '{property[0]}' was listed").does_not_contain(property)

@then("the user remains in the Create Property Page")
def validate_create_property_page(chrome_driver):
    create_properties_page = CreatePropertyPage(chrome_driver)
    assert_that(create_properties_page.get_page_title()).is_equal_to('Create Property')

@then("alert of negative price is displayed")
def validate_negative_price_alert(chrome_driver):
    properties_page = PropertiesPage(chrome_driver)
    assert_that(properties_page.get_error_alert_messages()).is_equal_to('Price must be a positive number.')

@then("property successfully deleted alert is displayed")
def validate_delete_property_alert(chrome_driver):
    properties_page = PropertiesPage(chrome_driver)
    assert_that(properties_page.get_success_alert_messages()).is_equal_to('Property deleted.')
