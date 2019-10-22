from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2")
SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")
HAM_MENU = (By.ID, 'nav-hamburger-menu')
AMAZON_MUSIC_MENU_ITEM = (By.XPATH, "//ul[contains(@class, 'menu-visible')]//div[contains(text(), 'Amazon Music')]")
AMAZON_MUSIC_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, 'ul.hmenu-visible a:not(.hmenu-back-button)')
SEARCH_FIRST_PRODUCT_RESULTS = (By.XPATH, "//span[@class='a-size-base-plus a-color-base a-text-normal']")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when('Click Amazon Orders link')
def click_orders_link(context):
    context.driver.find_element(*ORDERS_LINK).click()


@when('Search for {product}')
def search_product(context, product):
    search_field = context.driver.find_element(*SEARCH_INPUT)
    search_field.clear()
    search_field.send_keys(product)
    context.driver.find_element(*SEARCH_ICON).click()


@when('Open the first product search result')
def first_product_result(context):
    context.driver.find_element(*SEARCH_FIRST_PRODUCT_RESULTS).click()


@when('Click on hamburger menu')
def click_ham_menu(context):
    context.driver.find_element(*HAM_MENU).click()


@when('Click on Amazon Music menu item')
def click_amazon_music(context):
    context.driver.find_element(*AMAZON_MUSIC_MENU_ITEM).click()


@then('6 menu items are present')
def verify_amount_of_items(context):
    sleep(3)
    print(len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULTS)))
    assert len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULTS)) == 6, \
        f'Expected 6 items but got {len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULTS))}'
