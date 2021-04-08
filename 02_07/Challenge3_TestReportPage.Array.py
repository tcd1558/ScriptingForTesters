import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from copy import deepcopy
from time import sleep
import numpy as np      # https://stackoverflow.com/questions/3518778/how-do-i-read-csv-data-into-a-record-array-in-numpy
import pandas as pd     # panda  is for python2,
                        # pandas is for python3

scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('TestRunData').sheet1


#read in the data from the spreadsheet

print("----------------------------------------");
print("raw data - start")
print("----------------------------------------")

spreadsheet_data = sheet.get_all_values()
print("raw spreadsheet:\n",spreadsheet_data)
for row in spreadsheet_data:
    print(row)
print()

print("----------------------------------------");
print("raw data - end")
print("----------------------------------------")

print()

print("----------------------------------------");
print("Spreadsheet frame - start")
print("----------------------------------------")
# This was coded after the trimming section.
# This section can use the same code in reverse:
# remove all data.

spreadsheet_frame_rm=deepcopy(spreadsheet_data)
for row in spreadsheet_frame_rm:
    for i in range(len(row)-1, 1, -1):
        del row[i]
print('frame by removal:\n', spreadsheet_frame_rm)
print()

# You might as well just keep the first column. 'Average Run Time' is supposed to be a formula.

spreadsheet_frame_source=deepcopy(spreadsheet_data)
spreadsheet_frame_sel=[]
print('frame by selection:\n', spreadsheet_frame_source)
for row in spreadsheet_frame_source:
    #print(row[0], row[1])
    #print([row[0], row[1]])
    spreadsheet_frame_sel.append([row[0],row[1]]) # because row[0], row[1] are lists, it is going to be a shallow copy
print()
print(spreadsheet_frame_sel)

print("----------------------------------------");
print("Spreadsheet frame  - end")
print("----------------------------------------")

#a note to help you out here
#   We don't need the Test Name or Average Run Time
#   data, so we can remove those from each row using 
#   del row_data[x] where x is the index of the element
#   we want to remove
run_times = []

print("----------------------------------------");
print("trimming - start")
print("----------------------------------------")
print("trimmed spreadsheet_data")
for row in spreadsheet_data:
    #Remove the first 2 items from the row since we are not 
    #interested in the Test Name or Avg Run time
    del row[1]
    del row[0]
    print(row)
print()

print("----------------------------------------");
print("trimming - end")
print("----------------------------------------")


#read in csv data
csv_data = []
print("----------------------------------------");
print("read csv data file - start")
print("----------------------------------------")
print('csv.reader:')
with open('LatestTestRunData.csv') as csv_file:
    file_reader = csv.reader(csv_file)
    for row in file_reader:
        csv_data.append(row)
print(csv_data[1:])
# print in rows
print()
print("csv.reader - split between lists:")
for row in csv_data[1:]:
    print(row)
print()

print("----------------------------------------");
print("read csv data file - end")
print("----------------------------------------")



#for the sake of simplicity we are going to assume a few things:
# 1. All of the tests in the csv data were run on the same date
# 2. The test are in the same order in the csv file as they are in the 
#    spreadsheet data

#find the run date 
#remember that we can assume that all the tests in the csv file were run on the same date
#which means we can get the run date from the 3rd column of the 2nd row in the csv data

print("----------------------------------------");
print("retrieve date from csv_data - start")
print("----------------------------------------")

# Analysis of the new data
# - retrieve the date from the first test result
TestRunDate=csv_data[1][2]
print('Test run date: ', TestRunDate)

print("----------------------------------------");
print("retrieve date from csv_data - end")
print("----------------------------------------")

print("----------------------------------------");
print("check date in csv_data - start")
print("----------------------------------------")

# - now you could verify whether the date is the same for all tests
# for MyTestRunDate in
np_csv_data=np.array(csv_data)      # Instead of converting the array into a numpy, the csv_file should
                                    # be converted into a np-array
print('numpy: ', np_csv_data[1:,2]) # This syntax does not work for a list of lists
                                    # It has to be a numpy array
