# webdriver is needed to start the browser driver e.g. chromedriver
from selenium import webdriver
# Add the sleep function
from time import sleep

#driver = webdriver.Chrome(executable_path='/Users/marco/PycharmProjects/ScriptingForTesters_TM/03_01/end/chromedriver')
driver = webdriver.Chrome(executable_path='/Users/marco/PycharmProjects/ScriptingForTesters_TM/chromedriver')

driver.get('http://google.com')

element = driver.find_element_by_name('q')

element.send_keys("test")

from selenium.webdriver.common.keys import Keys
element.send_keys(Keys.RETURN)

# sleep 60 seconds to observe the result
sleep(60)
driver.quit()