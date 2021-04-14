import gspread, time
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(creds)

# open Google Sheets
# Create a new spreadsheet
# import/upload the local TextFieldInputs
# share it with client_email of the client_secret.json
sheet = client.open('TextFieldInputs').sheet1

#get the data from the spreadsheet
all_values = sheet.get_all_values()

#get the values we want out of the data
input_data = []
for row in all_values[1:]:
    input_data.append(row[1])

# use selenium to put that data in to the comment box
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome()
#driver = webdriver.Chrome(executable_path=chromedriver)
driver = webdriver.Chrome(executable_path='/Users/marco/PycharmProjects/ScriptingForTesters_TM/chromedriver')


driver.get('http://opensource.demo.orangehrmlive.com/index.php/leave/assignLeave')

def login(driver):
    user_name = driver.find_element_by_id('txtUsername')
    pwd = driver.find_element_by_id('txtPassword')

    user_name.send_keys('Admin')
    pwd.send_keys('admin')

    login_button = driver.find_element_by_id('btnLogin')
    login_button.click()

login(driver)

#set an employee
driver.find_element_by_id('assignleave_txtEmployee_empName').send_keys('John Smith')

#assign a leave type
leave_types = driver.find_element_by_id('assignleave_txtLeaveType')
leave_type_options = leave_types.find_elements_by_tag_name('option')

#get start and end date element
start_date = driver.find_element_by_id('assignleave_txtFromDate')
end_date = driver.find_element_by_id('assignleave_txtToDate')

#assign values to start and end date

#Send the input
for input_item in input_data:
    #get the comment element
    comment_text_area = driver.find_element_by_id('assignleave_txtComment')
    #get the assign button
    assign_button = driver.find_element_by_id('assignBtn')
    #send the input to the comment text area

