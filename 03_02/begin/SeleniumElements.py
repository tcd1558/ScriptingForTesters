# webdriver is needed to start the browser driver e.g. chromedriver
from selenium import webdriver
# Add special characters, e.g. RETURN to control web pages
from selenium.webdriver.common.keys import Keys
# Add the sleep function
from time import sleep

#driver = webdriver.Chrome(executable_path='/Users/marco/PycharmProjects/ScriptingForTesters_TM/03_02/end/chromedriver')
driver = webdriver.Chrome(executable_path='/Users/marco/PycharmProjects/ScriptingForTesters_TM/chromedriver')

google_search_string ='www.seleniumhq.org'
driver.get('http://google.com')
element = driver.find_element_by_name('q')
element.send_keys(google_search_string)
element.send_keys(Keys.RETURN)

#element.find_element_by_xpath('//*[@id="rso"]/div[1]/div[1]/div/div[1]/a/h3/span')
#element.click()

link_elements = driver.find_elements_by_tag_name('a')
keep_looping=True
for link_element in link_elements:
    if keep_looping:
        href=link_element.get_attribute('href')
        if href and google_search_string in href:
            link_element.click()
            keep_looping=False
    else:
        break
sleep(15)

#driver.get('https://seleniumhq.org')
driver.get('https://www.selenium.dev/')


#element = driver.find_element_by_xpath('/html/body/section[2]/div/div[1]/div[1]/img' )
element = driver.find_element_by_xpath('/html/body/section[2]/div/div[1]/div[2]/a/div/b')
element.click()
#driver.back() # website has changed

search_element = driver.find_element_by_id('gsc-i-id1')
search_element.send_keys('webdriver')
search_element.send_keys(Keys.RETURN)

sleep(1)
driver.switch_to.frame('master-1')

link_elements = driver.find_elements_by_tag_name('a')
print(link_elements[0].get_attribute('href'))

# sleep 60 seconds to observe the result
sleep(60)
driver.quit()