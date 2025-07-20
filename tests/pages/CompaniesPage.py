from selenium.webdriver.common.by import By

from tests.pages.BasePage import BasePage


class CompaniesPage(BasePage):

    URL = ''
    CREATE_COMPANY_BTN = (By.LINK_TEXT, '/create-company')
    COMPANY_ROWS = (By.XPATH, '//tbody/tr')

    def navigate_companies_page(self):
        self.navigate_to('http://localhost:5000/companies')

    def get_companies(self):
        rows = self.get_elements(self.COMPANY_ROWS)
        table = []
        for row in rows:
            data_cells = row.find_elements(By.TAG_NAME, 'td')
            table.append([data_cell.text for data_cell in data_cells[0:3]])
        return table

