from behave import given, when, then
from selenium.webdriver.common.by import By

SEARCH_CANCEL_ORDER1 = (By.XPATH, "//input[@id='helpsearch']")
SEARCH_SUBMIT = (By.XPATH, "//input[@class='a-button-input']")
SEARCH_RESULT = (By.XPATH, "//div[contains(@class, 'help-content')]")



@given('Open Amazon page and Amazon Help tab')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Click on search field')
def click_field(context):
    context.driver.find_element(*SEARCH_CANCEL_ORDER1).click()



@when('Input {text} in search field')
def input_text(context, text):
    context.driver.find_element(*SEARCH_CANCEL_ORDER1).clear()
    context.driver.find_element(*SEARCH_CANCEL_ORDER1).send_keys(text)


@when('Click on search icon1')
def click_search_icon(context):
    search = context.driver.find_element(*SEARCH_SUBMIT).click()


@then('Search results for Cancel order is shown')
def verify_result(context):
    assert 'Cancel Items or Orders' in context.driver.find_element(*SEARCH_RESULT).text
