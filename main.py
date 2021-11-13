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
print('   WELCOME !!!   ')


def account():
    i = len(values_worker) + 1
    have = input('Do you have an account ? (yes/no) \n').lower().strip()
    if have == 'yes':
        print('Please choose type of your account: \n 1)Director \n 2)Manager \n 3)Marketing \n 4)Worker')
        a = int(input('Please enter a number (1-4) to log in, (0) to exit >>> '))
        print('')
        if a == 1:
            print('YOU ARE IN DIRECTOR ACCOUNT! \n')
            for i in range(3):
                direc_login = input('Enter username >>> ').lower().strip()
                if direc_login in sheet.values().get(spreadsheetId=id, range="mains!A2").execute().get('values', [])[0]:
                    for j in range(3):
                        direc_password = input(
                            'Enter password >>> ').lower().strip()
                        if direc_password in sheet.values().get(spreadsheetId=id, range="mains!B2").execute().get('values', [])[0]:
                            director_menu()
                            break
                        else:
                            if j != 2:
                                print('Try again!!!')
                            else:
                                print('You have wasted all password attempts!!!')
                    break
                else:
                    if i != 2:
                        print('Try again!!!')
                    else:
                        print('You have wasted all username attempts!!!')
        elif a == 2:
            print('YOU ARE IN MANAGER ACCOUNT! \n')
            for i in range(3):
                manager_login = input('Enter username >>> ').lower().strip()
                if manager_login in sheet.values().get(spreadsheetId=id, range="mains!A3").execute().get('values', [])[0]:
                    for j in range(3):
                        mana_password = input(
                            'Enter password >>> ').lower().strip()
                        if mana_password in sheet.values().get(spreadsheetId=id, range="mains!B3").execute().get('values', [])[0]:
                            manager_menu()
                            break
                        else:
                            if j != 2:
                                print('Try again!!!')
                            else:
                                print('You have wasted all password attempts!!!')
                    break
                else:
                    if i != 2:
                        print('Try again!!!')
                    else:
                        print('You have wasted all username attempts!!!')
        elif a == 3:
            print('YOU ARE IN MARKETER ACCOUNT TYPE! \n')
            for i in range(3):
                market_login = input('Enter username >>> ').lower().strip()
                if market_login in sheet.values().get(spreadsheetId=id, range="mains!A4").execute().get('values', [])[0]:
                    for j in range(3):
                        marketing_password = input(
                            'Enter password >>> ').lower().strip()
                        if marketing_password in sheet.values().get(spreadsheetId=id, range="mains!B4").execute().get('values', [])[0]:
                            marketer_menu()
                            break
                        else:
                            if j != 2:
                                print('Try again!!!')
                            else:
                                print('You have wasted all password attempts!!!')
                    break
                else:
                    if i != 2:
                        print('Try again!!!')
                    else:
                        print('You have wasted all username attempts!!!')
        elif a == 4:
            print('YOU ARE IN WORKER ACCOUNT! \n')
            for i in range(3):
                work_login = input('Enter username >>> ').lower().strip()
                if [work_login] in sheet.values().get(spreadsheetId=id, range="worker!A2:A999").execute().get('values', []):
                    for check in sheet.values().get(spreadsheetId=id, range="worker!A2:B999").execute().get('values', []):
                        if work_login == check[0]:
                            for j in range(3):
                                worker_password = input('Enter password >>> ').lower().strip()
                                if worker_password == check[1]:
                                    worker_menu()
                                    break
                                else:
                                    if j != 2:
                                        print('\nWrong password')
                                        print('Try again!!!\n')
                                    else:
                                        print('\nYou have wasted all password attempts!!!')
                            break
                    break
                else:
                    if i != 2:
                        print('\nWe have not find account with this username!!!')
                        print('Try again!!!\n')
                    else:
                        print('\nYou have wasted all username attempts!!!')
        else:
            if a != 0:
                print(
                    ' >>> SORRY, BUT WE DID NOT FIND THIS TYPE OF ACCOUNT, PLEASE TRY AGAIN. <<< \n')
                account()
    elif have == 'no':
        print('Then you should sign up as worker')
        n, s = input().strip().lower(), input().strip().lower()
        l = [n, s]
        q = [l]
        print(q)
        sheet.values().update(spreadsheetId=id, range="worker!A{}".format(
            i), valueInputOption="USER_ENTERED", body={'values': [l]}).execute()
        print('Congratulations. You have successfully signed in !!! \n')
    else:
        print('Please try again!!!')
        account()


account()
