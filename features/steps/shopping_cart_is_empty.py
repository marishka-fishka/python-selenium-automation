from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


SHOPPING_CART_EMPTY = (By.XPATH, "//h1[@class='sc-empty-cart-header']")
@when('Click on the cart icon')
def click_cart_icon(context):
#     cart_icon = context.driver.find_element(By.CSS_SELECTOR, 'a#nav-cart')
#     print(cart_icon)
#     context.driver.refresh()
#     cart_icon = context.driver.find_element(By.CSS_SELECTOR, 'a#nav-cart')
#     print(cart_icon)
#     cart_icon.click()
#     sleep(3)
     context.app.main_page.click_cart_icon()


@then('Verify {expected_text} text present')
def verify_shopping_cart_empty(context, expected_text):
    # result_text = context.driver.find_element(*SHOPPING_CART_EMPTY).text
    # assert expected_text == result_text
    context.app.search_results_page.verify_shopping_cart_empty(expected_text)