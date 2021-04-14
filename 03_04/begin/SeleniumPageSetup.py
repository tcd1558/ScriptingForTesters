from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

#driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path='/Users/marco/PycharmProjects/ScriptingForTesters_TM/chromedriver')

url = 'http://automationpractice.com/index.php?id_category=3&controller=category'
driver.get(url)

product_containers = driver.find_elements_by_class_name('product-container')

for index,product_container in enumerate(product_containers):
    hover = ActionChains(driver).move_to_element(product_container)
    hover.perform()
    real_index=index+3
    time.sleep(2)
    # Add to Cart
    #driver.find_element_by_xpath('//*[@id="center_column"]/ul/li[%s]/div/div[2]/div[2]/a[1]/span'%real_index).click()
    #   selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable
    driver.find_element_by_css_selector('a.button.ajax_add_to_cart_button.btn.btn-default').click()
    # From Copy Selector: a.button.ajax_add_to_cart_button.btn.btn-default

    # selector of 1st element:
    # center_column > ul > li.ajax_block_product.col-xs-12.col-sm-6.col-md-4.last-item-of-tablet-line.hovered > div > div.right-block > div.button-container > a.button.ajax_add_to_cart_button.btn.btn-default
    # selector of 2nd element:
    # center_column > ul > li:nth-child(1) > div > div.right-block > div.button-container >                                                                    a.button.ajax_add_to_cart_button.btn.btn-default
    # The css_selector works with the first item, but fails with the second one:
    #   selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable
    time.sleep(1)

    # Continue Shopping
    # driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span/span').click()
    driver.find_element_by_css_selector('span.continue.btn.btn-default.button.exclusive-medium').click()
    # layer_cart > div.clearfix > div.layer_cart_cart.col-xs-12.col-md-6 > div.button-container > span > span
    time.sleep(1)

# sleep 60 seconds to observe the result
sleep(60)
driver.quit()