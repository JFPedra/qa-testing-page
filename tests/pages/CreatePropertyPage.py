from selenium.webdriver.common.by import By

from tests.pages.BasePage import BasePage


class CreatePropertyPage(BasePage):

    PROPERTY_NAME_FIELD = (By.ID, 'name')
    PROPERTY_ADDRESS_FIELD = (By.ID, 'address')
    PROPERTY_PRICE_FIELD = (By.ID, 'price')
    PROPERTY_SIZE_FIELD = (By.ID, 'size')
    PROPERTY_COMPANY_SELECT = (By.ID, 'company')
    CREATE_PROPERTY_BTN = (By.CSS_SELECTOR, 'button.btn-success')
    BACK_TO_LIST_BTN = (By.LINK_TEXT, 'Back to List')

    def enter_property_name(self, name):
        self.enter_text(self.PROPERTY_NAME_FIELD, name)

    def enter_property_address(self, address):
        self.enter_text(self.PROPERTY_ADDRESS_FIELD, address)

    def enter_property_price(self, price):
        self.enter_text(self.PROPERTY_PRICE_FIELD, price)

    def enter_property_size(self, size):
        self.enter_text(self.PROPERTY_SIZE_FIELD, size)

    def select_property_company(self, company):
        self.select_by_value(self.PROPERTY_COMPANY_SELECT, company)

    def click_create_property_btn(self):
        self.click(self.CREATE_PROPERTY_BTN)

    def click_back_to_list_btn(self):
        self.click(self.BACK_TO_LIST_BTN)
