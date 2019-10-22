from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By


ADD_CART_BUTTON = (By.CSS_SELECTOR, "input#add-to-cart-button")
CLOSING_X_SIDE_SECTION = (By.ID, 'attach-close_sideSheet-link')


@when('Click Add to cart button')
def add_cart_button(context):
    context.driver.find_element(*ADD_CART_BUTTON).click()


@when('Close suggestion side section')
def close_side_section(context):
    sleep(3)
    closing_btn = context.driver.find_elements(*CLOSING_X_SIDE_SECTION)
    if len(closing_btn) == 1:
        closing_btn[0].click()