#print('zip: ', list(list(zip(*csv_data[1:]))[2]))
                                    # Without the list(list(zip)), TypeError: 'zip' object is not subscriptable
                                    # In Python3 zip returns an iterator, not list
                                    # Force the iterator into a list with list()
                                    # But the list return a tuple, and you want a list. So another list()
#print('list comprehensive: ', [el[2] for el in csv_data[1:]])

column_to_add=[TestRunDate]
for test in csv_data[1:]: # start from 2nd element, because column_to_add needs to include test 1, too.
    print('checking test: ',test)
    if test[2] != TestRunDate:
        print(result[0], "was run at a different date")
        exit(1)
    # add field 2 to column_to_add
    column_to_add.append(test[1])

print("----------------------------------------")
print("retrieve date in csv_data file - end")
print("----------------------------------------")

print()

print("----------------------------------------")
print("prepare data for spreadsheet - start")
print("----------------------------------------")

# - sort the results in a list
#   - Date - goes into position 0
#   - Test 1 - goes into position 1
#   - Test 2 - goes into position 2
#    ...
#   - Test 10 - goes into position 10
#

print("csv_read:\n",column_to_add)
print()

run_date = TestRunDate

print("----------------------------------------")
print("prepare data for spreadsheet - end")
print("----------------------------------------")

print()

print("----------------------------------------")
print("remove old column in  spreadsheet - start")
print("----------------------------------------")

#now get the first row of the run_times list and modify it to remove the oldest value
#and add in the new run date

# from spreadsheet[[row0],[row1],[row2],..], delete first run time column
# from all row# lists, pop or delete item 0
print("spreadsheet_data w/ 03/01/2018:\n", spreadsheet_data)
for row in spreadsheet_data:
    del row[0]
    print(row)
print("spreadsheet_data w/o 03/01/2018:\n", spreadsheet_data)
print()

print("----------------------------------------")
print("remove old column in spreadsheet - end")
print("----------------------------------------")

print()

print("----------------------------------------")
print("append new column in spreadsheet - start")
print("----------------------------------------")

#similar to above, do this for each remaining row
#loop over the run_times and csv_data lists and for each time through the loop,
#get the new value from the csv_data and add it to the end of the run_times row
#and then remove the oldest value from that row
#note that you can use zip to iterate over multiple lists at the same time
#for spreadsheet_row,csv_row in zip(run_times[1:],csv_data[1:]):

# run_times is the remaining data in the spreadsheet_data
# csv_data is the column_to_add

new_spreadsheet_data=[]
for spreadsheet_row, csv_row in zip(spreadsheet_data[:], column_to_add[:]):
    #print("zipping:", spreadsheet_row, csv_row)
    # Append csv_row to spreadsheet_row
    spreadsheet_row.append(csv_row)
    new_spreadsheet_data.append(spreadsheet_row)
    print(spreadsheet_row)

print("----------------------------------------")
print("append new column in spreadsheet - end")
print("----------------------------------------")

print()

print("----------------------------------------")
print("write back spreadsheet - start")
print("----------------------------------------")

# Write the new spreadsheet data back into the spreadsheet
#   sheet.update_cell(row_index+1,col_index+1, value)

# Don't forget that lists are indexed starting from 0 and the
# spreadsheet index starts at 1.
#    sheet.update_cell(row_index+1,col_index+1, value)  # hence the 'index+1'

# Also remember that we want to start writing the data in the
# 3rd column in the spreadsheet since the first two columns have
# the test name and the average run time.
#    sheet.update_cell(row_index+3,col_index+3, value)  # hence the 'index+1' and another +2

# As a reminder, if you want both the value and the index
# of a list you can use the enumerate function

CellG1=sheet.acell('G1').value # reduce sheet querries
#CellG1=sheet.cell(1,7).value # reduce sheet querries
print('CellG1: ',CellG1, '\nTestRunDate: ', TestRunDate)
print('Array method')
for row_index,row in enumerate(new_spreadsheet_data):
    for col_index,value in enumerate(row):
        if (CellG1 != TestRunDate):
                        #print("How do you undo the changes?")
                            # Check course video.
                            # The csv file is import into google sheets manually
                            # and shared with an automation account
                            # The Average Run Time has to be replaced with a function.
                            # =Average(C2:G2)
            sheet_row_index=row_index+1
            sheet_col_index=col_index+3
            #print("row: ", sheet_row_index, " column_index: ", sheet_col_index, " new value: ", value)
            #print('cell coordinate old value: ', sheet.cell(sheet_row_index, sheet_col_index).value)
                                # to avoid hitting the daily quota limit, it is better to read the line once
                                # and work with the line values.
            #print()
            sheet.update_cell(sheet_row_index, sheet_col_index, value) # if not restricted to only change once,
                                    # this might make you hit the daily quota limit
            print('.',end='')
            sleep(5) # avoid to manny writes per time unit.

