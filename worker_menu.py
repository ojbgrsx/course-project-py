from google_api import *


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
    print()
    if menu == 1:
        task = open('tasks.txt', 'r')
        for k in task:
            if name.upper() in k:
                print(k, end='')
        print()
        task.close()
        if input('Any character to continue, (0) to exit: ') == '0':
            print()
        else:
            print('\nWORKER MENU\n')
            worker_menu(name)
    elif menu == 2:
        splitted = []
        task = open('tasks.txt', 'r')
        for k in task:
            if name.upper() in k:
                print(k, end='')
                splitted.append(k.split())
        task.close()
        print()
        print(splitted)
        del splitted[0:4]
        del splitted[-3::]
        print(splitted)
        print('Please type the FIRST WORD of the work to COMPLETE\n')
        q = input()
        uncompleted = []
        completed = ['Done by {}: '.format(name.upper())]
        task = open('tasks.txt')
        for i in task:
            print(i.split()[2])
            if i.split()[2] == name and splitted[0] == q:
                completed.append(i)
                print(completed)
            else:
                uncompleted.append(i)
        task.close()
        completed.append(' >>> at {}\n'.format(datetime.datetime.now()))
        print(completed)
        print(uncompleted)
        # task = open("tasks.txt", 'w')
        # task.writelines(uncompleted[:])
        # task.close()
        # complete = open('completed.txt', 'a')
        # if len(completed) > 2:
        #     complete.writelines(completed[:])
        # complete.close()

        if input('Any character to continue, (0) to exit: ') == '0':
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
        if input('Any character to continue, (0) to exit: ') == '0':
            print()
        else:
            print('\nWORKER MENU\n')
            worker_menu(name)
    elif menu == 4:

        if input('Any character to continue, (0) to exit: ') == '0':
            print()
        else:
            print('\nWORKER MENU\n')
            worker_menu(name)
    elif menu <= 0 or menu > 5:
        print(' \n >>> YOU ENTER A NUMBER THAT IS NOT IN THE MENU, PLEASE TRY AGAIN!!! <<< \n ')
        worker_menu(name)
    elif menu == 5:
        print(' \nThe program is over, we look forward to your return! \n ')


worker_menu('AKYLBEK')
