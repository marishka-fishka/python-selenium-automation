from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class ProductPage(Page):

    CART_BUTTON = (By.ID, 'add-to-cart-button')
    SIZE_SELECTION_TOOLTIP = (By.ID, 'a-popover-content-1')
    SALES_AND_DEALS_BUTTON = (By.CSS_SELECTOR, "div[id='nav-subnav'] a[class='nav-a nav-hasArrow']")
    DEALS_ARE_PRESENT = (By.XPATH, "//img[contains(@src,'FLYOUT/flyout__fall3_women._CB448971046_.jpg')]")


    def open_product(self, product_id):
        self.open_page(f'dp/{product_id}')

    def hover_add_to_cart(self):
        cart_button = self.find_element(*self.CART_BUTTON)
        self.actions.move_to_element(cart_button).perform()


    def verify_size_tooltip(self):
        self.wait_for_element_appear(*self.SIZE_SELECTION_TOOLTIP)

    def hover_sales_and_deals_but(self):
        sales_and_deals_button = self.find_element(*self.SALES_AND_DEALS_BUTTON)
        self.actions.move_to_element(sales_and_deals_button).perform()

    def verify_deals_present(self):
        self.wait_for_element_appear(*self.DEALS_ARE_PRESENT)



