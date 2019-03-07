import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('WI-Input').sheet1

pp = pprint.PrettyPrinter()
owners = sheet.get_all_records()


def get_royalty_acres(list_data):
    x = [i['Acres'] * i['Royalty'] for i in list_data]
    return sum(x)


def get_total_acres(list_data):
    total_acres = 0
    for i in list_data:
        total_acres = total_acres + i['Acres']
    return total_acres




weighted_nri = get_royalty_acres(owners) / get_total_acres(owners)

row = owners[0]['Name'], get_total_acres(owners), weighted_nri
index = 10
sheet.insert_row(row, index)
