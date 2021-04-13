Since SeleniumEssentialTraining uses Java, this is an exercise to recode it in Python.

The Java sources can be found under:
     /Users/marco/IdeaProjects/SeleniumEssentialTraining/src/

01_04
# This script opens a webdriver (Chrome) to access
# http://www.google.com and searches for 'Cheese!'
# Then it sleeps for 60 seconds and closes the browser

02_02
# This script opens a webdriver (Chrome) to access
# the test website https://formy-project.herokuapp.com
# enters a string and clicks on a button
# Then it sleeps for 60 seconds and closes the browser

02_03
# This script opens a webdriver (Chrome) to access
# the test website https://formy-project.herokuapp.com
# enters an address string and clicks the autocomplete option
# Then it sleeps for 60 seconds and closes the browser

02_04
# This script opens a webdriver (Chrome) to access
# the test website https://formy-project.herokuapp.com
# waits until a field becomes visible, moves to it and
# enters a string and a date
# Then it sleeps for 60 seconds and closes the browser
#   I believe this can be done more elegantly

02_05

04_05
# Reset button is not found
# selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":".btn\ btn-warning\ btn-reset"}
# resetButton = driver.find_element_by_class_name("btn btn-warning btn-reset")
# python does not support several classes. Use the following instead:
# resetButton = driver.find_element_by_css_selector("button.btn.btn-warning.btn-reset")

05_02 implicit wait
05_03 explicit wait

06_02
Autocomplete only seems to work for 1 field when dome manually
pac-item does not show up, when run in the chromedriver.

06_03
Check for success message and refactoring

07_04
access to saucelabs using java failed
Problem not solved



