'''
1. написать программу которая: запрашивает у пользователя логин
2. Есть функция котороя выводит сумму на счете
3. Декорируем эту функцию декоратором который проверяет если пользовател - админ (получили на первом этапе, то выводит сумму счета (выполняет функ из п 2)
4. Если не админ - Сумму не выводить (функцию даже не выполнять) а выводить - доступ запрещен
'''
account = input('введите имя пользователя:')
sum = 15000

def my_decoratorfunc(func):                                                       # my sugar description
    def check_login(*args, **kwargs):
        if args[0] == 'admin':
            result = func(account, sum)
            return result
        print('доступ запрещен')
    return check_login      
#account_money = check_user(account_money)

@my_decoratorfunc
def account_money(account, sum):                                                #функция по выводу денег на счету
    print(f'Money on {account} account:', sum) 
a = account_money(account, sum)