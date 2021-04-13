# This script opens a webdriver (Chrome) to access
# the test website https://formy-project.herokuapp.com
# enters a string and clicks on a button
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
HTML='https://formy-project.herokuapp.com/switch-window'

# Create a new instance of ChromeDriver
driver = webdriver.Chrome(executable_path=ChromeDriver)

# And now use the driver to open the google website
driver.get(HTML)

# Find the text input element by its name
newTabButton = driver.find_element_by_id('new-tab-button')
#alertButton = driver.find_element_by_id('alert-button')

originalHandle=driver.current_window_handle
newTabButton.click()

for handle1 in driver.window_handles:
    driver.switch_to.window(handle1)
    sleep(5)

driver.switch_to.window(originalHandle)

# sleep 60 seconds to observe the result
print("Sleeping for visual insprection")
sleep(60)
driver.quit()
