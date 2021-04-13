# This script opens a webdriver (Chrome) to access
# http://www.google.com and searches for 'Cheese!'
# Then it sleeps for 60 seconds and closes the browser

# webdriver is needed to start the browser driver e.g. chromedriver
from selenium import webdriver
# Add the sleep function
from time import sleep
# Add special characters, e.g. RETURN to control web pages
from selenium.webdriver.common.keys import Keys

# Set a variable where to find the chromedriver executable.
ChromeDriver='/Users/marco/PycharmProjects/ScriptingForTesters_TM/chromedriver'
HTML='http://www.google.com'

# Create a new instance of ChromeDriver
driver = webdriver.Chrome(executable_path=ChromeDriver)

# And now use the driver to open the google website
driver.get(HTML)

# Find the text input element by its name
element = driver.find_element_by_name('q')
# Enter something to search
element.send_keys('Cheese!')
# Execute the search by adding the RETURN key
element.send_keys(Keys.RETURN)

# sleep 60 seconds to observe the result
sleep(60)
driver.quit()
