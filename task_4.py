"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""


from collections import OrderedDict
from timeit import timeit

main_dict = {}
main_ord_dict = OrderedDict()


def append_dict(some_dict: dict):
    for i in range(10 ** 4):
        some_dict[i] = i
    return some_dict


def append_ord_dict(some_ord_dict: dict):
    for i in range(10 ** 4):
        some_ord_dict[i] = i
    return some_ord_dict


print('Заполнение.')
print(timeit('append_dict(main_dict.copy())', globals=globals(), number=100), '- dict')
print(timeit('append_ord_dict(main_ord_dict.copy())', globals=globals(), number=100), '- OrderedDict')
append_dict(main_dict)
append_ord_dict(main_ord_dict)
# 0.0627600000007078
# 0.09616219999952591


def pop_dict(some_dict: dict):
    for i in range(10 ** 4):
        some_dict.pop(i)
    return some_dict


def pop_ord_dict(some_ord_dict: dict):
    for i in range(10 ** 4):
        some_ord_dict.pop(i)
    return some_ord_dict


print('Удаление.')
print(timeit('pop_dict(main_dict.copy())', globals=globals(), number=100), '- dict')
print(timeit('pop_ord_dict(main_ord_dict.copy())', globals=globals(), number=100), '- OrderedDict')
# 0.07575469999937923
# 0.17790939999940747
'''
Обычный словарь выигрывает по времени во всех представленных случаях.
В Python 3.6 и более поздних версиях словари изначально упорядоченны, смысла в использовании OrderedDict нет.
'''