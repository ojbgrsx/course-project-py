# from datetime import date
from google_api import *
# from menus import *
# from manager_menu import *
from os import read
import pandas as pd
from pprint import pprint
import csv


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


worker_menu("akylbek")
# instagram = int(input('Instagram budget: '))
# facebook = int(input('Facebook budget: '))
# tiktok = int(input('TikTok budget: '))
# qwerty = [name, surname, district, instagram, facebook, tiktok]
# with open('client.csv', mode='a') as csv_write:
#     cs = csv.writer(csv_write, delimiter=',')
#     cs.writerow(qwerty)


# non_active = 0
# with open("client.csv") as d:
#     d = csv.reader(d)
#     for i in d:
#         non_active += i.count("0")
#     print(non_active)
# print(df.loc[df['Name'] == 'Baiaaly'].loc[df['Instagram'] != 0])

# l = [['Market', 'Workers', 'All']]
# with open('budget.csv', mode='w') as f:
#     w = csv.writer(f)
#     df = pd.read_csv('client.csv')
#     all_bud = df['Instagram'].sum()+df['Facebook'].sum()+df['Telegram'].sum()
#     mar_bud = all_bud * 70 / 100
#     wor_bud = all_bud * 30 / 100
#     q = [mar_bud] + [wor_bud] + [all_bud]
#     l.append(q)
#     w.writerows(l)

# df.index += 1
# sver = df.loc[df['District'] == 'Sverdlovskiy']
# df['Total'] = df['Instagram'] + df['Facebook'] + df['TikTok']
# print(sver, f'\nAmount: {len(sver)}')
# print(df.sort_values(['Name']))

#
##################################
# pprint(field)
# for col in field:
#     print(col[1])
# with open('client.csv', mode='w') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=',')
#     for i in field:
#         i += ''
#         print(i)
#         csv_writer.writerow(i)
# # for row in csv_reader:
#     print(row)
# print(csv_reader.line_num)
#     if line_count == 0:
#         print(f'Column names are {", ".join(row)}')
#         line_count += 1
#     else:
#         print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#         line_count += 1
# print(f'Processed {line_count} lines.')
