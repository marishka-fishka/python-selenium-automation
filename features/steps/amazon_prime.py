from behave import given, then, when
from selenium.webdriver.common.by import By
from  time import sleep

AMAZON_PRIME_BOXES_RESULTS=(By.XPATH, "//div[@class='a-section a-spacing-none benefit-container']//div[contains(@class,'a-column a-span6')]")

@when('Open Prime page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/amazonprime')

@then('Verify that {expected_boxes_count} boxes are present')
def verify_amount_of_items(context, expected_boxes_count):
    sleep(3)
    actual_boxes_count = len(context.driver.find_elements(*AMAZON_PRIME_BOXES_RESULTS))
    assert actual_boxes_count == int(expected_boxes_count),\
        f'Expected {expected_boxes_count} items but got {actual_boxes_count}'
