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
