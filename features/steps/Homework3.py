from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

@when('Click on the cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a#nav-cart').click()
    sleep(3)


@then('Verify that Shopping cart is empty')
def verify_shopping_cart_empty(context):
    assert 'empty' in context.driver.find_element(By.XPATH, "//h1[@class='sc-empty-cart-header']").text