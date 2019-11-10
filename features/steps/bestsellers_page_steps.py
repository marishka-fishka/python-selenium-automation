from  behave import then
from selenium.webdriver.common.by import By
from time import sleep

BEST_SELLERS_LINK = (By.XPATH, "//a[contains(text(), 'Best Sellers')]")
TOP_LINKS = (By.CSS_SELECTOR,'#zg_tabs a')
HEADER = (By.CSS_SELECTOR, '#zg_banner_text_wrapper')


@when('Click on Best Sellers link')
def click_best_sellers(context):
    best_sellers = context.driver.find_element(*BEST_SELLERS_LINK)
    best_sellers.click()

@then ('User can click through top links and verify correct page opens')
def click_thru_top(context):
    top_links=context.driver.find_elements(*TOP_LINKS)
    for x in range(len(top_links)):
        link_to_click = context.driver.find_elements(*TOP_LINKS)[x]
        link_text = link_to_click.text
        link_to_click.click()
        sleep(1)

        new_text = context.driver.find_element(*HEADER).text
        assert link_text in new_text, f'Expected {link_text} to be in {new_text}'