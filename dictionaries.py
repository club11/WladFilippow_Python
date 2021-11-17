import copy

""" 

nd = {
    "Sveta Sokolova" : {
        'sex' : 'female',
        'age' : 16,
        'hobby' : ['flowers', 'singing'],
    },
}
print(nd["Sveta Sokolova"])
print(nd["Sveta Sokolova"]['age'])
nd ['vasya'] = 'loch'
print(nd)
print(nd.items())
print(nd.pop("Sveta Sokolova"))
print(nd)

nd["Sveta Sokolova"] = 'asdassd'
print(nd)
print(len(nd))

print(nd.get('sdasdasd', 'нет такого ключа'))
print(nd.keys())
print(nd.values())
new_nd = nd
print(new_nd)
print(nd)
new_nd ['vasya'] = 'ne loch'
print(new_nd)
print(nd)
print(id(new_nd))
print(id(nd))

new_nd = copy.deepcopy(nd)
new_nd ['vasya'] = 'loch'
print(new_nd)
print(nd)

some_list = [1, 1, 1, 33, 33, 333123]
print(set(some_list))
print(list(set(some_list)))

############# LESSON 4
a = input('vvedite chislo:')
k = a or 'ne vveli chislo'      ### ЛЕНЬ
print(k)

nn = 0 or '' or 7 or 6 or False         # Лень
print(a)
a = 5 and 6 and 0 and True and 4        # Лень
print(a)
a= 5 and 7                              # Лень   
print(a)
a= 0 and 7                              # Лень   
print(a)

a, b = 5, 5
if a == b:
    a += 1
    b -=1
    print(f'{a} + {b} = {b} + {a}') 

x = int(input('vvedite esho chislo:')) 
if x < 50:
    print(f'x'"<50") 
elif x > 100:
    print(f'x'">100")  
else:   
    print(f'x'">50 and < 100")  

x = int(input('vvedite esho chislo:')) 
if x < 50:
    print(f'x'"<50") 
if x > 100:
    print(f'x'">100")  
else:   
    print(f'x'">50 and < 100")      


### case аналог:
a = {1 : 'y', 2 : 'n'}
a.get(1, 'значение отсутствует')
a.get(2, 'значение отсутствует') 

"""

""" 
##Циклы: for , while

#блоки с for и while не формируют локальную область видимость переменной 

n = input('vvedite chislo:')
d = {1: '22', 2: '2332', 3: '3333'}
print(d.values())
for i in d.values():
    print(i)
for i in d.items():     # items - tuple в виде тапла
    print(i)
for i in d.items():
    print(*i)       #- * (звезхдочка) - распаковка тапла
for i in d.keys():
    print(i)
for i in d:
    print(d[i])     # по динамическому ключу

for name in str('222'):
    print('Hello, '+ name )    

# range-  генератор
for i in range (1, 20, 3):
    print(i)


while True:
    a = input('vvedite dannye:')
    if a == 'q':
        break
    else:
        print('hurra! hurra!') 


i = 0
while i < 100000000:
    i += 1
print(i)    

## comrehension
end_list = []
for i in range(10000):
    end_list.append(i**10)

end_list = [x**10 for x in range(10000)]    # list comrehension

end_dict = {x : x**10 for x in range(10000)}    # dictionary comrehension
print(end_dict[33])


################# ZIP

list_a = ['a', 'b', 'c', 'asdasd']
list_b = [1, 2, 3, 4]

for a,b in zip(list_a, list_b):
    print(a, b)                                # склкеиваем два списка
print(list(zip(list_a, list_b)))             # из zip в список  
print(dict(list(zip(list_a, list_b))))
print(dict(zip(list_a, list_b)))        ## даже проще из zip в словарь

################# ENUMERATE
list_a = ['a', 'b', 'c', 'asdasd']
for n, v in enumerate(list_a, start=1):
    print(n, v)
"""

