#Индекс Массы Тела рассчитывается по формуле: ИМТ = вес (кг) / рост (м)2.
user_name = str
weight_data = 1
height_data = 1
bmi_index = 4
who3le_users_list ={}
while True:

    def bmi_calculator(weightt, heightt):
        bmi = int(weightt) / (int(heightt)/100*int(heightt)/100)
        return bmi

    def bmi_presentation(func):
        value_point = int (func) -20
        show_string = 30 * '='
        show_string = show_string[: value_point] + '|' + show_string[value_point :]
        print(show_string)

    who3le_users_list[user_name] = {'weight' : weight_data, 'height' : height_data, 'bmi' : bmi_index, 'bmi_pres' : bmi_presentation}

#    menu_choise = input("""Меню:'\n 
#    '1. Вывести список пользователей(ключ - login)'\n
#    '2. Посмотреть инфо о пользователе (рост, вес, шкала БМИ)'\n
#    '3. Изменить данные о пользователе (выбираем соответсвенно ключу)'\n
#    '4. Удалить выбранного пользователя'\n
#    '5. Добавить пользователя'\n
#    '6. Выход\n""")

    choose_a_function = input(""" 
1. Вывести список пользователей(ключ - login)
2. Посмотреть инфо о пользователе (рост, вес, шкала БМИ)
3. Изменить данные о пользователе (выбираем соответсвенно ключу)
4. Удалить выбранного пользователя
5. Добавить пользователя
6. Выход
введите параметр:""")

    if choose_a_function not in ('1', '2','3','4','5','6','7','8','9','0',):
        continue

    elif int(choose_a_function) == 1:
        #    if menu_choise == '1':
        print('*'*32)
        print(who3le_users_list.keys())
        print('*'*32)

    elif int(choose_a_function) == 2:
        #   elif menu_choise == '2':                    # '2. Посмотреть инфо о пользователе (рост, вес, шкала БМИ)'\n
        def user_present(some_dict):   
            while True:   
                print('если желаете вернуться в предыдущее меню, нажмите "n"')
                user_name = input("введите логин для просмотра параметров:")
                if user_name =='n':
                    break
                if user_name in some_dict.keys():
                    print(some_dict[user_name])
                    global bmi_presentation
                    bmi_presentation = bmi_presentation(some_dict[user_name]['bmi']) 
                    crutch = some_dict[user_name]['bmi']
                    print(f'{user_name}, ваш индекс BMI равен {crutch}')
                    break
                else:
                    continue     

        print('*'*32)                
        user_data = user_present(who3le_users_list) 
        print('*'*32)

    #    bmi_index = bmi_calculator(weight_data, height_data)                               #полезная штука
    #    print(f'{user_name}, ваш индекс BMI равен {bmi_index}')                            #полезная штука

    #    bmi_presentation = bmi_presentation(bmi_index)                                     #полезная штука

    elif int(choose_a_function) == 3:
        #    elif menu_choise == '3':                   #'3. Изменить данные о пользователе (выбираем соответсвенно ключу)'\n
        def user_change(some_dict): 
            while True:  
                print('если желаете вернуться в предыдущее меню, нажмите "n"')
                user_name = input("введите логин для изменения параметров:")
                if user_name =='n':
                    break
                user_change = some_dict.get(user_name, )
                print(user_change)
                if user_change is None:
                    continue
                else:
                    weight_dat = int(input('введите вес (кг):'))
                    height_dat = int(input('введите рост (см):'))
                    bmi_index = bmi_calculator(weight_dat, height_dat)
                    global bmi_presentation
                    bmi_presentation = bmi_presentation(bmi_index)
                    some_dict[user_name] = {'weight' : weight_dat, 'height' : height_dat, 'bmi' : bmi_index, 'bmi_pres' : bmi_presentation}
                    return some_dict

        print('*'*32)            
        change_user_data = user_change(who3le_users_list) 
        print('*'*32)

    elif int(choose_a_function) == 4:
            #elif menu_choise == '4':       #'4. Удалить выбранного пользователя'\n
        def user_del(some_dict): 
            while True:  
                print('если желаете вернуться в предыдущее меню, нажмите "n"')
                user_name = input("введите логин для удаления:")
                if user_name =='n':
                    break
                if user_name in some_dict.keys():
                    del(some_dict[user_name])
                    break
                else:
                    continue

        print('*'*32)
        del_user_data = user_del(who3le_users_list) 
        print('*'*32)

    elif int(choose_a_function) == 5:
        #elif menu_choise == '5':               #'5. Добавить пользователя'\n
        def user_add(some_dict): 
            while True:  
                user_name = input("добавить пользователя:")
                if user_name in some_dict.keys():
                    print('юзер с таким логином уже существует')
                    print('если желаете вернуться в предыдущее меню, нажмите "n"')
                    back_to_menu = input()
                    if back_to_menu =='n':
                        break
                    continue
                else:
                    weight_datt = int(input('введите вес (кг):'))
                    height_datt = int(input('введите рост (см):'))
                    bmi_index = bmi_calculator(weight_datt, height_datt)
                    global bmi_presentation
                    bmi_presentation = bmi_presentation(bmi_index)
                    some_dict[user_name] = {'weight' : weight_datt, 'height' : height_datt, 'bmi' : bmi_index, 'bmi_pres' : bmi_presentation}
                    break

        print('*'*32)
        add_new_user = user_add(who3le_users_list) 
        print('*'*32)

    elif int(choose_a_function) == 6:
            #elif menu_choise == '6':
        exit()    



