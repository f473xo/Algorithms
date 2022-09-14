"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""


import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


num = [el for el in range(10000)]

print(timeit.timeit('func_1(num)', globals=globals(), number=1000))

# 0.7727904000003036

print(timeit.timeit('func_1(num)', globals=globals(), number=10000))

# 7.478116499999942


def func_2(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


print(timeit.timeit('func_2(num)', globals=globals(), number=1000))

# 0.5932646999999633

print(timeit.timeit('func_2(num)', globals=globals(), number=10000))

# 5.960700499999803

# Оптимизация кода ускорила работу.
