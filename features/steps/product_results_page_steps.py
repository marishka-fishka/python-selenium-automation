from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


TOOLBAR_TEXT_BOLD = (By.CSS_SELECTOR, "h1 span.a-text-bold")
CARD_ITEM_COUNT = (By.ID, 'nav-cart-count')


@then('Search results for {product} is shown')
def verify_result(context, product):
    result_text = context.driver.find_element(*TOOLBAR_TEXT_BOLD).text
    assert product in result_text, "Expected text is dress, but got {result_text}"


@then('Verify cart has {expected_number} item')
def verify_number_of_item(context, expected_number):
    sleep(3)
    actual_number_of_items = len(context.driver.find_element(*CARD_ITEM_COUNT).text)
    assert actual_number_of_items == int(
        expected_number), f'Expected {expected_number}, but got {actual_number_of_items}'


@when('Put item in the cart')
def put_item_in_cart(context):
   context.driver.find_element(By.CSS_SELECTOR, "a[id='dealTitle']").click()
   context.driver.wait.until(EC.element_to_be_clickable)
   context.driver.find_element(By.ID, 'add-to-cart-button').click()
   context.driver.wait.until(EC.element_to_be_clickable)
   context.driver.find_element(By.CSS_SELECTOR, "button[id='attachSiAddCoverage-announce']").click()


