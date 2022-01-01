# from datetime import date
from pandas.io.parsers import read_csv
from google_api import *
# from menus import *
# from manager_menu import *
from os import name, read
import pandas as pd
from pprint import pprint
import csv

with open('client.csv') as f:
    df = read_csv('client.csv')
    reading = csv.reader(f)
    names = []
    surnames = []
    for i in reading:
        if i[0] != 'Name':
            names.append(i[0])
            surnames.append(i[1])
    print('YOU ARE IN CLIENT MENU! \n')
    for z in range(3):
        name = input('Enter name >>> ').lower().strip()
        if name in names:
            for j in range(3):
                surname = input('Enter surname >>> ').lower().strip()
                if surname in surnames:
                    print(df[(df['Name'] == name)])
                    break
                else:
                    if j != 2:
                        print('\nWrong surname')
                        print('Try again!!!\n')
                    else:
                        print(
                            '\nYou have wasted all password attempts!!!')
            break
        elif z != 2:
            print('\nWe have not find account with this name!!!')
            print('Try again!!!\n')
        else:
            print('\nYou have wasted all name attempts!!!')
            break

    # for asking in range(3):
    #     name = input('Please input your name: ')
    #     if
