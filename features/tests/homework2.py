from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver=webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com')
sleep(1)

driver.get('https://www.amazon.com/gp/help/customer/display.html')

driver.find_element(By.XPATH, "//input[@id='helpsearch']").click()
search = driver.find_element(By.NAME, 'help_keywords')
search.clear()
search.send_keys('Cancel order')

# wait for 4 sec
sleep(4)

# Click search
driver.find_element(By.XPATH, "//input[@class='a-button-input']").click()

# verify
assert 'Cancel Items or Orders' in driver.find_element(By.XPATH, "//div[contains(@class, 'help-content')]").text

driver.quit()
