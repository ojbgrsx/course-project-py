from googleapiclient.discovery import build
from google.oauth2 import service_account
from pprint import pprint

from googleapiclient.http import MediaIoBaseDownload
from menus import *

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'key.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
id = '1cTg4QyIFSBJeQjuXk8dgJTTMpyGtzIPvkdz5Sd0wyhM'
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
mains = sheet.values().get(spreadsheetId=id, range="mains!A1:C999").execute()
worker = sheet.values().get(spreadsheetId=id, range="worker!A1:C999").execute()
values_mains = mains.get('values', [])
values_worker = worker.get('values', [])

for i in range(3):
    work_login = input('Enter username >>> ').lower().strip()
    if [work_login] in sheet.values().get(spreadsheetId=id, range="worker!A2:A999").execute().get('values', []):
        for check in sheet.values().get(spreadsheetId=id, range="worker!A2:B999").execute().get('values', []):
            if work_login == check[0]:
                for j in range(3):
                    worker_password = input('Enter password >>> ').lower().strip()
                    if worker_password == check[1]:
                        print('Great')
                        break
                    else:
                        print('Wrong Password')
                break
        break
    else:
        print('We have not find account with this username!!!')