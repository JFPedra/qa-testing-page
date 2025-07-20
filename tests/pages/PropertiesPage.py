from selenium.webdriver.common.by import By

from tests.pages.BasePage import BasePage


class PropertiesPage(BasePage):
    URL = 'http://localhost:5000/properties'
    CREATE_COMPANY_BTN = (By.LINK_TEXT, '+ Create Property')
    PROPERTY_ROWS = (By.XPATH, '//tbody/tr')

    def navigate_properties_page(self):
        self.navigate_to(self.URL)

    def click_create_property_btn(self):
        self.click(self.CREATE_COMPANY_BTN)

    def get_properties(self):
        rows = self.get_elements(self.PROPERTY_ROWS)
        table = []
        for row in rows:
            data_cells = row.find_elements(By.TAG_NAME, 'td')
            table.append([data_cell.text for data_cell in data_cells[0:5]])
        return table