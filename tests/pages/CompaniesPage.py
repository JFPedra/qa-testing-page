from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from tests.pages.BasePage import BasePage


class CompaniesPage(BasePage):

    URL = 'http://localhost:5000/companies'
    CREATE_COMPANY_BTN = (By.LINK_TEXT, '+ Create Company')
    COMPANY_ROWS = (By.XPATH, '//tbody/tr')
    SUCCESS_DELETE_ALERT = (By.CSS_SELECTOR, "div.alert-success.alert-dismissible")

    def navigate_companies_page(self):
        self.navigate_to(self.URL)

    def click_create_company_btn(self):
        self.click(self.CREATE_COMPANY_BTN)

    def get_companies(self):
        rows = self.get_elements(self.COMPANY_ROWS)
        table = []
        for row in rows:
            data_cells = row.find_elements(By.TAG_NAME, 'td')
            table.append([data_cell.text for data_cell in data_cells[0:3]])
        return table

    def delete_company(self, company_name):
        company_index =str(self.find_company_index(company_name) + 1)
        self.click((By.XPATH, '//tbody/tr[i]//button'.replace('i', company_index)))
        Alert(self.driver).accept()

    def find_company_index(self, company_name):
        for i, row in enumerate(self.get_companies()):
            if company_name == row[0]:
                return i
        raise ValueError(f"Company '{company_name}' not found")

    def get_alert_messages(self):
        return self.get_text(self.SUCCESS_DELETE_ALERT)

