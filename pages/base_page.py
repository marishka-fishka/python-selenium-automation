class Page:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.amazon.com/'

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text,  *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def open_page(self, url=''):
        self.driver.get(self.base_url + url)

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f'Expected text {expected_text}, but got {actual_text}'

    def verify_url(self, expected_url, *locator ):
        current_url = self.driver.find_element(*locator).text
        assert expected_url == current_url, f'Expected url {expected_url}, but got {current_url}'