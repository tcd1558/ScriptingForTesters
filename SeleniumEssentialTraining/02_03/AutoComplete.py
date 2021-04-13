# This script opens a webdriver (Chrome) to access
# the test website https://formy-project.herokuapp.com
# enters an address string and clicks the autocomplete option
# Then it sleeps for 60 seconds and closes the browser

# webdriver is needed to start the browser driver e.g. chromedriver
from selenium import webdriver
# Add the sleep function
from time import sleep
# Add special characters, e.g. RETURN to control web pages
from selenium.webdriver.common.keys import Keys

# Set a variable where to find the chromedriver executable.
ChromeDriver='/Users/marco/PycharmProjects/ScriptingForTesters_TM/chromedriver'
HTML='https://formy-project.herokuapp.com/autocomplete'

# Create a new instance of ChromeDriver
driver = webdriver.Chrome(executable_path=ChromeDriver)

# And now use the driver to open the google website
driver.get(HTML)

# Find the text input element by its name
autocomplete = driver.find_element_by_id('autocomplete')
# autocomplete.send_keys('1558 Timber Creek Drive, San')
autocomplete.send_keys('1555 Park Blvd, Palo Alto')
sleep(1)
autocompleteResult = driver.find_element_by_class_name('pac-item')
autocompleteResult.click()

# sleep 60 seconds to observe the result
sleep(60)
driver.quit()
