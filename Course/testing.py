# from googleapiclient.discovery import build
# from google.oauth2 import service_account

# from googleapiclient.http import MediaIoBaseDownload
from os import name
from menus import *

# SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# SERVICE_ACCOUNT_FILE = 'key.json'

# creds = None
# creds = service_account.Credentials.from_service_account_file(
#     SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# # The ID and range of a sample spreadsheet.
# id = '1cTg4QyIFSBJeQjuXk8dgJTTMpyGtzIPvkdz5Sd0wyhM'
# service = build('sheets', 'v4', credentials=creds)

# # Call the Sheets API
# sheet = service.spreadsheets()
# mains = sheet.values().get(spreadsheetId=id, range="mains!A1:C999").execute()
# worker = sheet.values().get(spreadsheetId=id, range="worker!A1:C999").execute()
# values_mains = mains.get('values', [])
# values_worker = worker.get('values', [])
###############################
# q = input()
# uncompleted = []
# completed = ['Done by {}: '.format()]
# task = open('tasks.txt')
# for i in task:
#     if i.split()[0] == q:
#         completed.append(i)
#     else:
#         uncompleted.append(i)
# task.close()
# task = open("tasks.txt", 'w')
# task.writelines(uncompleted[:])
# task.close()
# complete = open('completed.txt', 'a')
# print(completed)
# complete.writelines(completed[:])
# complete.close()
###################################
# complete = open('completed.txt')
# print()
# for f in complete:
#     if 'AKYLBEK' in f:
#         print(f, end='')
# print()
# complete.close()

print(ord(input()))
