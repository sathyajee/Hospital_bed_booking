import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope=["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds=ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client=gspread.authorize(creds)
sheet=client.open("Bed_Booking_Form").sheet1
data=sheet.get_all_records()
#row=sheet.row_values(1)

cell=sheet.cell(2,9).value

#sheet.update_cell(2,2,"change")
#len(data)--> no. of rows
print(len(data))