"""  
######## LESSON 5
def my_name():
    print('my name is Wlad')
print(type(my_name))   
print(my_name()) 



def hello_user(a):
    print(f'your name is {a}')
name = input("ttype the name:")    
print(hello_user(name))
"""
"""  
def hello_user(a, b, c):
    "" a - sdfsdfsfdsfsdf ""                          #при наведении курсором на имя функции подсветить описание (полезная фича)
    print(f'your name is {a}, {b}, {c}')
#    print('your name is {}, {}, {}'.format(a,b,c))     ##### устаревший вариант
name1 = input("type the name1:")    
name2 = input("type the name2:")    
name3  = input("type the name3:")    
print(hello_user(name1, name2, name3))                  #просто вызов функции   ПОЗИЦИОННЫЙ СПОСОБ
print(hello_user(c=name1, a=name2, b=name3))            #вызов функции с указанными подставными параметрами аргументов      ИМЕННОЙ СПОСОБ
print(hello_user(name1, c=name2, b=name3))              # СМЕШАННЫЙ СПОСОБ вызова функции
#### ПРИ ЭТОМ СЛЕДУЕТ ПОМНИТЬ, ЧТО МОЖНО ОПРЕДЕЛЯТЬ ЗНАЧЕНИЕ ПЕРЕМЕННОЙ ПО УМОЛЧАНИЮ  ПРИ ОПРЕДЕЛЕНИИ ФУНКЦИИ(БУДЕТ ИСПОЛЬЗОВАНО ЕСЛИ НЕ ПОДСТАВИТСЯ ДРУГОЕ ЗНАЧЕНИЕ):
def hello_user2(a, c, b="АНАРХИЯ"):
     print(f'your name is {a}, {b}, {c}')
name4 = input("type the name4:")      
name6  = input("type the name6:")       
print(hello_user2(name4, name6))                        # в данном случае при вводе 2 аргументов третьим подается b="АНАРХИЯ" по умолчанию
"""
"""  
### *ARGS, **KWARGS
def mocna_func(a, b, *args, ** kwargs):
    #print(f'imprented data: {a}, {b}, {args[0] [1]}, {kwargs}')     # доработать , здесь у меня ошибка самодельный код
    print(f'imprented data: {a}, {b}, {args[1:3:1]}, {kwargs}')     # доработать , здесь у меня ошибка самодельный код
print(mocna_func('asdasd', 222, 232343, 234234, 12123, 123213, ap='s1212', ab='1ddqwdqdqw'))
"""
"""  
## возвращение функцией значения RETURN
def age_control(name, lastname, age=18, weight=100):
    name = input('write or name:')
    lastname = input('write or lastname:')
    age = int(input('write or age:'))
    if age > 18:
        return 'You are adult'
    return 'You are not adult'
a = age_control('a', 'b')   
print (a) 
"""
"""
### Функции высшего порядка: функция может принять функцию и вернуть функцию

ПРиЧЕМ ВАЖНО понимать когда функция принимается как коробка  (например def logger(min) или return helper ), а когда идет на исполнение (например return helper() )


def mul(a):                 # замыкание
    a=5
    def helper(b):
        return a * b
    return helper           # тут функция возвращает функцию helper с залипшей снаружи переменной     

nn = mul(100)                # здесь неважно что ввели 20или 100
print(nn(3))                ###### ВАХХХХХХ!!!!! MAGIC !!! все просто nn = helper и сам выполняется как функция


import datetime
print(datetime.datetime.now())

def logger(fun):
    # fun залипла тут
    def helper(v):
        return print("RESULT OF THE WHOLE FUNCTION IS:   " + str(datetime.datetime.now()) + '  ||  ' + str(fun(v)))
    return helper    
a= logger(min)            #здесь закинули функцию например print Но не выполняем ее еще т.е. не print()
print(a)
print("---------------")
a([3, 5, 7])
a= logger(max) 
a([3, 5, 7])
"""  
"""  
### ДЕКОРАТОР
#Декоратор - функция которая принимает на вход функцию расширяя ее поведение без изменения
# new_func = decorator(new_func)  -----вот так по сути это выглядит

def decorator(func):
    # making magic staff
    def wrapper_decorator(*args, **kwargs):
        # do something before
        value = func(*args, **kwargs)
        # do something after
        return value
    return wrapper_decorator    

#############################
def new_func(name):
    print(f'Hello, {name}') 

print(new_func('W.L.A.D.'))      


@decorator
def new_func(name):
    print(f'Hello, {name}') 

print(new_func('W.L.A.D.')) 
##############################
"""
"""  
# Теперь рабочий пример декоратора:

def len_check(func):
    #
    def wrapper_decorator(*args, **kwargs):
        if args[0] > 5:
            return 'Too big'
        value = func(*args, **kwargs)
        return value
    return wrapper_decorator   

def my_len(lst):
    return len(lst)    

a = my_len([1, 2, 3, 3, 4, 54, 54])
print(a)

#-------------------- теперь та же функйция но с декоратором:

@len_check
def my_len(lst):
    return len(lst)    

a = my_len([1, 2, 3, 3, 4, 54, 54])
print(a)
"""


