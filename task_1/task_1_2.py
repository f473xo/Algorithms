# Лекция 4, задание 4.


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
