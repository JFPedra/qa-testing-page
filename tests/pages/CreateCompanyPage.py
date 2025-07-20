from selenium.webdriver.common.by import By

from tests.pages.BasePage import BasePage

class CreateCompanyPage(BasePage):

    URL = 'http://localhost:5000/create-company'
    COMPANY_NAME_FIELD = (By.ID, 'name')
    COMPANY_TYPE_DROPDOWN = (By.ID, 'type')
    COMPANY_EMAIL_FIELD = (By.ID, 'email')
    CREATE_COMPANY_BTN = (By.CSS_SELECTOR, 'button.btn-success')
    BACK_TO_LIST_BTN = (By.LINK_TEXT, 'Back to List')

    def enter_company_name(self, name):
        self.enter_text(self.COMPANY_NAME_FIELD, name)

    def select_company_type(self, type):
        self.select_by_value(self.COMPANY_TYPE_DROPDOWN, type)

    def enter_company_email(self, email):
        self.enter_text(self.COMPANY_EMAIL_FIELD, email)

    def click_create_company_btn(self):
        self.click(self.CREATE_COMPANY_BTN)

    def click_back_to_list_btn(self):
        self.click(self.BACK_TO_LIST_BTN)