"""  
#Рабочий пример из задания на дом - поломай мозгь

account = input('введите имя пользователя:')
sum = 15000

def my_decoratorfunc(func):                                                       # my sugar description
    def check_login(*args, **kwargs):
        if args[0] == 'admin':
            return func(*args, **kwargs)
        print('доступ запрещен')
    return check_login      

@my_decoratorfunc
def account_money(login, smoney):                                                #функция по выводу денег на счету
    print(f'Money on {account} account:', sum) 

a = account_money(account, sum)

"""
"""  
#def logger(func):
#    def helper(v):
#        return print('asdasdsadsadasdasdasd asdasd asdasd' + str(func(v)))
#    return helper  
#
#b = logger(min)    
#print(b([3, 5, 7]))


#loggin = input('whrite your loggin:')
#money_amont = 11000
#
#def decorator(func):
#    def wrapper_decorator(*args, **kwargs):
#        if args[0] == 'admin':
#            value = func(*args, **kwargs)
#            return value
#        return 'access denied'    
#    return wrapper_decorator                    #ОТСУТСТВИЕ СКОБОК - Функция возвращает объект, а не результат работы
#
#@decorator
#def show_money(log, money):
#   return f'{loggin}. on your account is {money_amont}'
#
#a = show_money(loggin, money_amont)  
#print(a)  
"""
"""  
#########Глобальные и локальные переменные
global_data = 'i am a global'

#чистая функция - которая никуда не вмешивается
def func(some_data):
    print(some_data)
    print(global_data)

n = func(1)
"""
"""  
global_data = 'i am a global'

def func():
    global_data = 'some new shit'           #переменная внутри функции с таким же именем как глобальная, ей переписали значение, НО в самой глобальной переменной значение останется прежним
    print(global_data)
    
def func2():
    global_da = 'some another shit'           
    print(global_da)   
    print(global_data)


a= func()   
print('------------------')
b= func2() 
print('------------------')
print(global_data)                      #значение глобальной переменной осталось прежним
"""
"""  
#измнение ГЛОБАЛЬНОЙ ПЕРЕМЕННОЙ ВНУТРИ ФУНКЦИИ -НЕЧИСТАЯ ФУНКЦИЯ:
global_data = 'i am a global'

def func():
    global global_data                      # втащили здесь глобальную переменную объявив ее словом global
    global_data = 'some new shit'           # изменяем Глобальную переменную
    print(global_data)

a= func()                               #значение глобальной переменной поменяли в функции
print(global_data)                      #значение глобальной переменной изменилось
"""
"""  
# АВТОМАТИЧЕСКИЙ ДОБАВИТЕЛЬ В СПИСОК
def list_auto_appender(el, l=[]):
    l.append(el)
    return l

a= ['sss', 222, 3, 5]
a = list_auto_appender('vasya', a)    
print(a)
"""
""" 
# НО АХТУНГ:
glo_data = 'iamglobal'

def glob_func(var, l=[]):
    l.append(var)
    return l
n = glob_func('ohnonono')    
print(n)
n = glob_func('ohnonono')    
print(n)
n = glob_func('ohnonono')    
print(n) 
# во избежание продолжения записывания в список (хотя у меня такого не происходило) при повторном вызове, лучше:
def list_auto_appender(el, l=None):
    if l is None:
        l = []
    l.append(el)
    return l

a= ['sss', 222, 3, 5]
a = list_auto_appender('added element')    
print(a)
a = list_auto_appender('new added element', a)    
print(a)



glo_data = 'iamglobal'

def glob_func(var, l=None):
    if l is None:
        l = []
    l.append(var)
    return l
n = glob_func('ohnonono')    
print(n)
n = glob_func('ohnonono')    
print(n)
n = glob_func('ohnonono')    
print(n)
 """
"""  
#ГЕНЕРАТОР
#генератор -специальная  функция, у ккоторой вмесс return стоит слоово yield.  ОТдав значение, функция как бы засыпает до следующего своего вызова (при этом запомнив текущее значение переменной)

def my_generator():
    yield 'vasya'
    yield 'petja'
    yield 'sava'

for i in my_generator():
    print(i)

# Генератор можно юзать пошагово командой next:

d= my_generator()
print(next(d))
print('------------')
print(next(d))


def my_range(start, stop):
    while True:
        if stop < start:
            raise StopIteration                                     #Одно из свойств итератора, можно выполнить останов итератора stopiteration (обрати внимание на флаг raise)
        yield print(start)
        start +=1
    
##a = my_range(1, 10)
##
##next(a)
##next(a)
##next(a)
#for i in my_range(1, 8):
#    i
"""
"""  
############# немножко о МАГИЧЕСКИХ МЕТОДАХ на примере double under __next__:
n = my_range(1, 5)
n.__next__()                #вызываем фактически то же что и next(n) . иными словами next(n) - это вызов my_range с методом __next__(n)
n.__next__()
"""

"""  
#пример моей маленькой проги - генератор пароля на коленке за 1 минуту:
account_name = input('type your name, please:')

def parol_gen(acc):
    first_data = 1
    last_data = 44
    while True:
        first_data += first_data
        last_data += last_data
        yield str(first_data) + acc + str(last_data)

n = parol_gen(account_name)
print(next(n))
print(next(n))
print(n.__next__())
"""
"""  
## РЕКУСИЯ - РЕКУСИЯ - РЕКУСИЯ - РЕКУСИЯ - РЕКУСИЯ - РЕКУСИЯ - РЕКУСИЯ - РЕКУСИЯ -

# на примере цифр - списков (навроде папок в дереве, нужно достать списки из списков, не зная общего конечного количества глубины вложения)Ж:

folder_list = [1,2, 3, 3435, [44, 433, 23, [33, 2, 77, 3, 'dasd'], 33, '33gfd'], [2, 6565, 3, 2, 1]]

def deep_list_into_list(some_list):
    for el in some_list:
        if isinstance(el, list):
            deep_list_into_list(el)
        else:
            print(el)  

nn = deep_list_into_list(folder_list)            
  """

