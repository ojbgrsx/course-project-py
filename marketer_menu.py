from google_api import *


def marketer_menu():
    bd = pd.read_csv('budget.csv')
    df = pd.read_csv('client.csv', delimiter=',')
    print('1) Show a list of all customer coverage areas by district ')
    # 1) Показывает количество людей - клиентов данной организации из файла «clients.txt»
    print('2) Show a list of categories for marketing')
    # 2) Показывает список мест для маркетинга, как пример это может быть Фейсбук, Инстаграм
    # и т.д. и количество пользователей того или иного приложения
    print('3) Show dedicated budget for a specific category of marketing sites ')
    # 3) Показывает список зон для маркетинга, а затем в зависимости от выбора показывается бюджет для маркетинга
    print('4) Show total budget for marketing ')
    # 4) Показывает общий бюджет маркетинга
    print('5) Spend your promotion budget ')
    # 5) Нужно выбрать название для продвижения: Instagram,Facebook,YouTube и т.д.
    print('6) Exit')
    # 6) Выход
    menu = int(input(
        ' \nPlease dial the menu number to work with the program, if finished, then dial 6: '))
    print()
    if menu == 1:
        print('\n1)Show clients in the Sverdlovskiy district')
        print('2)Show clients in Pervomaiskiy district')
        print("3)Show clients in Oktyabrskiy district")
        print("4)Show clients in Leninskiy district\n")
        print(f'Amount of all clients is: {len(df)}\n')
        q = input('\nPlease choose: ')
        print()
        df.index += 1
        if q == "1":
            sver = df[(df['District'] == 'sverdlovskiy')]
            print(sver, f'\n\nAmount of clients in this district: {len(sver)}')
        elif q == "2":
            per = df[(df['District'] == 'pervomaiskiy')]
            print(per, f'\n\nAmount of clients in this district: {len(per)}')
        elif q == "3":
            okt = df[(df['District'] == 'oktyabrskiy')]
            print(okt, f'\n\nAmount of clients in this district: {len(okt)}')
        elif q == "4":
            lns = df[(df['District'] == 'leninskiy')]
            print(lns, f'\n\nAmount of clients in this district: {len(lns)}')
        else:
            pass
        if input('\nAny character to continue, (0) to exit: ') == '0':
            print()
        else:
            print('\nMARKETER MENU\n')
            marketer_menu()
    elif menu == 2:
        print('1) Instagram Users Amount is: ',
              len(df.loc[df["Instagram"] != 0]))
        print('2) Facebook Users Amount is: ',
              len(df.loc[df["Facebook"] != 0]))
        print('3) Telegram Users Amount is: ',
              len(df.loc[df["Telegram"] != 0]))
        if input('\nAny character to continue, (0) to exit: ') == '0':
            print()
        else:
            print('\nMARKETER MENU\n')
            marketer_menu()
    elif menu == 3:
        print('1) Instagram\n2) Facebook\n3) Telegram')
        promote = input('\nChoose a title to promote: ')
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
            print('\nMARKETER MENU\n')
            marketer_menu()
    elif menu == 4:
        print('Market\'s total budget is: {}'.format(
            bd.iloc[0, 0:3].sum(axis=0)))
        if input('\nAny character to continue, (0) to exit: ') == '0':
            print()
        else:
            print('\nMARKETER MENU\n')
            marketer_menu()
    elif menu == 5:
        print('1) Instagram\n2) Facebook\n3) Telegram')
        promote = input('\nChoose a title to promote: ')
        outcome = int(
            input('Enter the amount of expense that you want to spend from the budget:'))
        if promote == '1' and outcome <= bd['Instagram'][0]:
            bd.loc[0, 'Instagram'] -= outcome
            bd.to_csv('budget.csv', index=False)
        elif promote == "2" and outcome <= bd['Facebook'][0]:
            bd.loc[0, 'Facebook'] -= outcome
            bd.to_csv('budget.csv', index=False)
        elif promote == "3" and outcome <= bd['Telegram'][0]:
            bd.loc[0, 'Telegram'] -= outcome
            bd.to_csv('budget.csv', index=False)
        else:
            pass
        if input('\nAny character to continue, (0) to exit: ') == '0':
            print()
        else:
            print('\nMARKETER MENU\n')
            marketer_menu()
    elif menu <= 0 or menu > 6:
        print(' \n >>> YOU ENTER A NUMBER THAT IS NOT IN THE MENU, PLEASE TRY AGAIN!!! <<< \n ')
        marketer_menu()
    elif menu == 6:
        print(' \nThe program is over, we look forward to your return! \n ')
