import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from copy import deepcopy
from time import sleep
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

print()

pd_spreadsheet_data=pd.DataFrame(sheet.get_all_values())
cols=pd_spreadsheet_data.iloc[0]
idx=pd_spreadsheet_data.iloc[:,0]
# drop first row
pd_spreadsheet_data=pd_spreadsheet_data[1:]
pd_spreadsheet_data.columns=cols
pd_spreadsheet_data.set_index('Test Name', inplace=True) # The 'Test Name' needs to be a column header
pd_spreadsheet_data.name='pd_spreadsheet_data'
    # 0     col1    col2    col3
    # idx
    # ind0  a       b       c
    # ind1  a1      b1      c1
    #   What is the '0' above he index?
print("raw pd_spreadsheet:\n",pd_spreadsheet_data)
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

# Delete first and second column
print("trimmed pd_spreadsheet_data:")
pd_spreadsheet_frame=pd_spreadsheet_data.iloc[:,:1]
pd_spreadsheet_data=pd_spreadsheet_data.iloc[:,1:] # data[] all rows, iloc[rows, columns]
print('pd_spreadsheet_frame:\n', pd_spreadsheet_frame)
print('pd_spreadsheet_data:\n', pd_spreadsheet_data)
print()

print("----------------------------------------");
print("trimming - end")
print("----------------------------------------")


#read in csv data
csv_data = []
print("----------------------------------------");
print("read csv data file - start")
print("----------------------------------------")

# read with panda
df = pd.read_csv('LatestTestRunData.csv')
pd_csv_data = df.copy()
pd_csv_data.set_index('Test Name', inplace=True)
print('Pandas:\n',pd_csv_data)
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
TestRunDate=pd_csv_data.iloc[1,1]
print('Test run date: ', TestRunDate)

print("----------------------------------------");
print("retrieve date from csv_data - end")
print("----------------------------------------")

print("----------------------------------------");
print("check date in csv_data - start")
print("----------------------------------------")

#print(pd_csv_data.columns)
for test in pd_csv_data.index: # start from 2nd element, because column_to_add needs to include test 1, too.
    print('Checking Run Time for: ',test)
    #print(pd_csv_data.loc[test, 'Run Time'], TestRunDate)
    #print(pd_csv_data.loc[test, 'Run Date'], TestRunDate)
    #print(pd_csv_data.loc[test, 'Run Status'], TestRunDate)

    if pd_csv_data.loc[test,'Run Date'] != TestRunDate:
        print(test, "was run at a different date")
        print(pd_csv_data.loc[test, 'Run Date'], TestRunDate)
        exit(1)

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

print("Pandas slicing:")
print("row 1 only:\n", pd_csv_data[0:1]) # first line [zero to 1 excluding] is interpreted as header

print("Run Time column:\n ", pd_csv_data['Run Time'])
print()
pd_column_to_add=pd_csv_data['Run Time']
pd_column_to_add.name='Run Time'
#print("Cols:",pd_column_to_add.columns)
#pd_column_to_add.index=pd_column_to_add.index + 1   # ahift the index by 1
#pd_column_to_add.rename=TestRunDate                # Create an item at index 0
#pd_column_to_add=pd_column_to_add.sort_index()      # sort the index
print("pd_column_to_add:\n", pd_column_to_add)
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
CellG1=sheet.acell('G1').value # reduce sheet querries
print('CellG1: ',CellG1, '\nTestRunDate: ', TestRunDate)
if (CellG1 != TestRunDate):
    pd_spreadsheet_data=pd_spreadsheet_data.iloc[:,1:] # data[] all rows, iloc[rows, columns]
print("pd_spreadsheet_data:\n", pd_spreadsheet_data)
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

print("pandas")
print(pd_spreadsheet_data)
print(pd_column_to_add)

print()
print('CellG1: ',CellG1, '\nTestRunDate: ', TestRunDate)
if (CellG1 != TestRunDate):
    pd_spreadsheet_data[TestRunDate]=pd_column_to_add
#print(pd_spreadsheet_data.merge(pd_column_to_add, how='outer'))
print(pd_spreadsheet_data)

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

#CellG1=sheet.acell('G1').value # reduce sheet querries; done above.
#CellG1=sheet.cell(1,7).value # reduce sheet querries
print('CellG1: ',CellG1, '\nTestRunDate: ', TestRunDate)
pd_spreadsheet_data_rows=len(pd_spreadsheet_data)
print('Row count: ', pd_spreadsheet_data_rows)
pd_spreadsheet_data_columns=len(pd_spreadsheet_data.columns)
print('Column count: ', pd_spreadsheet_data_columns)

if (CellG1 != TestRunDate):
    sheet_row_index=1
    for col_index, value in enumerate(pd_spreadsheet_data.columns):
        sheet_col_index = col_index + 3
        #print("row: ", sheet_row_index, " column_index: ", sheet_col_index, " new value: ", col)
        sheet.update_cell(sheet_row_index, sheet_col_index, value) # if not restricted to only change once,
            # this might make you hit the daily quota limit
        print('.', end='')
        sleep(5)
    #print()

    for row_index,row in enumerate(pd_spreadsheet_data.index):
        for col_index,col in enumerate(pd_spreadsheet_data.columns):
            value=pd_spreadsheet_data.iloc[row_index,col_index]
            sheet_row_index = row_index + 2
            sheet_col_index = col_index + 3
            print("row: ", sheet_row_index, " column_index: ", sheet_col_index, " new value: ", value)
            sheet.update_cell(sheet_row_index, sheet_col_index, str(value)) # if not restricted to only change once,
                # this might make you hit the daily quota limit
            #print('.', end='')
            sleep(5)  # avoid to manny writes per time unit.
    print(' done\n')

selection=input('Proceed with Return ')
#print()

# Superfluous - Join spreadsheet_frame with spreadsheet_data
#           This step could be omitted, if the spreadsheet_data can be
#           manipulated without deleting columns

print('pandas:')
print()

# instead of re-adding the Average again, you might as well carry it all the way.
# just for the exercise. insert the average column
print('pd_spreadsheet_frame:\n', pd_spreadsheet_frame) # this is the old column 0 instead of the Average Run Time.
                                    # fix aabove

print('pd_spreadsheet_data:\n', pd_spreadsheet_data)
pd_spreadsheet_data.insert(0,'Average Run Time', pd_spreadsheet_frame)   # idx = 0
                # new_col = [7, 8, 9]  # can be a list, a Series, an array or a scalar
                # df.insert(loc=idx, column='A', value=new_col)
print('pd_spreadsheet_data after insert:\n', pd_spreadsheet_data)

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

print('final_spreadsheet:\n',pd_spreadsheet_data)

TestNames=pd_spreadsheet_data.index
print('Testnames 1:\n',TestNames)
#print('Testnames 2:\n',TestNames[1:])
#print(item[0] for item in final_spreadsheet)
for testVal, avg, TestName in zip(pd_column_to_add[:], avg_data[1:], TestNames):
#for testVal, avg, in zip(avg_data[1:], column_to_add[1:]):
    #print('testVal:',testVal,' avg: ',avg)
    table_data.append([TestName,testVal])
    print(float(avg), float(testVal))
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