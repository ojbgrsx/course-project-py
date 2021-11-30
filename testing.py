from datetime import date
from google_api import *
from menus import *

name = 'akimaaly'
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
pprint(completed)
pprint(uncompleted)
print()
for qwerty in range(len(completed)):
    print(qwerty+1, completed[qwerty], end='')
print()
task.close()
task = open('tasks.txt', 'r', encoding='utf-8')
choosing = input('Please choose the work that you want to finish: ')
print()
perdun = completed[int(choosing)-1]

s = 'Done by {} : '.format(
    name.upper()) + perdun[12+len_name:-32] + ' >>> at {}\n'.format(datetime.datetime.now())
completed.append(s)
uncompleted.clear()
for k in task:
    if completed[int(choosing)-1] != k:
        uncompleted.append(k)
del completed[0:-1]
pprint(completed)
pprint(uncompleted)
task.close()

task = open('tasks.txt', 'w', encoding='utf-8')
task.writelines(uncompleted)
task.close()

complete = open('completed.txt', 'a', encoding='utf-8')
complete.writelines(completed)
complete.close()

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
