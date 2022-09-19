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


def median_search(my_list):
    global median
    more = 0
    less = 0
    ind = 0
    for i in my_list:
        for j in my_list[ind + 1:]:
            if i > j:
                more += 1
            else:
                less += 1
        if less == (round(len(my_list) / 2)):
            median = i
            break
        elif more == (round(len(my_list) / 2)):
            median = i
            break
        else:
            more = 0
            less = 0
            ind = 0

    return median


m = 10
new_list = [randint(-100, 100) for i in range(2 * m + 1)]
my_median = median_search(new_list)
print(new_list)
print(f"Медиана: {my_median}")
print(timeit("median_search(new_list.copy())", globals=globals(), number=1000))  # 0.008698500000718923

m = 100
new_list = [randint(-100, 100) for i in range(2 * m + 1)]
print(new_list)
print(timeit("median_search(new_list.copy())", globals=globals(), number=1000))  # 0.8659396000002744

m = 1000
new_list = [randint(-100, 100) for i in range(2 * m + 1)]
print(new_list)
print(timeit("median_search(new_list.copy())", globals=globals(), number=1000))  # 4.614929100000154
