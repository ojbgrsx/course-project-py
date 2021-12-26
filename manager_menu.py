from google_api import *
from main import account
df = pd.read_csv('client.csv', delimiter=',')
all_bud = df['Instagram'].sum()+df['Facebook'].sum() + \
    df['Telegram'].sum()
ins_bud = all_bud * 25 / 100
fac_bud = all_bud * 20 / 100
tel_bud = all_bud * 15 / 100
wor_bud = all_bud * 40 / 100


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
