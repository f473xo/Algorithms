"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""


import timeit


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    enter_num_list = list(str(enter_num))
    enter_num_list.reverse()
    return ''.join(enter_num_list)


enter_num = 18556834


print('revers_1:', timeit.timeit('revers_1(enter_num)', globals=globals()))
print('revers_2:', timeit.timeit('revers_2(enter_num)', globals=globals()))
print('revers_3:', timeit.timeit('revers_3(enter_num)', globals=globals()))
print('revers_4:', timeit.timeit('revers_4(enter_num)', globals=globals()))

""""
revers_1: 1.4947672000002967
revers_2: 1.062025100000028
revers_3: 0.25080649999972593
revers_4: 0.4196167999998579

Функция 1: Самая долгая работа из-за рекурсивного вызова.
Функция 2: Цикл и математика. Почти в два раза быстрее первой.
Функция 3: Самый быстрый вариант. Срезы позволяют обрезать список взяв только нужные элементы,
за счет этого выигрывают в скорости.
Функция 4: Встроенные функции списка. Занимает чуть больше времени чем 3.
"""
