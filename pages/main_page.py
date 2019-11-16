from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class MainPage(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")
    ADD_CART_BUTTON = (By.CSS_SELECTOR, "input#add-to-cart-button")
    ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2")
    CART_ICON_BUTTON = (By.CSS_SELECTOR, "a#nav-cart")
    HAM_MENU = (By.ID, 'nav-hamburger-menu')
    AMAZON_MUSIC_MENU_ITEM = (By.XPATH, "//ul[contains(@class, 'menu-visible')]//div[contains(text(), 'Amazon Music')]")
    AMAZON_MUSIC_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, 'ul.hmenu-visible a:not(.hmenu-back-button)')
    SELECT_DEPARTMENT = (By.CSS_SELECTOR, 'select.nav-search-dropdown')
    PRODUCT_NAME = (By.CSS_SELECTOR, "span[class='a-color-state a-text-bold']")
    def search_for_keyword(self, text):
        self.input_text(text, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_ICON)

    def add_to_cart_button(self):
        self.click(*self.ADD_CART_BUTTON)

    def click_orders_link(self):
        self.click(*self.ORDERS_LINK)

    def click_cart_icon(self):
        self.click(*self.CART_ICON_BUTTON)

    def click_hamburger_menu(self):
        self.click(*self.HAM_MENU)

    def click_Amazon_music_icon(self):
        self.click(*self.AMAZON_MUSIC_MENU_ITEM)
        sleep(1)

    def verify_6_menu_items(self):
        self.verify_amount_of_items(*self.AMAZON_MUSIC_MENU_ITEM_RESULTS)

    def select_department(self):
        select_department_element = self.find_element(*self.SELECT_DEPARTMENT)
        select = Select(select_department_element)
        select.select_by_value('search-alias=garden')

    def department_selected(self, product):
        self.verify_text(product, *self.PRODUCT_NAME)





