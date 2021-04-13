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
HTML='https://formy-project.herokuapp.com/radiobutton'

# Create a new instance of ChromeDriver
driver = webdriver.Chrome(executable_path=ChromeDriver)

# And now use the driver to open the google website
driver.get(HTML)

# Find the text input element by its name
Radiobutton1 = driver.find_element_by_id('radio-button-1')
Radiobutton2 = driver.find_element_by_css_selector("input[value='option2']")
Radiobutton3 = driver.find_element_by_xpath('/html/body/div/div[3]/input')

sleep(5)
Radiobutton2.click()
sleep(5)
Radiobutton3.click()
sleep(5)
Radiobutton1.click()
sleep(5)

HTML='https://formy-project.herokuapp.com/checkbox'
driver.get(HTML)

checkbox1 = driver.find_element_by_id('checkbox-1')
checkbox2 = driver.find_element_by_css_selector("input[value='checkbox-2']")
checkbox3 = driver.find_element_by_xpath("//*[@id=\"checkbox-3\"]")

sleep(5)
checkbox1.click()
sleep(5)
checkbox2.click()
sleep(5)
checkbox3.click()
sleep(5)
checkbox1.click()
sleep(5)
checkbox2.click()
sleep(5)
checkbox3.click()
sleep(5)

# sleep 60 seconds to observe the result
print("Sleeping for visual insprection")
sleep(60)
driver.quit()
