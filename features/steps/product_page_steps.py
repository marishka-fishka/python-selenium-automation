from time import sleep

from behave import given, when, then
from selenium.webdriver.common.by import By


ADD_CART_BUTTON = (By.CSS_SELECTOR, "input#add-to-cart-button")
CLOSING_X_SIDE_SECTION = (By.ID, 'attach-close_sideSheet-link')

COLOR_OPTIONS = (By.CSS_SELECTOR, 'div#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR,'div#variation_color_name span.selection')


JEANS_COLORS = (By.CSS_SELECTOR, 'div#variation_color_name li')
SELECTED_JEANS_COLOR = (By.CSS_SELECTOR,'div#variation_color_name span.selection')

SEARCH_PRODUCTS = (By.XPATH, "//*[@id='wfm-pmd_deals_section']/div[6]//li")
NAME_PRODUCTS = (By.XPATH, "//*[@id='wfm-pmd_deals_section']/div[6]//li//span[@class='a-size-medium wfm-sales-item-card__product-name a-text-bold']")

@when('Click Add to cart button')
def add_cart_button(context):
    #context.driver.find_element(*ADD_CART_BUTTON).click()
     context.app.main_page.add_to_cart_button()


@when('Close suggestion side section')
def close_side_section(context):
    sleep(3)
    closing_btn = context.driver.find_elements(*CLOSING_X_SIDE_SECTION)
    if len(closing_btn) == 1:
        closing_btn[0].click()

@then('Verify user can select through colors')
def verify_colors(context):
    expected_colors = ['Black', 'Emerald', 'Ivory', 'Navy']
    color_webelements = context.driver.find_elements(*COLOR_OPTIONS)
    print(color_webelements)
   # for x in range(len(color_webelements)):
 #    color_webelements[x].click()
 #       actual_color = context.driver.find_element(*SELECTED_COLOR).text
 #       print(actual_color)
 #       assert actual_color == expected_colors[x], f'Expected {expected_colors[x]}, but got {actual_color}'
    for color in color_webelements:
        color.click()
        actual_color = context.driver.find_element(*SELECTED_COLOR).text

        assert actual_color == expected_colors[color_webelements.index(color)]

@then('Verify user can select through jeans colors')
def verify_jeans_colors(context):
    expected_colors = ['Medium Wash', 'Dark Wash', 'Rinse']
    color_webelements = context.driver.find_elements(*JEANS_COLORS)
    for color in color_webelements:
        color.click()
        actual_color = context.driver.find_element(*SELECTED_JEANS_COLOR).text
        assert actual_color == expected_colors[color_webelements.index(color)]

@then('Verify that every product has a text "Regular"')
def verify_text(context):
    text_webelements = context.driver.find_elements(*SEARCH_PRODUCTS)
    for text in text_webelements:
        text.click()
        actual_text = context.driver.find_element(*SEARCH_PRODUCTS).text
        assert 'Regular' in actual_text

@then('Verify a product name')
def verify_name(context):
    expected_names = ['Beyond Beef Plant-Based Ground', 'Previously Frozen Sockeye Salmon Fillets', 'Beef Round Sirloin Tip Roast', 'Extra Virgin Olive Oil Destination Series',
                       'Beef Boneless Bottom Round Roast', 'Premium Cooking Sauce', 'Beef Round Stew Meat', 'Pipcorn, Little Dippers and Cheese Balls',
                       'Alkaline Spring Water', 'Cereal', 'Beauty Collagens and Collagen Shots', 'Bath & Body', 'Cosmetics & Skin Care',
                       'Cabot Clothbound Cheddar', 'Sliced Genoa Salami']

    name_webelements = context.driver.find_elements(*NAME_PRODUCTS)
    for name in name_webelements:
        name.click()
        actual_name = context.driver.find_element(*NAME_PRODUCTS).text
        assert actual_name in expected_names, f'Expected {expected_names}, but got {actual_name}'



 #===========================================================================


@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.app.product_page.open_product(product_id)

@when('Hover over Add To Cart button')
def hover_add_to_cart(context):
    context.app.product_page.hover_add_to_cart()

@then('Verify size selection tooltip is shown')
def verify_size_tooltip(context):
    context.app.product_page.verify_size_tooltip()

#=================================================================================


@when('Hover over Sales and Deals button')
def hover_add_to_cart(context):
    context.app.product_page.hover_sales_and_deals_but()

@then('Verify that deals are present')
def verify_size_tooltip(context):
    context.app.product_page.verify_deals_present()