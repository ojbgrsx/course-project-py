from google_api import *
from menus import *

name = 'akylbek'
splitted = []
unchanged = []
task = open('tasks.txt', 'r')
for k in task:
    if 'AKYLBEK' in k:
        s = ''
        s += k
        print(s, end='')
        unchanged.append(s)
        splitted.append(k.split())
print()
print(unchanged)
for i in splitted:
    del i[0:4]
    del i[-3::]

print(splitted)
# print('Please type the FIRST WORD of the work to COMPLETE\n')
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
