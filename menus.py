from google_api import *

i = len(values_worker_with_username) + 1


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
        show_workers = open('workers.txt', encoding="utf-8")
        print(show_workers.read())
        show_workers.close()
        if int(input('Any digit to continue, (0) to exit: ')) == 0:
            print()
        else:
            print('\nMANAGER MENU\n')
            manager_menu()
    elif menu == 2:
        mg_task = open("manager_task.txt")
        mg_task.read()
        mg_task.close()
        mg_task = open("manager_task.txt", 'a')
        t = input('Write the name of the case: >>>')
        t += '\n'
        mg_task.append(t)
        t.close()
        if int(input('Any digit to continue, (0) to exit: ')) == 0:
            print()
        else:
            print('\nMANAGER MENU\n')
            manager_menu()
    elif menu == 3:
        print()
        task = open('tasks.txt')
        print(task.read())
        task.close()
        if int(input('Any digit to continue, (0) to exit: ')) == 0:
            print()
        else:
            print('\nMANAGER MENU\n')
            manager_menu()
    elif menu == 4:

        if int(input('Any digit to continue, (0) to exit: ')) == 0:
            print()
        else:
            print('\nMANAGER MENU\n')
            manager_menu()
    elif menu == 5:

        if int(input('Any digit to continue, (0) to exit: ')) == 0:
            print()
        else:
            print('\nMANAGER MENU\n')
            manager_menu()
    elif menu == 6:
        print()
        show_workers = open('workers.txt', encoding="utf-8")
        print(show_workers.read())
        worker_name = input("Worker\'s name:>>> ").lower()
        s = ''

        if worker_name in (i[0] for i in values_worker):
            show_workers.close()
            worker_task = input("Worker\'s task:>>> ").lower()
            task = open('tasks.txt', 'a', encoding='utf-8')
            s = 'Work for {}'.format(worker_name.upper()) + \
                ' : ' + worker_task + ' >>> ' + \
                str(datetime.datetime.now()) + '\n'
            task.writelines(s)
            task.close()
        else:
            show_workers.close()
            print('We could not find account with the username {}'.format(
                worker_name.upper()))
        if int(input('Any digit to continue, (0) to exit: ')) == 0:
            print()
        else:
            print('\nMANAGER MENU\n')
            manager_menu()
    elif menu == 7:
        print(' \nThe program is over, we look forward to your return! \n ')


def marketer_menu():

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
        choosing = input('Please choose the work that you want to finish: ')
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
