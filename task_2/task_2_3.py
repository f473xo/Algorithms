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
lists = [randint(0, 100) for i in range(2 * m + 1)]
print(lists)
print(timeit("median(lists[:])", globals=globals(), number=10000))  # 0.018076899999869056
print(lists[m])

m = 100
lists = [randint(0, 100) for i in range(2 * m + 1)]
print(lists)
print(timeit("median(lists[:])", globals=globals(), number=10000))  # 0.027450400000361697
print(lists[m])

m = 1000
lists = [randint(0, 100) for i in range(2 * m + 1)]
print(lists)
print(timeit("median(lists[:])", globals=globals(), number=10000))  # 0.1384648999996898
print(lists[m])

