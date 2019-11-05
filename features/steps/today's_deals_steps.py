from behave import then
from selenium.webdriver.common.by import By


TODAYS_DEALS_HEADER = (By.CSS_SELECTOR, "div[class='a-row a-spacing-top-small suppleTitle']")

@then("{expected_header} are shown")
def header_is_correct(context, expected_header):
    actual_header = context.driver.find_element(*TODAYS_DEALS_HEADER).text
    assert  actual_header == expected_header, f'Expected {expected_header}, but got {actual_header}'
