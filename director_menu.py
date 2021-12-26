from google_api import *
from main import account


def director_menu():
    df = pd.read_csv('client.csv', delimiter=',')
    bd = pd.read_csv('budget.csv')
    print(' \n YOU ARE WELCOME BOSS !!! \n ')
    print('1) Show a list of all customer coverage areas by district ')
    # 1) Показывает список районов с количеством клиентов
    print('2) Show list of budget categories ')
    # 2) Показывает категорию бюджета: бюджет для маркетинга, бюджет для заработной платы
    print('3) Show dedicated budget for a specific category of marketing sites ')
    # 3) Показывает список зон для маркетинга, а затем в зависимости от выбора показывается бюджет для маркетинга
    print('4) Show current marketing funds ')
    # 4) Показывает общие средства для маркетинга, в случае если маркетолог
    # потратил определенные средства на маркетинг, то понижаются и средства
    print('5) Show total budget required for salary ')
    # 5) Показывает общий бюджет для зарплаты, в случае повышение
    # зарплаты, увеличивается и бюджет, который необходим, в случае
    # если зарплата понижается, то понижается и требования для бюджет
    print('6) Increase the salary of an employee: ')
    # 6) Повышает зарплату сотрудника
    print('7) Lower the salary of an employee')
    # 7) Понижает зарплату сотрудника
    print('8) Exit ')
    # 8) Выход
    menu = int(input(
        ' \nPlease dial the menu number to work with the program, if finished, then dial 8: '))
    print()
    if menu == 1:
        print('\n1)Show clients in the Sverdlovskiy district')
        print('2)Show clients in Pervomaiskiy district')
        print("3)Show clients in Oktyabrskiy district")
        print("4)Show clients in Leninskiy district\n")
        print(f'Amount of all clients is: {len(df)}\n')
        q = int(input('\nPlease choose: '))
        print()
        df.index += 1
        if q == 1:
            sver = df[(df['District'] == 'sverdlovskiy')]
            print(sver, f'\n\nAmount of clients in this district: {len(sver)}')
        elif q == 2:
            per = df[(df['District'] == 'pervomaiskiy')]
            print(per, f'\n\nAmount of clients in this district: {len(per)}')
        elif q == 3:
            okt = df[(df['District'] == 'oktyabrskiy')]
            print(okt, f'\n\nAmount of clients in this district: {len(okt)}')
        elif q == 4:
            lns = df[(df['District'] == 'leninskiy')]
            print(lns, f'\n\nAmount of clients in this district: {len(lns)}')
        if input('\nAny character to continue, (0) to exit: ') == '0':
            print()
        else:
            print('\DIRECTOR MENU\n')
            director_menu()
    elif menu == 2:
        print('Budget for Marketing is: {}'.format(
            bd.loc[0, 'Instagram']+bd.loc[0, "Facebook"]+bd.loc[0, "Telegram"]))
        print('Budget for Salaries are: {}'.format(bd.loc[0, 'Workers']))
        if input('\nAny character to continue, (0) to exit: ') == '0':
            print()
        else:
            print('\nDIRECTOR MENU\n')
            director_menu()
    elif menu == 3:
        print('1) Instagram\n2) Facebook\n3) Telegram')
        promote = input('\nChoose a title: ')
        if promote == "1":
            print('\nBudget for Instagram: {}'.format(bd.iloc[0, 0]))
        elif promote == "2":
            print('\nBudget for Facebook: {}'.format(bd.iloc[0, 1]))
        elif promote == "3":
            print('\nBudget for Telegram: {}'.format(bd.iloc[0, 2]))
        else:
            pass
        if input('\nAny character to continue, (0) to exit: ') == '0':
            print()
        else:
            print('\nDIRECTOR MENU\n')
            director_menu()
    elif menu == 4:
        print('Current marketing medium: {}'.format(
            bd.loc[0, 'Instagram']+bd.loc[0, "Facebook"]+bd.loc[0, "Telegram"]))
        if input('\nAny character to continue, (0) to exit: ') == '0':
            print()
        else:
            print('\nDIRECTOR MENU\n')
            director_menu()
    elif menu == 5:
        print('Budget for Salaries are: {}'.format(bd.loc[0, 'Workers']))
        if input('\nAny character to continue, (0) to exit: ') == '0':
            print()
        else:
            print('\nDIRECTOR MENU\n')
            director_menu()
    elif menu == 6:
        wb = pd.read_csv('workers.csv')
        wb.index += 1
        print(wb, '\n')
        which = int(input(
            'Type the number of the employee you want to raise the salary: >>> '))
        summa = int(input('How much you want to increase: '))
        print()
        wb.iloc[which-1, 2] += summa
        bd.iloc[0, 3] += summa
        print(wb.iloc[which-1:which])
        wb.to_csv('workers.csv', index=False)
        bd.to_csv('budget.csv', index=False)
        if input('\nAny character to continue, (0) to exit: ') == '0':
            print()
        else:
            print('\nDIRECTOR MENU\n')
            director_menu()
    elif menu == 7:
        wb = pd.read_csv('workers.csv')
        wb.index += 1
        print(wb, '\n')
        which = int(input(
            'Type the number of the employee you want to raise the salary: >>> '))
        summa = int(input('How much you want to deccrease: '))
        print()
        wb.iloc[which-1, 2] -= summa
        bd.iloc[0, 3] -= summa
        print(wb.iloc[which-1:which])
        wb.to_csv('workers.csv', index=False)
        bd.to_csv('budget.csv', index=False)
        if input('\nAny character to continue, (0) to exit: ') == '0':
            print()
        else:
            print('\nDIRECTOR MENU\n')
            director_menu()
    elif menu <= 0 or menu > 9:
        print(' \n >>> YOU ENTER A NUMBER THAT IS NOT IN THE MENU, PLEASE TRY AGAIN!!! <<< \n ')
        director_menu()
    elif menu == 8:
        account()
    elif menu == 9:
        print(' \nThe program is over, we look forward to your return! \n ')


director_menu()
