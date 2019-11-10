from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


TOOLBAR_TEXT_BOLD = (By.CSS_SELECTOR, "h1 span.a-text-bold")
CARD_ITEM_COUNT = (By.ID, 'nav-cart-count')
EMAIL_FIELD = (By.CSS_SELECTOR, "input[type='email']")
ITEM_NAME = (By.CSS_SELECTOR, "a[id='dealTitle']")
FIRST_ELEMENT_IN_DEALS = (By.CSS_SELECTOR, "div[id='octopus-dlp-asin-stream'] [class='a-box a-box-normal a-color-base-background']")
CART_BUTTON = (By.ID, 'add-to-cart-button')

@then('Search results for {product} is shown')
def verify_result(context, product):
   # result_text = context.driver.find_element(*TOOLBAR_TEXT_BOLD).text
   # assert product in result_text, "Expected text is {product}, but got {result_text}"
    context.app.search_results_page.verify_result_shown(product)

@then('Verify cart has {expected_number} item')
def verify_number_of_item(context, expected_number):
    context.driver.wait.until(EC.element_to_be_clickable)
    actual_number_of_items = len(context.driver.find_element(*CARD_ITEM_COUNT).text)
    assert actual_number_of_items == int(
        expected_number), f'Expected {expected_number}, but got {actual_number_of_items}'


@when('Put item in the cart')
def put_item_in_cart(context):
   context.driver.find_element(*ITEM_NAME).click()
   sleep(5)
   item_numbers = context.driver.find_elements(*FIRST_ELEMENT_IN_DEALS)
   if len(item_numbers) > 1:
       item_numbers[0].click()
   context.driver.find_element(*CART_BUTTON).click()


@then('Verify Sign In page is opened')
def verify_signin_opened(context):
    context.driver.find_element(*EMAIL_FIELD)
    assert 'https://www.amazon.com/ap/signin' in context.driver.current_url
    #context.app.search_results_page.verify_sign_in_opened('https://www.amazon.com/ap/signin')
