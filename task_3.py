"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""


from collections import deque
from timeit import timeit


my_list = [i for i in range(10 ** 6)]
my_deque = deque([i for i in range(10 ** 6)])


def append_list():
    for i in range(10 ** 5):
        my_list.append(i)


def append_deque():
    for i in range(10 ** 5):
        my_deque.append(i)


# print('Метод append:')
# print(timeit('append_list()', globals=globals(), number=100), '- Список')
# print(timeit('append_deque()', globals=globals(), number=100), '- Дек')
# 0.7258392000003369
# 0.5340427000001


def pop_list(list1):
    for _ in range(10 ** 4):
        list1.pop()


def pop_deque(deque1):
    for _ in range(10 ** 4):
        deque1.pop()


# print('Метод pop:')
# print(timeit('pop_list(my_list.copy())', globals=globals(), number=100), '- Список')
# print(timeit('pop_deque(my_deque.copy())', globals=globals(), number=100), '- Дек')
# 0.8262089999998352
# 1.3882211999998617


def extend_list():
    for _ in range(1000):
        my_list.extend([1, 2, 3, 4])


def extend_deque():
    for _ in range(1000):
        my_deque.extend([1, 2, 3, 4])


# print('Метод extend:')
# print(timeit('extend_list()', globals=globals(), number=100), '- Список')
# print(timeit('extend_deque()', globals=globals(), number=100), '- Дек')
# 0.017523600000458828
# 0.012478599999667495


def appendleft_list():
    for i in range(10 ** 4):
        my_list.insert(0, i)


def appendleft_deque():
    for i in range(10 ** 4):
        my_deque.appendleft(i)


# print('Метод appendleft:')
# print(timeit('appendleft_list()', globals=globals(), number=10), '- Список')
# print(timeit('appendleft_deque()', globals=globals(), number=10), '- Дек')
# 60.83301380000012
# 0.005189999999856809


def popleft_list(list1):
    for i in range(10 ** 3):
        list1.pop(0)


def popleft_deque(deque1):
    for i in range(10 ** 3):
        deque1.popleft()


# print('Метод popleft:')
# print(timeit('popleft_list(my_list.copy())', globals=globals(), number=10), '- Список')
# print(timeit('popleft_deque(my_deque.copy())', globals=globals(), number=10), '- Дек')
# 6.991545099999712
# 0.13342130000000907


def extendleft_list(list1):
    for i in range(10 ** 3):
        list1.insert(0, [1, 2, 3, 4])


def extendleft_deque(deque1):
    for i in range(10 ** 3):
        deque1.extendleft([1, 2, 3, 4])


# print('Метод extendleft:')
# print(timeit('extendleft_list(my_list.copy())', globals=globals(), number=10), '- Список')
# print(timeit('extendleft_deque(my_deque.copy())', globals=globals(), number=10), '- Дек')
# 6.073768799999925
# 0.13724529999944934


def check_list():
    for i in range(100, 1000):
        my_list[i] = i


def check_deque():
    for i in range(100, 1000):
        my_deque[i] = i


print('Получение случайных элементов:')
print(timeit('check_list()', globals=globals(), number=10000), '- Список')
print(timeit('check_deque()', globals=globals(), number=10000), '- Дек')
# 0.30828139999994164
# 0.43437119999998686
'''
1) Методы append, pop и extend списка и дека показывают примерно одно время.
2) Во всех операциях дек оказался гораздо быстрее.
3) Получение случайных элементов быстрее у списка.
'''