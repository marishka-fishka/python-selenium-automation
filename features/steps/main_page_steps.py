from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2")
SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")
HAM_MENU = (By.ID, 'nav-hamburger-menu')
AMAZON_MUSIC_MENU_ITEM = (By.XPATH, "//ul[contains(@class, 'menu-visible')]//div[contains(text(), 'Amazon Music')]")
AMAZON_MUSIC_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, 'ul.hmenu-visible a:not(.hmenu-back-button)')
SEARCH_FIRST_PRODUCT_RESULTS = (By.XPATH, "//span[@class='a-size-base-plus a-color-base a-text-normal']")
DEALS_UNDER_25_LINK=(By.XPATH, "//a[contains(@aria-label, 'deals under $25')]")
SIGN_IN_TOOLTIP = (By.CSS_SELECTOR, "div#nav-signin-tooltip")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')

@given('Open Amazon wholefoods page')
def open_wholeffods_page(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')



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


#=======================$25 DEALS==============================

@when('Store original windows')
def store_current_windows(context):
    context.original_window = context.driver.current_window_handle
    context.old_windows = context.driver.window_handles
    print('original_window',  context.original_window)
    print('old_window', context.old_windows)

@when('Click to open Deals under 25')
def click_to_open_deals_under_25(context):
    context.driver.find_element(*DEALS_UNDER_25_LINK).click()

@when('Switch to the newly opened window')
def switch_to_new_window(context):
    # wait for new window
    context.driver.wait.until(EC.new_window_is_opened)

    current_windows = context.driver.window_handles
    print('\n"current_windows"\n' , current_windows)

    #new_window = current_windows[1]
    #print('new_window', new_window)

    new_windows = current_windows
    for old_window in context.old_windows:
        new_windows.remove(old_window)
    print('new_windows', new_windows)
    # Switch to freshly opened window
    context.driver.switch_to_window(new_windows[0])

@then('User can close new window and switch back to original')
def close_and_switch_window_back(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)
    sleep(4)

@when('Refresh the page')
def refresh_the_page(context):
    context.driver.refresh()
    sleep(4)



#=======================TOOLTIP==============================

@then('Verify SignIn tooltip is present and clickable')
def verify_signin_tooltip_clickable(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(*SIGN_IN_TOOLTIP)
    )

@When('Wait until SignIn tooltip disappears')
def wait_signin_tooltip_dissappears(context):
    context.driver.wait.until(
        EC.invisibility_of_element_located(SIGN_IN_TOOLTIP)
    )

@then('Verify SignIn tooltip is not clickable')
def wait_signin_tooltip_clickable(context):

    context.driver.wait.until_not(
        EC.element_to_be_clickable(SIGN_IN_TOOLTIP)
    )