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
HTML='https://formy-project.herokuapp.com/fileupload'

# Create a new instance of ChromeDriver
driver = webdriver.Chrome(executable_path=ChromeDriver)

# And now use the driver to open the google website
driver.get(HTML)

sleep(5) # takes time to load
# Find the text input element by its name
fileUploadField = driver.find_element_by_id('file-upload-field')
# resetButton = driver.find_element_by_class_name("btn btn-warning btn-reset")
# remember that a class starts with a '.'
# resetButton = driver.find_element_by_class_name(".btn.btn-warning.btn-reset")
# resetButton = driver.find_element_by_class_name(".btn .btn-warning .btn-reset")
# https://stackoverflow.com/questions/60534244/how-to-locate-an-element-with-multiple-classnames-using-selenium-and-python
resetButton = driver.find_element_by_css_selector("button.btn.btn-warning.btn-reset")
#/html/body/div/form/div/div/span[2]/button
#driver.find_element_by_xpath("/html/body/div/form/div/div/span[2]/button[@class='btn btn-warning btn-reset']")
fileUploadField.send_keys("file-to-upload.png")
sleep(5)
resetButton.click()
sleep(5)

#chooseButton=driver.find_element_by_class_name("btn btn-secondary btn-choose")
chooseButton=driver.find_element_by_css_selector("button.btn.btn-secondary.btn-choose")
chooseButton.click()

# sleep 60 seconds to observe the result
print("Sleeping for visual inspection")
sleep(60)
driver.quit()
