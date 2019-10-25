from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By


ADD_CART_BUTTON = (By.CSS_SELECTOR, "input#add-to-cart-button")
CLOSING_X_SIDE_SECTION = (By.ID, 'attach-close_sideSheet-link')


JEANS_COLORS = (By.CSS_SELECTOR, 'div#variation_color_name li')
SELECTED_JEANS_COLOR = (By.CSS_SELECTOR,'div#variation_color_name span.selection')

@when('Click Add to cart button')
def add_cart_button(context):
    context.driver.find_element(*ADD_CART_BUTTON).click()


@when('Close suggestion side section')
def close_side_section(context):
    sleep(3)
    closing_btn = context.driver.find_elements(*CLOSING_X_SIDE_SECTION)
    if len(closing_btn) == 1:
        closing_btn[0].click()


@then('Verify user can select through jeans colors')
def verify_jeans_colors(context):
    expected_colors = ['Medium Wash', 'Dark Wash', 'Rinse']
    color_webelements = context.driver.find_elements(*JEANS_COLORS)
    for color in color_webelements:
        color.click()
        actual_color = context.driver.find_element(*SELECTED_JEANS_COLOR).text
        assert actual_color == expected_colors[color_webelements.index(color)]