from google_api import *


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
        if input('Any character to continue, (0) to exit: ') == '0':
            print()
        else:
            print('\nMANAGER MENU\n')
            manager_menu()
    elif menu == 2:

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

        if input('Any character to continue, (0) to exit: ') == '0':
            print()
        else:
            print('\nMANAGER MENU\n')
            manager_menu()
    elif menu == 5:

        if input('Any character to continue, (0) to exit: ') == '0':
            print()
        else:
            print('\nMANAGER MENU\n')
            manager_menu()
    elif menu == 6:
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
        if input('Any character to continue, (0) to exit: ') == '0':
            print()
        else:
            print('\nMANAGER MENU\n')
            manager_menu()
    elif menu == 7:
        print(' \nThe program is over, we look forward to your return! \n ')


manager_menu()