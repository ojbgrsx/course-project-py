from google_api import *
i = len(values_worker_with_username) + 1
df = pd.read_csv('client.csv', delimiter=',')
all_bud = df['Instagram'].sum()+df['Facebook'].sum() + \
    df['Telegram'].sum()
ins_bud = all_bud * 25 / 100
fac_bud = all_bud * 20 / 100
tel_bud = all_bud * 15 / 100
wor_bud = all_bud * 40 / 100

######## DIRECTOR MENU ########


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
        print(' \nThe program is over, we look forward to your return! \n ')

######## MANAGER MENU ########


def manager_menu():
    df = pd.read_csv('client.csv', delimiter=',')
    print('1) Show list of employees ')
    print('2) Show to-do list ')
    # 2) Показывает список всех дел, которую необходимо выполнить
    print('3) Show a list of instructions to employees ')
    # 3) Показывает список всех указаний по сотрудникам
    print('4) Show a list of all customer coverage areas by district ')
    # 4) Показывает количество людей - клиентов данной организации
    print('5) Calculate ')
    # 5) Тут есть подменю
    print('6) Give an assignment to employees ')
    # 6) Пишется в отдельный файл «tasks.txt» имя сотрудника и название задания,
    # где помимо всего прочего указывается и дата задания с помощью библиотеки datetime)
    print('7) Exit ')
    # 7) Выход
    menu = int(input(
        ' \nPlease dial the menu number to work with the program, if finished, then dial 7: '))
    if menu <= 0 or menu > 7:
        print(' \n >>> YOU ENTER A NUMBER THAT IS NOT IN THE MENU, PLEASE TRY AGAIN!!! <<< \n ')
        manager_menu()
    elif menu == 1:
        print()
        df = pd.read_csv('workers.csv')
        df.index += 1
        print(df['Name'])
        print()
        if input('Any character to continue, (0) to exit: ') == '0':
            print()
        else:
            print('\nMANAGER MENU\n')
            manager_menu()
    elif menu == 2:
        mg_task = open("manager_task.txt")
        print()
        print(mg_task.read())
        mg_task.close()
        mg_t = open("manager_task.txt", 'a+')
        t = input('Write the name of the case: >>>')
        t += '\n'
        mg_t.writelines(t)
        mg_t.close()
        if input('Any character to continue, (0) to exit: ') == '0':
            print()
        else:
            print('\nMANAGER MENU\n')
            manager_menu()
    elif menu == 3:
        print()
        task = open('tasks.txt')
        print(task.read())
        task.close()
        if input('Any character to continue, (0) to exit: ') == '0':
            print()
        else:
            print('\nMANAGER MENU\n')
            manager_menu()
    elif menu == 4:
        print()
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
            print('\nMANAGER MENU\n')
            manager_menu()
    elif menu == 5:
        print()
        print('1) The total contribution of all clients')
        print('2) Average contribution of all clients')
        print('3) Calculate the total income from the search for clients:')
        q = int(input('\nChoose the option: '))
        if q == 1:
            print('\nThe total contribution of all clients is: ', all_bud)
        elif q == 2:
            print('\nAverage income of all clients is : ', all_bud / len(df))
        elif q == 3:
            print(df)
            name = input(
                '\nEnter the name of the person to calculate the total and average contribution >>> ')
            print()
            non_active = 0
            with open("client.csv") as d:
                d = csv.reader(d)
                for i in d:
                    if name in i:
                        non_active += i.count("0")
            df['Total'] = df.iloc[:, 3:7].sum(axis=1)
            df['Average'] = round(
                (df.iloc[:, 3:7].sum(axis=1)/(3-non_active)))
            print(df.loc[df['Name'] == name]
                  [['Name', 'Surname', 'District', 'Total', 'Average']])
            print()
        if input('\nAny character to continue, (0) to exit: ') == '0':
            print()
        else:
            print('\nMANAGER MENU\n')
            manager_menu()
    elif menu == 6:
        show_workers = pd.read_csv('workers.csv')
        print(show_workers["Name"])
        worker_name = input("Worker\'s name:>>> ").lower()
        s = ''

        if worker_name in (i[0] for i in values_worker):
            worker_task = input("Worker\'s task:>>> ").lower()
            task = open('tasks.txt', 'a', encoding='utf-8')
            s = 'Work for {}'.format(worker_name.upper()) + \
                ' : ' + worker_task + ' >>> ' + \
                str(datetime.datetime.now()) + '\n'
            task.writelines(s)
            task.close()
        else:
            print('We could not find account with the username {}'.format(
                worker_name.upper()))
        if input('Any character to continue, (0) to exit: ') == '0':
            print()
        else:
            print('\nMANAGER MENU\n')
            manager_menu()
    elif menu == 7:
        print(' \nThe program is over, we look forward to your return! \n ')

