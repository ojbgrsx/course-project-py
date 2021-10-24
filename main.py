print('Welcome!!!')


def director_menu():
    print('YOU ARE WELCOME BOSS !!!')


def manager_menu():
    print('YOU ARE WELCOME MANAGER !!!')


def marketer_menu():
    print('YOU ARE WELCOME MARKETER !!!')


def worker_menu():
    print('YOU ARE WELCOME WORKER !!!')


def account():
    print('Please choose type of your account: \n 1)Director \n 2)Manager \n 3)Marketing \n 4)Worker')
    a = int(input('Please enter a number (1-4) to log in, (0) to exit >>> '))
    print('')
    if a == 1:
        print('YOU ARE IN DIRECTOR ACCOUNT! \n')
        director_login = 'user-director'
        director_password = 'coolman'
        for i in range(3):
            direc_login = input('Enter username >>> ').lower()
            if direc_login == director_login:
                for j in range(3):
                    direc_password = input('Enter password >>> ').lower()
                    if direc_password == director_password:
                        director_menu()
                        break
                    else:
                        if j != 2:
                            print('Try again!!!')
                        else:
                            print('You have wasted all password attempts!!!')
                break
            else:
                if i != 2:
                    print('Try again!!!')
                else:
                    print('You have wasted all username attempts!!!')
    elif a == 2:
        print('YOU ARE IN MANAGER ACCOUNT! \n')
        mana_login = 'user-manager'
        manager_password = 'manager'
        for i in range(3):
            manager_login = input('Enter username >>> ').lower()
            if mana_login == manager_login:
                for j in range(3):
                    mana_password = input('Enter password >>> ').lower()
                    if mana_password == manager_password:
                        manager_menu()
                        break
                    else:
                        if j != 2:
                            print('Try again!!!')
                        else:
                            print('You have wasted all password attempts!!!')
                break
            else:
                if i != 2:
                    print('Try again!!!')
                else:
                    print('You have wasted all username attempts!!!')

    elif a == 3:
        print('YOU ARE IN MARKETER ACCOUNT TYPE! \n')
        marketing_login = 'user-marketing'
        market_password = 'marketer'
        for i in range(3):
            market_login = input('Enter username >>> ').lower()
            if marketing_login == market_login:
                for j in range(3):
                    marketing_password = input('Enter password >>> ').lower()
                    if marketing_password == market_password:
                        marketer_menu()
                        break
                    else:
                        if j != 2:
                            print('Try again!!!')
                        else:
                            print('You have wasted all password attempts!!!')
                break
            else:
                if i != 2:
                    print('Try again!!!')
                else:
                    print('You have wasted all username attempts!!!')
    elif a == 4:
        print('YOU ARE IN WORKER ACCOUNT! \n')
        worker_login = 'user-worker'
        work_password = 'worker'
        for i in range(3):
            work_login = input('Enter username >>> ').lower()
            if worker_login == work_login:
                for j in range(3):
                    worker_password = input('Enter password >>> ').lower()
                    if worker_password == work_password:
                        worker_menu()
                        break
                    else:
                        if j != 2:
                            print('Try again!!!')
                        else:
                            print('You have wasted all password attempts!!!')
                break
            else:
                if i != 2:
                    print('Try again!!!')
                else:
                    print('You have wasted all username attempts!!!')
    else:
        if a != 0:
            print(
                ' >>> SORRY, BUT WE DID NOT FIND THIS TYPE OF ACCOUNT, PLEASE TRY AGAIN. <<< \n')
            account()


account()
