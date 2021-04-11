b=list()
a=['a', 'a', "sa", "dsd", {2: "dict"}]
b=['a', 'G', "sa", "dsd", {2: "dict"}]
print (a, b)
print(type(a))
st="ssssss  'sdfsdfsdf' "
print(st)
print(a[3])
id(a)
print(a==b)
print(b[::-1])
b+="str"
print(b)
print(a+b)
print('sa' in a)
print('ssa' in a)
list2=['sa']*10
print(list2)
list1=list2+a
print(list1.count('sa'))
print(len(list1))
print ('zz' in list1)
print(list1)
aspr=list1.pop(14)
print(list1)
print(aspr)
print(list1.index("dsd"))
print(list1)
print(max(list1))
print(min(list1))
print(list1)
list1.sort(reverse=True)  #in place
print(list1)
list1.sort(reverse=False)
print(list1)
print(sorted(list1))      #mot in place
new_list=['fsd', 'asd', 'asdasds', ['s', ['ssss', 'asadsda'],'asd'],['ssa', 'sssda']]
print(new_list[3][1][-1])
string='а проснись, сыч, ты обо...'
string='О'+string[1:]
print(string)
string+='!!!!'

a_list=string.split()   #split
print(a_list)

a_list.append('не')   #мутабельность
print(a_list)

a_list.remove('не') #мутабельность
print(a_list)
list1[0]=123123123
print(list2)
print(list2)
print(list2)
del list2[3]            #удаление элемента списка
print(list2)
list2.remove('sa')
print(list2)
list3=[1,2,3,4,5,6,7,8]
list3.insert(2, 100)
print(list3)            #вставка в середину списка
del list2 #удаление

try:
    print(list2)                                           #TRY and EXCEPT
except:
    print("такого перечня нет!")    


z=['a', 'b', 'c']
print('-*-*-'.join(z))                  #объединение элементов списка

#КорТЕЖ
oops=tuple()    
tuple1=(1, 123, 'sdfsdf', [1, "23"], {1 : "s", 2 : "dad"})
print(tuple1)
print(tuple1[::-1])
t=1,
print(t)
t=1, 2, ['sdasd', 1, 1.5, 'sadas']                  # скобки фактически не нужны, по сути то же самое t=(1, 2, ['sdasd', 1, 1.5, 'sadas'])
print(t)
print(t[2][1])
t[2][2] ='sdasd'
print(t)
t[2].append('senSDD')
print(t)
tT=('amba', 'zumba', 'rumba')                       # как оказалось, не обязательно почему то
z, x, c =('amba', 'zumba', 'rumba')                 #распаковка 
print(z,  x,  c)


oooo=('num1', 'num2', 'num3')   
y,u,i=oooo                      #запаковка
print(y,u,i)

a = 5
b = "строка"
a, b = "строка", 5
print(a, b)                     #1)Мой способ

a = 5
b = "строка"
temp=a
a=b
b=temp
print(a, b)                     #2)тупо длинный способ


a = 5
b = "строка"
a, b = b, a 
print(a, b)                     #3)лучший способ


#СЛОВАРЬ
oomph=dict()
oomph = {
        'key1' : "value1",
        'key3' : "value2",
        'key3' : "value3",
        2.7 : 123123,
        ('currancy', 'numb') : ('BYN', 5),
}
print (oomph)


d=dict([
  ['Доллар', 'USD'],                        # Пример 2 создания словаря СТРЕМНАЯ БАДЯГА по созданию словаря, неочевидно
  ('Белорусский рубль','BYN')  
])
print(d)
print(type(d))

d=dict(                                     # Пример 3 более очевидный
Света=27,
Юра=33,
Катя=34
)
print(d)

print(d['Света'])                           # доступ по ключу

clue={
        'Валентин Дудович': 
        {'пол':"мужик",
        'возраст': 34,
        'хобби':["сосет бабло", 'бьет детей', 'пьет' ]
        },
        'Аниса Александровна': 
        {'пол':"жанчына",
        'возраст': 33,
        'хобби':"сосет бабло"
        }
}
print(clue['Валентин Дудович']['хобби'][2])
print(len(clue))

print(clue.get('Валентин Ддович', 'Нет такого значения'))

print(clue.items())                                                 ######### WTF!!!

print(clue.keys())                                                  #Показать ключи

print(clue.values())                                            #Показать значения
print(clue)
clue['Валентин Дудович']['пол']='мудак'
print(clue)



import copy

slounik= copy.deepcopy(clue)                                                #ПРАВИЛЬНОЕ КОПИРОВАНИЕ СЛОВАРЯ без изменения индекса словаря копируемого
slounik['Валентин Дудович']['пол']='чудак'
print(slounik)
print(clue)


ass=slounik.pop('Валентин Дудович')                #попули
print(ass)
print(ass)
print(ass)
print(slounik)
slounik.update(clue)                                    ##обновляем словарь новым (старым) словарем

print(slounik)


#SET МНОЖЕСТВО
s=set()
s.add('guzno')
s.add('www')
s.add('www')                                        #множество НЕ добавляет повторно встречающиеся элементы

print(s)


list_rep=[1, 1, 1, 2, 33, 3, 33,11, 1]
print(list(set(list_rep)))                          #фильтр повторяющихся данных