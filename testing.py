# from datetime import date
# from google_api import *
# from menus import *
# from manager_menu import *
from os import name
from pprint import pprint
import csv
field = []
name = input('Name: ')
district = input('District: ')
instagram = int(input('Instagram budget: '))
facebook = int(input('Facebook budget: '))
tiktok = int(input('TikTok budget: '))
qwerty = [name, district, instagram, facebook, tiktok]
with open("client.csv") as f:
    r = csv.reader(f, delimiter="\t")
    next(r)
    for row in r:
        print(row)
        field.append(row)
    field.append(qwerty)
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


# name = 'akimaaly'
# len_name = len(name)
# completed = []
# uncompleted = []
# task = open('tasks.txt', 'r')
# print()
# for k in task:
#     s = ''
#     s += k
#     if name.upper() in k:
#         completed.append(s)
#     else:
#         uncompleted.append(s)
# pprint(completed)
# pprint(uncompleted)
# print()
# for qwerty in range(len(completed)):
#     print(qwerty+1, completed[qwerty], end='')
# print()
# task.close()
# task = open('tasks.txt', 'r', encoding='utf-8')
# choosing = input('Please choose the work that you want to finish: ')
# print()
# perdun = completed[int(choosing)-1]

# s = 'Done by {} : '.format(
#     name.upper()) + perdun[12+len_name:-32] + ' >>> at {}\n'.format(datetime.datetime.now())
# completed.append(s)
# uncompleted.clear()
# for k in task:
#     if completed[int(choosing)-1] != k:
#         uncompleted.append(k)
# del completed[0:-1]
# pprint(completed)
# pprint(uncompleted)
# task.close()

# task = open('tasks.txt', 'w', encoding='utf-8')
# task.writelines(uncompleted)
# task.close()

# complete = open('completed.txt', 'a', encoding='utf-8')
# complete.writelines(completed)
# complete.close()

# q = input()
# uncompleted = []
# completed = ['Done by {}: '.format(name.upper())]

# for i in :
#     print(i.split()[2])
#     if i.split()[2] == name.upper() and splitted[0] == q:
#         completed.append(i)
#         print(completed)
#     else:
#         uncompleted.append(i)

# completed.append(' >>> at {}\n'.format(datetime.datetime.now()))
# print(completed)
# print(uncompleted)
# task = open("tasks.txt", 'w')
# task.writelines(uncompleted[:])
# task.close()
# complete = open('completed.txt', 'a')
# if len(completed) > 2:
#     complete.writelines(completed[:])
# complete.close()
