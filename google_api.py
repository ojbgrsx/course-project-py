from googleapiclient.discovery import build
from google.oauth2 import service_account
from pprint import pprint
import datetime

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'key.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
id = '1cTg4QyIFSBJeQjuXk8dgJTTMpyGtzIPvkdz5Sd0wyhM'
service = build('sheets', 'v4', credentials=creds)
# sheet_id = 1921119551
# Call the Sheets API
sheet = service.spreadsheets()
mains = sheet.values().get(spreadsheetId=id, range="mains!A1:B999").execute()
worker = sheet.values().get(spreadsheetId=id, range="worker!A2:B999").execute()
worker_with_username = sheet.values().get(
    spreadsheetId=id, range="worker!A1:B999").execute()
values_mains = mains.get('values', [])
values_worker = worker.get('values', [])
values_worker_with_username = worker_with_username.get('values', [])

# def deleting_worker():
#     which_worker = int(input())
#     request_body = {
#         "requests": [
#             {
#                 "deleteDimension": {
#                     'range': {
#                         'sheetId': sheet_id,
#                         'dimension': "ROWS",
#                         'startIndex': which_worker-1,
#                         'endIndex': which_worker
#                     }

#                 }
#             }
#         ]
#     }
#     sheet.batchUpdate(
#         spreadsheetId=id,
#         body=request_body
#     ).execute()
