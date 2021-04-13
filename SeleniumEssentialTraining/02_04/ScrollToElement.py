# This script opens a webdriver (Chrome) to access
# the test website https://formy-project.herokuapp.com
# waits until a field becomes visible, moves to it and
# enters a string and a date
# Then it sleeps for 60 seconds and closes the browser

# webdriver is needed to start the browser driver e.g. chromedriver
from selenium import webdriver
# Add the sleep function
from time import sleep
# Add special characters, e.g. RETURN to control web pages
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set a variable where to find the chromedriver executable.
ChromeDriver='/Users/marco/PycharmProjects/ScriptingForTesters_TM/chromedriver'
HTML='https://formy-project.herokuapp.com/scroll'

# Create a new instance of ChromeDriver
driver = webdriver.Chrome(executable_path=ChromeDriver)

# And now use the driver to open the google website
driver.get(HTML)

# Find the text input element by its name
# name = driver.find_element_by_id('name')
# date = driver.find_element_by_id('date')

# autocomplete.send_keys('1558 Timber Creek Drive, San')
# Wait for Name field to show up (using Explicit Wait)
# https://stackoverflow.com/questions/27934945/selenium-move-to-element-does-not-always-mouse-hover
# https://selenium-python.readthedocs.io/waits.html
# 'By' takes capitalized methods : ID, XPATH, LINK_TEXT, PARTIAL_LINK_TEXT, NAME, TAG_NAME, CLASS_NAME, CSS_SELECTOR
name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "name")))
action=ActionChains(driver)
action.move_to_element(name).perform()
name.send_keys('Billy Kimber')

# wait for Fastrack menu item to appear, then click it
date = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "date")))
date.send_keys('02/11/2021')

# sleep 60 seconds to observe the result
sleep(60)
driver.quit()
