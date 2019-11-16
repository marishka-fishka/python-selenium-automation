from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.amazon.com/'
        self.wait = WebDriverWait(self.driver, 15)
        self.actions = ActionChains(self.driver)

    def click(self, *locator):
        """
        Clicks on WebElement
        :param locator: search strategy for find_element of a Web Element, ex. (By.ID, 'id')

        """
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def open_page(self, url=''):
        self.driver.get(self.base_url + url)

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f'Expected text {expected_text}, but got {actual_text}'

    def verify_url(self, expected_url, *locator):
        current_url = self.driver.find_element(*locator).text
        assert expected_url == current_url, f'Expected url {expected_url}, but got {current_url}'

    def verify_amount_of_items(self, *locator):
        menu_len = len(self.driver.find_elements(*locator))
        assert menu_len == 6, f'Expected 6 items but got {menu_len}'

    def wait_for_element_click(self, *locator):
        e = self.driver.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_appear(self, *locator):
        self.driver.wait.until(EC.presence_of_element_located(locator))