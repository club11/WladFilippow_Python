#my module
# калькулятор, функции меню, проверка введенного логина

def menu_list():
	actions_list = '''
	Меню:\n
	1. вывести список пользователей)(ключ - login) (L) (введите \'1\')
	2. показать информацию о пользователе (рост, вес, шкала БМИ) (R) (введите \'2\')
	3. изменить данные о пользователе (выбираем соот во ключу) (U) (введите \'3\')
	4. удалить пользователя (введите \'4\') (D)
	5. добавить пользователя (введите \'6\') (C)
	6. выход'''
	print(actions_list)
	the_choice = int(input('введите Ваш выбор (от 1 до 6):\n'))
	return the_choice

list_of_users = {'Captain America': {'пол': 'мужск',
                 'рост, см': 188,
                 'вес, кг': 109,
                 'BMI_index' : 111},
 'Iron Man': {'пол': 'мужск',
                    'рост': '185',
                    'вес, кг': 90,
                    'BMI_index' : 111}}

def back_to_menu():									#возвращаем в меню
	back_button = input('нажмите \'M\' для возвращения в главное меню:')
	while back_button != 'm':
		back_button = input('нажмите \'M\' для возвращения в главное меню:')
	return menu_list	

def user_login_exist():   						#проверка введенного логина
	global list_of_users
	check_user_login = input('введите логин пользователя:')
	list_of_logins = list_of_users.keys()
	while check_user_login not in list_of_logins:
		check_user_login = input('логин отсутствует. введите корректный логин:')
	return check_user_login

def check_login_data(*arg, **kwarg):				# проверка на существующий логин
    global list_of_users
    new_login_check = input('введите логин:')
    check = list_of_users.keys()
    while new_login_check in check:
        print('пользователь с таким логином уже существует')
        print(check)
        new_login_check = input('введите логин:')
    return new_login_check   

def bmi_calc():							# BMI - калькулятор
	gender = input('введите пол:')
	height = int(input('введите рост:'))/100
	weight = int(input('введите вес:'))
	bmi_index = int(weight / height*height)
	scale ='20==============================50'                              # шкала len(34) с шагом в 1 единицу
	scale = scale[0 : bmi_index - 1 -20 ] +'|' + scale[bmi_index -20 : ]          # слайс по значению точки шкалы + добавление метки | + слайс остатка
	scale = '=' * (bmi_index - 21) +'|' + '=' *(bmi_index -20)
	print('20'+ scale + '50')
	user_data = {'пол' : gender, 'рост, см' : height, 'вес, кг' : weight, 'BMI_index' : bmi_index }
	return user_data