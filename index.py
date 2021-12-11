# повтор 
# for 
# while
# lambda fx
# functions

# int
# float
# bool

#        Iterables - потому что их можно прогнать через цикл
# str
# list
# tuple
# dict
# set



# for simbol in  'Hello':
#     print(simbol)

# for letter in  'Hello':
#     print(letter)

# for character in  'Hello':
#     print(character)

# for number in [10, 20, 30]:
#     print(number)

# for text in ['Elbek', 'Hello', 'Putin']:
#     print(text)

# for name in ['Elbek', 'Hello', 'Putin']:
#     print(name)

# names = ['Putin']
# names.append('Elbek')     #how to add to spisku
# del names[0]              #how to delete spiski po indexu
# names.remove('Elbek' '''удаляет по значению''')
# names.clear( )            #удаляет все из списка
 
# names.pop(0)              #how to delete spiski po indexu

# names_copy = names.copy()    # копирует массив
# names.count('Malik')         # считает сколько раз элемент повторяется в списке
# names.index('Elbek')         # возвращает индекс элемента

# sozdaet i prisvaivaet i perevernut spisok 
# names = names[::-1]

# sozdaet perevernutiy spisok
# names[::-1]

# переворачивает список 
# names.reverse()

# обновление списка (замена значения по индексу)
# names[0] = 'Aziz'

# расширяет другим списком 
# names.extend(range(10))
# names.extend({1, 2, 3})

# print(names)





# CRUD операции - Create read  update Delete


#  На вопрос в чем отличие списка от картежа следдует отвечать:
# 1 Списки изменяемые (мутируемые, модифицируемые)
# 2 Кортежи неизменяемые (немутируемые и немодифицируемые
# Можно ответить что списки поддерживают CRUD операции а кортеж только READ операцию

# names2 = ('Elbek', 'Aziz')
# names.count



# спискаподобные словарь
# dict ={
#     0: 'Malik', 
#     1: 'Putin',
#     2: 'Elbek'
# }
# print(dict[0])
# #print(dict[2])          # тут будет ошибка так как несуществующий ключ
# print(dict.get(1))
# print(dict.get(2))       #тут будет none
# со словарями желательно использовать .get

# print(dict.pop(1))
# print(dict.keys())
# print(dict.values())
# print(dict.popitem())
# print(dict)
# print(dict.items())

# print(range(6).index(4))

# str = "Putin is the worst"

# str = str.replace('is', 'IS')
# print(str.find('wo'))                # найдет по значению .find
# print(str.split('th'))
# print(str.strip(' '))               #удаляет по значению 
# print(str.rstrip(' '))              #справа
# print(str.lstrip(' '))              #слева
# print(str.capitalize())
# print(str.lower())
# print(str.upper())

# print('CASEFOLD',str.casefold())
# print('COUNT',str.count('P'))        #сколько раз встречается
# print('END WITH',str.endswith('P'))   #если да то тру а иначе фалс
# print('SWAP CASE',str.swapcase())
# print('HELLO I AM ZAKIR'.title())


def format_tel(tel):
    return f'{tel[0:4]} ({tel[4:6]}) {tel[6:9]}-{tel[9:11]}-{tel[11:13]}'

# format_tel('+998997776655')  #+998(99) 777-66-55
# Решение с использованием срезов

def format_tel_2(tel):
    return '{}{}{}{}({}{}) {}{}{}-{}{}-{}{}'.format(*list(tel))

print(format_tel('+998997776655'))
print(format_tel_2('+998997776655'))
print(*list('+998997776655'))