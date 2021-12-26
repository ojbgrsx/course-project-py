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
        print()
        df = pd.read_csv('workers.csv')
        df.index += 1
        col = list(df.columns.values)
        print(df[[col[0]] + [col[2]]].loc[df['Name'] == name])
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


worker_menu(input())
