from selenium.webdriver.common.by import By

from tests.pages.BasePage import BasePage


class TopBar(BasePage):
    COMPANIES_BTN = (By.XPATH, "//a[@href='/companies']")
    PROPERTIES_BTN = (By.XPATH, "//a[@href='/properties']")
    RESET_BTN = (By.XPATH, "//form[@action='/reset']/button")
    SUCCESS_RESET_ALERT =  (By.CSS_SELECTOR, "div.alert-success.alert-dismissible")

    def click_company_btn(self):
        self.click(self.COMPANIES_BTN)

    def click_property_btn(self):
        self.click(self.PROPERTIES_BTN)

    def click_reset_btn(self):
        self.click(self.RESET_BTN)
        self.wait_until_locator_is_visible(self.SUCCESS_RESET_ALERT)