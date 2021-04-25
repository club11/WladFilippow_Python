from my_module_func import menu_list, list_of_users, back_to_menu, user_login_exist, check_login_data, bmi_calc

def show_users_list():				#1. вывести список пользователей)(ключ - login) (L) (введите \'1\')
	global list_of_users
	list_of_logins = dict(list_of_users)
	user_keys = list_of_logins.keys()
	print(list(user_keys))
	back_to_menu()
		
def show_users_info():				#2. показать информацию о пользователе (рост, вес, шкала БМИ) (R) (введите \'2\')
	global list_of_users
	check = user_login_exist()
	print('параметры ' + str(check), " :",   list_of_users.get(check))
	back_to_menu()
		
def change_user_data():						#3.изменить данные о пользователе (выбираем соот во ключу) (U) (введите \'3\')
	global list_of_users
	checked_user_login = user_login_exist()
	update_user_data = bmi_calc()
	list_of_users.update({checked_user_login : update_user_data}) 	  
	back_to_menu()
	
def del_user():												#4. удалить пользователя (введите \'4\') (D)
    global list_of_users
    print(list_of_users.keys()) 
    checked_user_login = user_login_exist()
    del(list_of_users[checked_user_login])
    print('пользователь удален:', list(list_of_users.keys())) 
    back_to_menu()
  
def add_new_user():					#5. добавить пользователя (введите \'6\') (C)
    global list_of_users
    new_login = check_login_data()
    new_data = bmi_calc()
    list_of_users.setdefault(new_login, new_data)
    back_to_menu()



def exit_program():					# выход из программы
	end_program = input('нажмите \'M\' для возвращения в главное меню или: \'y\' для выхода из программы:')
	while end_program != 'y':
		if end_program == 'y':
			import sys
			sys.exit()
		elif end_program == 'm':
			menu_list()
		end_program = input('нажмите \'M\' для возвращения в главное меню или: \'y\' для выхода из программы:')		
	
actions_list = {
1 : show_users_list,
2 : show_users_info,
3 : change_user_data,
4 : del_user,
5 : add_new_user,
6 : exit_program
}

def do_action(choice_in_menu):
	return actions_list.get(choice_in_menu)

def main():
	while True:
		choice_in_menu = menu_list()
		do_action = actions_list.get(choice_in_menu)
		do_action()
		
main()