######## MARKETER MENU ########


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

######## WORKER MENU ########


def worker_menu(name):
    print('1) Show a list of tasks assigned to me ')
    print('2) Complete the case:')
    # 2) Здесь пишется название дела, которую собирается выполнить сотрудник.
    # После того, как сотрудник ввел название дело, которую сотрудник хочет выполнить,
    # то это дело автоматически удаляется из файла “tasks.txt” и одновременно записывается в файл
    # “completed-tasks.txt” с указанием имени сотрудника и название дела
    print('3) Show list of completed instructions ')
    # 3) Показывает список завершенных дел для этого сотрудника из файла “completed-tasks.txt”
    print('4) Show salary ')
    # 4) Показывается текущая зарплата для этого сотрудника из файла “salary.txt”
    print('5) Exit')
    # 5) Выход

    menu = int(input(
        ' \nPlease dial the menu number to work with the program, if finished, then dial 5: '))
    if menu == 1:
        print()
        f = open('tasks.txt', 'r')
        for t in f:
            if name.upper() in t:
                print(t, end='')
        print()
        if int(input('Any digit to continue, (0) to exit: ')) == 0:
            print()
        else:
            print('\nWORKER MENU\n')
            worker_menu(name)
    elif menu == 2:
        len_name = len(name)
        completed = []
        uncompleted = []
        task = open('tasks.txt', 'r')
        print()
        for k in task:
            s = ''
            s += k
            if name.upper() in k:
                completed.append(s)
            else:
                uncompleted.append(s)
        print()
        for qwerty in range(len(completed)):
            print(qwerty + 1, completed[qwerty], end='')
        print()
        task.close()
        choosing = input(
            'Please choose the work that you want to finish, (0) or ENTER to exit: ')
        if choosing != '0' and choosing != '':
            task = open('tasks.txt', 'r', encoding='utf-8')
            print()
            perdun = completed[int(choosing) - 1]

            s = 'Done by {} : '.format(
                name.upper()) + perdun[12 + len_name:-32] + ' >>> at {}\n'.format(datetime.datetime.now())
            completed.append(s)
            uncompleted.clear()
            for k in task:
                if completed[int(choosing) - 1] != k:
                    uncompleted.append(k)
            del completed[0:-1]
            task.close()

            task = open('tasks.txt', 'w', encoding='utf-8')
            task.writelines(uncompleted)
            task.close()

            complete = open('completed.txt', 'a', encoding='utf-8')
            complete.writelines(completed)
            complete.close()
        else:
            pass
        if int(input('Any digit to continue, (0) to exit: ')) == 0:
            print()
        else:
            print('\nWORKER MENU\n')
            worker_menu(name)
    elif menu == 3:
        complete = open('completed.txt')
        print()
        for f in complete:
            if name.upper() in f:
                print(f, end='')
        print()
        complete.close()
        if int(input('Any digit to continue, (0) to exit: ')) == 0:
            print()
        else:
            print('\nWORKER MENU\n')
            worker_menu(name)
    elif menu == 4:
        print()
        df = pd.read_csv('workers.csv')
        df.index += 1
        col = list(df.columns.values)
        sal = df[col[2]].loc[df['Name'] == name]
        print('Your salary is: {}'.format(sal.iloc[0]))
        print()
        if int(input('Any digit to continue, (0) to exit: ')) == 0:
            print()
        else:
            print('\nWORKER MENU\n')
            worker_menu(name)
    elif menu <= 0 or menu > 5:
        print(' \n >>> YOU ENTER A NUMBER THAT IS NOT IN THE MENU, PLEASE TRY AGAIN!!! <<< \n ')
        worker_menu(name)
    elif menu == 5:
        print(' \nThe program is over, we look forward to your return! \n ')
