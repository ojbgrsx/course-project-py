print('Welcome!!!')


def director_menu():
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
    if menu <= 0 or menu > 8:
        print(' \n >>> YOU ENTER A NUMBER THAT IS NOT IN THE MENU, PLEASE TRY AGAIN!!! <<< \n ')
        director_menu()
    elif menu == 8:
        print(' \nThe program is over, we look forward to your return! \n ')


def manager_menu():
    print(' \n YOU ARE WELCOME MANAGER !!! \n ')
    print('1) Show list of employees ')
    # 1) Показывает список всех сотрудников
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
    elif menu == 7:
        print(' \nThe program is over, we look forward to your return! \n ')


def marketer_menu():
    print(' \n YOU ARE WELCOME MARKETER !!! \n ')
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
    if menu <= 0 or menu > 6:
        print(' \n >>> YOU ENTER A NUMBER THAT IS NOT IN THE MENU, PLEASE TRY AGAIN!!! <<< \n ')
        marketer_menu()
    elif menu == 6:
        print(' \nThe program is over, we look forward to your return! \n ')


def worker_menu():
    print(' \n YOU ARE WELCOME WORKER !!! \n ')
    print('1) Show a list of tasks assigned to me ')
    # 1) Показывает список порученных дел для этого сотрудника из файла “tasks.txt”
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
    if menu <= 0 or menu > 5:
        print(' \n >>> YOU ENTER A NUMBER THAT IS NOT IN THE MENU, PLEASE TRY AGAIN!!! <<< \n ')
        worker_menu()
    elif menu == 5:
        print(' \nThe program is over, we look forward to your return! \n ')


def account():
    print('Please choose type of your account: \n 1)Director \n 2)Manager \n 3)Marketing \n 4)Worker')
    a = int(input('Please enter a number (1-4) to log in, (0) to exit >>> '))
    print('')
    if a == 1:
        print('YOU ARE IN DIRECTOR ACCOUNT! \n')
        for i in range(3):
            direc_login = input('Enter username >>> ').lower()
            if direc_login == 'user-director':
                for j in range(3):
                    direc_password = input('Enter password >>> ').lower()
                    if direc_password == 'coolman':
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
            manager_login = input('Enter username >>> ').lower()
            if manager_login == 'user-manager':
                for j in range(3):
                    mana_password = input('Enter password >>> ').lower()
                    if mana_password == 'manager':
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
            market_login = input('Enter username >>> ').lower()
            if market_login == 'user-marketing':
                for j in range(3):
                    marketing_password = input('Enter password >>> ').lower()
                    if marketing_password == 'marketer':
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
            work_login = input('Enter username >>> ').lower()
            if work_login == 'user-worker':
                for j in range(3):
                    worker_password = input('Enter password >>> ').lower()
                    if worker_password == 'worker':
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


account()
