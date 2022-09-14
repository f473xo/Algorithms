"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""

import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    max_el = sorted([(i, array.count(i)) for i in set(array)], key=lambda t: t[1])[-1]
    return f'Чаще всего встречается число {max_el[0]} оно появилось в массиве {max_el[1]} раз(а)'


print(func_1())
print(func_2())


print(timeit.timeit("func_1()", setup="from __main__ import func_1", number=10000))
print(timeit.timeit("func_2()", setup="from __main__ import func_2", number=10000))
print(timeit.timeit("func_3()", setup="from __main__ import func_3", number=10000))

"""
func_1: 0.010185399999954825
func_2: 0.014293000000179745
func_3: 0.01580820000026506
Первый вариант показывает наибольшую эффективность, ускорить процесс не удалось.
"""
