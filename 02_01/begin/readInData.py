import csv

#final desired format
# - Charts [["Test Name",<diff from avg>]]
# - spreadsheet [["Test Name",<current run time>]]

timing_data = []
with open('TestTimingData.csv') as csv_file:
    file_reader = csv.reader(csv_file)
    for row in file_reader:
        timing_data.append(row)

# The data set timing_data includes the test name, run time, and the average run time for this test.
# Create 2 new data sets;
# A data set table_data with the test name and the run time
# A data set column_chart_data with the test name and the run time difference from the average

# Define the headers for
# column_chart_data and table_data
column_chart_data= [["Test Name", "Diff from Avg"]]
table_data = [["Test Name", "Run Time (s)"]]

for row in timing_data[1:]:
    test_name = row[0]
    if not row[1] or not row[2]:
        continue
    current_run_time = float(row[1])
    avg_run_time = float(row[2])
    print("Test Name", "current_run_time", "avg_run_time")
    print(test_name, current_run_time, avg_run_time)

    diff_from_avg = avg_run_time - current_run_time
    column_chart_data.append([test_name, diff_from_avg])
    table_data.append([test_name,current_run_time])

print(column_chart_data)
print(table_data)
