"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
2) без сортировки
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""


from random import randint
from timeit import timeit


m = 10
lists = [randint(0, 100) for i in range(2 * m + 1)]
print(lists)
print(timeit("lists[m]", globals=globals()))  # 0.03082029999995939
print(lists[m])

m = 100
lists = [randint(0, 100) for i in range(2 * m + 1)]
print(lists)
print(timeit("lists[m]", globals=globals()))  # 0.03348160000018652
print(lists[m])

m = 1000
lists = [randint(0, 100) for i in range(2 * m + 1)]
print(lists)
print(timeit("lists[m]", globals=globals()))  # 0.0333883999999216
print(lists[m])
