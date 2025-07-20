from pytest_bdd import given, when, then, parsers
from assertpy import assert_that

from tests.pages.CompaniesPage import CompaniesPage
from tests.pages.CreateCompanyPage import CreateCompanyPage


@given('the user is in the companies page')
def navigate_to_companies_page(chrome_driver):
    companies_page = CompaniesPage(chrome_driver)
    companies_page.navigate_companies_page()

@then('the user is in the companies page')
def validate_companies_page(chrome_driver):
    companies_page = CompaniesPage(chrome_driver)
    companies_page.wait_until_url_is(companies_page.URL)
    assert_that(companies_page.get_page_title()).is_equal_to('Companies List')

@when('the user clicks on + Create Company')
def click_on_company_create(chrome_driver):
    companies_page = CompaniesPage(chrome_driver)
    companies_page.click_create_company_btn()

@when(parsers.parse("the user enters '{name}' as Company Name"))
def enter_company_name(name, chrome_driver):
    create_company_page = CreateCompanyPage(chrome_driver)
    create_company_page.enter_company_name(name)

@when(parsers.parse("the user selects '{type}' as Company Type"))
def select_company_type(type, chrome_driver):
    create_company_page = CreateCompanyPage(chrome_driver)
    create_company_page.select_company_type(type)

@when(parsers.parse("the user enters '{email}' as Email"))
def enter_email(email, chrome_driver):
    create_company_page = CreateCompanyPage(chrome_driver)
    create_company_page.enter_company_email(email)

@when("the user clicks on Create Company")
def create_company(chrome_driver):
    create_company_page = CreateCompanyPage(chrome_driver)
    create_company_page.click_create_company_btn()

@then('the following companies are listed:')
def validate_companies_listed(datatable, chrome_driver):
    companies_page = CompaniesPage(chrome_driver)
    companies_list = companies_page.get_companies()
    for company in datatable:
        assert_that(companies_list, f"company '{company[0]}' was not listed").contains(company)

