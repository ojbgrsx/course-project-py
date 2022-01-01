from googleapiclient.discovery import build
from google.oauth2 import service_account
from pprint import pprint
import datetime
import pandas as pd
import csv
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'key.json'
creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
id = '1cTg4QyIFSBJeQjuXk8dgJTTMpyGtzIPvkdz5Sd0wyhM'
service = build('sheets', 'v4', credentials=creds)
# Call the Sheets API
sheet = service.spreadsheets()
mains = sheet.values().get(spreadsheetId=id, range="mains!A1:B999").execute()
worker = sheet.values().get(spreadsheetId=id, range="worker!A2:B999").execute()
worker_with_username = sheet.values().get(
    spreadsheetId=id, range="worker!A1:C999").execute()
values_mains = mains.get('values', [])
values_worker = worker.get('values', [])
values_worker_with_username = worker_with_username.get('values', [])
##################### DELETING WORKERS #######################
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
############### REFRESHING BUDGET BY CLIENTS AT THE BEGGINING #########
# def sign_up_client():
#     print()
#     name = input('\nName: ')
#     surname = input('Surname: ')
#     district = input('District: ')
#     instagram = int(input('Instagram budget: '))
#     facebook = int(input('Facebook budget: '))
#     tiktok = int(input('TikTok budget: '))
#     print()
#     qwerty = [name, surname, district, instagram, facebook, tiktok]
#     with open('client.csv', mode='a') as csv_write:
#         cs = csv.writer(csv_write, delimiter=',')
#         cs.writerow(qwerty)
#     print('Congratulations. You have successfully signed up as CLIENT !!!\n')
# df = pd.read_csv('client.csv', delimiter=',')
# l = [['Instagram', "Facebook", "Telegram", 'Workers', 'All']]
# with open('budget.csv', mode='w') as f:
#     w = csv.writer(f)
#     all_bud = df['Instagram'].sum()+df['Facebook'].sum() + \
#         df['Telegram'].sum()
#     ins_bud = all_bud * 25 / 100
#     fac_bud = all_bud * 20 / 100
#     tel_bud = all_bud * 15 / 100
#     wor_bud = all_bud * 40 / 100
#     q = [ins_bud] + [fac_bud] + [tel_bud] + [wor_bud] + [all_bud]
#     l.append(q)
#     w.writerows(l)
