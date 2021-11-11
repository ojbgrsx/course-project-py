from googleapiclient.discovery import build
from google.oauth2 import service_account


def account():
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
                if work_login in sheet.values().get(spreadsheetId=id, range="worker!A5").execute().get('values', [])[0]:
                    for j in range(3):
                        worker_password = input(
                            'Enter password >>> ').lower().strip()
                        if worker_password in sheet.values().get(spreadsheetId=id, range="worker!B5").execute().get('values', [])[0]:
                            worker_menu()
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
        else:
            if a != 0:
                print(
                    ' >>> SORRY, BUT WE DID NOT FIND THIS TYPE OF ACCOUNT, PLEASE TRY AGAIN. <<< \n')
                account()
    elif have == 'no':
        print('Then you should sign up')
        print('1)Worker')
        n = input().strip()
        s = input().strip()
        i = len(values) + 1
        l = list(n, s)
        q = [l]
        print(q)
        send = sheet.values().update(spreadsheetId=id, range="mains!A{}".format(
            i), valueInputOption="USER_ENTERED", body={'values': [l]}).execute()
        print('Congratulations. You have successfully signed in !!!')
    else:
        print('Please try again!!!')
        account()