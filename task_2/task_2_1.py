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


def sort_list(my_list):
    i, j, size = 1, 2, len(new_list)
    i = 1
    while i < size:
        if my_list[i - 1] <= my_list[i]:
            i += 1
        else:
            tmp = my_list[i]
            my_list[i] = my_list[i - 1]
            my_list[i - 1] = tmp
            i -= 1
            if i == 0:
                i = 1
    return my_list


m = 10
new_list = [randint(-100, 100) for i in range(2 * m + 1)]
print(sort_list(new_list))
lst = sort_list(new_list)
print(timeit("sort_list(new_list.copy())", globals=globals(), number=1000))  # 0.001593699999830278


m = 100
new_list = [randint(-100, 100) for i in range(2 * m + 1)]
print(sort_list(new_list))
lst = sort_list(new_list)
print(timeit("sort_list(new_list.copy())", globals=globals(), number=1000))  # 0.014768999999432708


m = 1000
new_list = [randint(-100, 100) for i in range(2 * m + 1)]
print(sort_list(new_list))
lst = sort_list(new_list)
print(timeit("sort_list(new_list.copy())", globals=globals(), number=1000))  # 0.17995410000003176

# Выполнено с помощью Гномьей сортировки.