print(' done\n')
#selection=input('Proceed with Return ')
#print()

# Superfluous - Join spreadsheet_frame with spreadsheet_data
#           This step could be omitted, if the spreadsheet_data can be
#           manipulated without deleting columns

print("array")
spreadsheet_frame=deepcopy(spreadsheet_frame_rm)
print("zipping spreadsheet_frame, new_spreadsheet_data:")
final_spreadsheet=[]
for frame,data in zip(spreadsheet_frame,new_spreadsheet_data):
    print(frame,data)
    for result in data:
        frame.append(result)
    final_spreadsheet.append(frame)

print('final_spreadsheet:\n',final_spreadsheet)
for row in final_spreadsheet:
    print(row)

print("----------------------------------------")
print("write back spreadsheet - end")
print("----------------------------------------")

print()

print("----------------------------------------")
print("Creating Chart - start")
print("----------------------------------------")
# read in the average data from the spreadsheet
# Hint: use sheet.col_values
# avg_data = []
avg_data=sheet.col_values(2)

print('avg_data:\n',avg_data)

# intializing the chart_data list with the headers
chart_data = [["Test Name","Diff From Avg"]]
print('chart_data:\n',chart_data)
table_data = [["Test Name","Run Time (s)"]]
print('table_data:\n',table_data)

# add test names and the difference from the average for each
# of the test to the chart_data list
# hint: use zip again to loop over both the avg_data and the
# csv_data lists at the same time

# The resulting graph has one result for each Test.
# Avg Test 1 - latest Test 1 result = -5.2
# 2 - -3.8
# 3 - -2.2
# 4 - +5.2
# 5 + 11.4
# 6 - -7
# 7 - -0.2
# 8 - -4.6
# 9 - -3.8
# 10 - +1.2
# The actual result is the opposite value. Meaning: test result - average

print('final_spreadsheet:\n',final_spreadsheet)

TestNames=[]
for row in final_spreadsheet:
    TestNames.append(row[0])
print('Testnames 1:\n',TestNames)
print('Testnames 2:\n',TestNames[1:])
#print(item[0] for item in final_spreadsheet)
for testVal, avg, TestName in zip(column_to_add[1:], avg_data[1:], TestNames[1:]):
#for testVal, avg, in zip(avg_data[1:], column_to_add[1:]):
    #print('testVal:',testVal,' avg: ',avg)
    table_data.append([TestName,testVal])
    DiffFromAvg=float(avg)-float(testVal)
    chart_data.append([TestName,DiffFromAvg])
    print(TestName, DiffFromAvg) # get TestName from final_spreadsheet or spreadsheet_frame

print('Table Data:\n',table_data)
print('Chart Data:\n',chart_data)
#print("Exit here")
#exit(0)

from string import Template
# first substitution is the header, the rest is the data
htmlString = Template("""<html><head><script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
  google.charts.load('current', {packages: ['corechart']});
  google.charts.setOnLoadCallback(drawChart);
  
  function drawChart(){
      var data = google.visualization.arrayToDataTable([
      $labels,
      $data
      ],
      false);

      var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
      chart.draw(data);
  }
</script>
</head>
<body>
<div id = 'chart_div' style='width:800; height:600'><div>
</body>

</html>""")

#format the data correctly
chart_data_str = ''
for row in chart_data[1:]:
    chart_data_str += '%s, \n' % row

#Substitute the data into the template
completed_html = htmlString.substitute(labels=chart_data[0], data=chart_data_str)

#Write the html to a file
with open('Chart.html','w') as f:
    f.write(completed_html)

print("----------------------------------------")
print("Creating Chart - end")
print("----------------------------------------")