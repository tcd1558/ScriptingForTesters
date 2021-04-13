# This script opens a webdriver (Chrome) to access
# the test website https://formy-project.herokuapp.com
# enters a string and clicks on a button
# Then it sleeps for 60 seconds and closes the browser
#
# Reset button is not found

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
HTML='https://formy-project.herokuapp.com/autocomplete'

# Create a new instance of ChromeDriver
driver = webdriver.Chrome(executable_path=ChromeDriver)

# And now use the driver to open the google website
driver.get(HTML)

sleep(5) # takes time to load
# Find the text input element by its name
autocomplete= driver.find_element_by_id('autocomplete')
autocomplete.send_keys("1555 Park Blvd, Palo Alto, CA")

# explicit wait
# https://selenium-python.readthedocs.io/waits.html
# https://www.tutorialspoint.com/what-is-implicit-wait-in-selenium-with-python
# 'By' takes capitalized methods : ID, XPATH, LINK_TEXT, PARTIAL_LINK_TEXT, NAME, TAG_NAME, CLASS_NAME, CSS_SELECTOR
#             name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,        "name"    )))
autocompleteResult = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME,"pac-item")))
autocompleteResult.click()

# sleep 60 seconds to observe the result
print("Sleeping for visual inspection")
sleep(60)
driver.quit()
