"""
Задание 1.
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее)!
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""

import random
from timeit import timeit

numbers = [random.randint(-100, 100) for _ in range(10)]


def sort_bubble(nums):
    for j in range(len(nums) - 1):
        for i in range(len(nums) - 1 - j):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums


print(sort_bubble(numbers))
print(timeit("sort_bubble(numbers.copy())", globals=globals(), number=1000))  # 0.004450200000064797


def sort_bubble_2_0(nums):
    n = 1
    count = 0
    flag = True
    for j in range(len(nums) - n):
        if flag is False:
            return nums
        flag = False
        for i in range(len(nums) - 1 - j):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                flag = True
            count += 1
    return nums


print(sort_bubble_2_0(numbers))  # 0.0010987999994540587
print(timeit("sort_bubble_2_0(numbers.copy())", globals=globals(), number=1000))
