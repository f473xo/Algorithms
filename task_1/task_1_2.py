'''
Лекция 4, задание 4.

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
'''


from memory_profiler import profile
from random import randint
import numpy as np


@profile
def func_1():
    array = [randint(0, 100000) for i in range(10000)]
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


@profile
def func_2():
    array_np = np.array([randint(0, 100000) for i in range(10000)])
    u, c = np.unique(array_np, return_counts=True)
    m_idx = c.argmax()
    num = u[m_idx]
    m = c[m_idx]

    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


if __name__ == "__main__":
    print(func_1())
    print(func_2())

# До: 38.4 MiB      0.4 MiB       10003       array = [randint(0, 100000) for i in range(10000)]
# После: 38.4 MiB      0.1 MiB       10003       array_np = np.array([randint(0, 100000) for i in range(10000)])
