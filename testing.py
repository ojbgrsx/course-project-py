# from datetime import date
# from google_api import *
# from menus import *
# from manager_menu import *
from os import read
import pandas as pd
from pprint import pprint
import csv
l = []
l.append(0)
print(l)


df = pd.read_csv('workers.csv')
print(df.iloc[4:5])

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
