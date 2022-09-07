"""
Задание 1.
Реализуйте функции:
a) заполнение списка, оцените сложность в O-нотации
   заполнение словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
b) получение элемента списка, оцените сложность в O-нотации
   получение элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
с) удаление элемента списка, оцените сложность в O-нотации
   удаление элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""


import time


def time_dec(func):
    start_time = time.time()
    func()
    return print(f'Время выполнения: {time.time() - start_time}')


list1 = []
dict1 = dict()

# A.
@time_dec
def add_list():
    # Сложность: О(1)
    for i in range(10000):
        list1.append(i)
    print(f'Список заполнен.')

@time_dec
def add_dict():
    # Сложность: О(1)
    for i in range(10000):
        dict1[i] = i
    print(f'Словарь заполнен.')

# Словарь заполняется дольше из-за вычислений хеша.


print()

# B.
@time_dec
def check_list():
    print('Получение элементов списка.')
    for i in range(1000):
        print(list1[i], end=' ')  # Сложность O(1)
    print('\nЭлементы получены.')

@time_dec
def check_dict():
    print(f'Получение элементов словаря')
    for i in range(1000):
        print(dict1[i], end=' ')  # Сложность O(1)
    print('\nЭлементы получены.')


print()

# C.
@time_dec
def del_list():
    """Сложность O(1)"""
    print('Удаление элементов списка')
    for i in range(10000):
        list1.pop(0)
    print('Элементы удалены')

@time_dec
def del_dict():
    """Сложность O(1)"""
    print('Удаление элементов словаря')
    for i in range(10000):
        dict1.pop(i)
    print('Элементы удалены')

# Так как большинство операций по словарю имеют константную сложность они быстрее чем у списков.
