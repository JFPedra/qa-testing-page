from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

from tests.pages.BasePage import BasePage


class PropertiesPage(BasePage):
    URL = 'http://localhost:5000/properties'
    CREATE_COMPANY_BTN = (By.LINK_TEXT, '+ Create Property')
    PROPERTY_ROWS = (By.XPATH, '//tbody/tr')
    SUCCESS_DELETE_ALERT = (By.CSS_SELECTOR, "div.alert-success.alert-dismissible")

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

    def delete_property(self, property_name):
        index = self.find_property_index(property_name)
        delete_button_locator = (By.XPATH, f"//tbody/tr[{index + 1}]//button")
        self.click(delete_button_locator)
        Alert(self.driver).accept()

    def find_property_index(self, property_name):
        for i, row in enumerate(self.get_properties()):
            if property_name == row[0]:
                return i
        raise ValueError(f"Company '{property_name}' not found")

    def get_alert_messages(self):
        return self.get_text(self.SUCCESS_DELETE_ALERT)
