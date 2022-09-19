"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""


from random import randint
from timeit import timeit


def sort_list(list):
    i, j, size = 1, 2, len(lists)
    i = 1
    while i < size:
        if list[i - 1] <= list[i]:
            i += 1
        else:
            tmp = list[i]
            list[i] = list[i - 1]
            list[i - 1] = tmp
            i -= 1
            if i == 0:
                i = 1
    return list


m = 10
lists = [randint(0, 100) for i in range(2 * m + 1)]
print(sort_list(lists))
lst = sort_list(lists)
print(lst[m])
print(timeit("sort_list(lists[:])", globals=globals(), number=10000))  # 0.00165610000021843


m = 100
lists = [randint(0, 200) for i in range(2 * m + 1)]
print(sort_list(lists))
lst = sort_list(lists)
print(lst[m])
print(timeit("sort_list(lists[:])", globals=globals(), number=10000))  # 0.0.016157300000031682


m = 1000
lists = [randint(0, 2000) for i in range(2 * m + 1)]
print(sort_list(lists))
lst = sort_list(lists)
print(lst[m])
print(timeit("sort_list(lists[:])", globals=globals(), number=10000))  # 0.1922128999999586

# Выполнено с помощью Гномьей сортировки.