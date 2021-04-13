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
HTML='https://formy-project.herokuapp.com/form'

# Create a new instance of ChromeDriver
driver = webdriver.Chrome(executable_path=ChromeDriver)

# And now use the driver to open the google website
driver.get(HTML)

sleep(5) # takes time to load
# Find the text input element by its name
firstName = driver.find_element_by_id('first-name')

# 06_02 With Autocomplete
firstName.send_keys("Ravi")
firstName.click()

# sleep(10)
# autocompleteResult = driver.find_element_by_class_name('pac-item')
# autocompleteResult.click()
# Autocomplete only submits one field. The pac-item needs a implicit/explicit wait.
# The pac-item does not show up.

lastName = driver.find_element_by_id('last-name')
lastName.send_keys("Joshi")

jobTitle = driver.find_element_by_id('job-title')
jobTitle.send_keys("QA manager")

radioButton3 = driver.find_element_by_css_selector("input[value='radio-button-3']")
radioButton3.click()

checkbox1 = driver.find_element_by_id('checkbox-1')
checkbox1.click()

yearsOfExperience = driver.find_element_by_id("select-menu")
yearsOfExperience.click()

button = driver.find_element_by_xpath("//*[@id=\"select-menu\"]/option[5]")
button.click()

dateField = driver.find_element_by_id('datepicker')
dateField.click()
# Select today
myToday = driver.find_element_by_css_selector("td.today.day")
myToday.click()

# https://stackoverflow.com/questions/60534244/how-to-locate-an-element-with-multiple-classnames-using-selenium-and-python
submitButton = driver.find_element_by_css_selector("a.btn.btn-lg.btn-primary")
submitButton.click()

# sleep 60 seconds to observe the result
print("Sleeping for visual inspection")
sleep(60)
print("exiting ..")
driver.quit()
