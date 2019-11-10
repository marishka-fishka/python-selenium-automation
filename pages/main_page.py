from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")
    ADD_CART_BUTTON = (By.CSS_SELECTOR, "input#add-to-cart-button")
    ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2")
    CART_ICON_BUTTON = (By.CSS_SELECTOR, "a#nav-cart")
    def search_for_keyword(self, text):
        self.input_text(text, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_ICON)

    def add_to_cart_button(self):
        self.click(*self.ADD_CART_BUTTON)

    def click_orders_link(self):
        self.click(*self.ORDERS_LINK)

    def click_cart_icon(self):
        self.click(*self.CART_ICON_BUTTON)