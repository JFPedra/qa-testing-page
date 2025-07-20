from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_until_url_is(self, url):
        self.wait.until(EC.url_to_be(url))

    def wait_until_locator_is_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    def get_page_title(self):
        return self.driver.title

    def get_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def navigate_to(self, url):
        self.driver.get(url)

    def click(self, locator):
        element = self.get_element(locator)
        self.wait.until(EC.element_to_be_clickable(element))
        element.click()

    def get_text(self, locator):
        return self.get_element(locator).text

    def get_elements(self, locator):
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def enter_text(self, locator, text):
        self.get_element(locator).send_keys(text)

    def select_by_value(self, select_locator, value):
        element = self.get_element(select_locator)
        Select(element).select_by_value(value)

