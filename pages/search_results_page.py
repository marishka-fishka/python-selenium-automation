from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResults(Page):
    TOOLBAR_TEXT_BOLD = (By.CSS_SELECTOR, "h1 span.a-text-bold")
    SHOPPING_CART_EMPTY = (By.XPATH, "//h1[@class='sc-empty-cart-header']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[type='email']")

    def verify_result_shown(self, expected_text):
        self.verify_text(expected_text, *self.TOOLBAR_TEXT_BOLD)

    def verify_shopping_cart_empty(self, expected_text):
        self.verify_text(expected_text, *self.SHOPPING_CART_EMPTY)

    def verify_sign_in_opened(self, expected_url):
        self.verify_url(expected_url, *self.EMAIL_FIELD )