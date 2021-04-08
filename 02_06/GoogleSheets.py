import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(creds)
sheet = client.open('ServiceAccountTest').sheet1

sheet.update_cell(1,1,"test")
# https://gspread.readthedocs.io/en/latest/user-guide.html#getting-a-cell-value
print('row values: ',sheet.row_values(1))
print('call value: ', sheet.acell('A1').value)
print('cell coordinate value: ', sheet.cell(1,1).value)
print()
print(sheet.get_all_values())

my_data = [[1,2,3],[4,5,6]]

for row_index,row in enumerate(my_data):
    for col_index,value in enumerate(row):
        sheet.update_cell(row_index+1,col_index+1, value)