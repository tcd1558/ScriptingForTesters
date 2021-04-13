# webdriver is needed to start the browser driver e.g. chromedriver
from selenium import webdriver
# Add the sleep function
from time import sleep

driver = webdriver.Chrome(executable_path='/Users/marco/PycharmProjects/ScriptingForTesters_TM/chromedriver')

driver.get('http://www.phptravels.net/offers')

b_tags=driver.find_elements_by_tag_name('b')
for b_tag in b_tags:
    print(btag)

sleep(60)
driver.quit()