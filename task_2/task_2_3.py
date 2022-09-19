"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
3) с помощью встроенной функции поиска медианы
сделайте замеры на массивах длиной 10, 100, 1000 элементов
В конце сделайте аналитику какой трех из способов оказался эффективнее
"""


from timeit import timeit
from random import randint
from numpy import median


m = 10
my_list = [randint(-100, 100) for i in range(2 * m + 1)]
print(my_list)
print(timeit("median(my_list.copy())", globals=globals(), number=1000))  # 0.01675630000045203

m = 100
my_list = [randint(-100, 100) for i in range(2 * m + 1)]
print(my_list)
print(timeit("median(my_list.copy())", globals=globals(), number=1000))  # 0.026233700000375393

m = 1000
my_list = [randint(-100, 100) for i in range(2 * m + 1)]
print(my_list)
print(timeit("median(my_list.copy())", globals=globals(), number=1000))  # 0.12784089999968273
