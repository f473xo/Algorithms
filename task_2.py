"""
Задание 2.
Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.
Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.
Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""


from memory_profiler import profile


def memory(func):

    @profile
    def wrapper(*args, **kwargs):
        return func(*args)

    return wrapper


@memory
def sum_recursion_decorator(num, lst=[0, 0]):

    lst[0 if (num % 10) % 2 == 0 else 1] += 1

    if num < 10:
        return lst

    return sum_recursion(num // 10, lst)


def sum_recursion(num, lst=[0, 0]):

    lst[0 if (num % 10) % 2 == 0 else 1] += 1

    if num < 10:
        return lst

    return sum_recursion(num // 10, lst)


@profile
def foo():
    print(f'Количество четных и нечетных цифр в числе равно: {sum_recursion(int(input("Введите число:")))}')


if __name__ == '__main__':
    foo()
    print(f'Количество четных и нечетных цифр в числе равно: {sum_recursion_decorator(int(input("Введите число:")))}')

'''
Проблема заключается в том, что профилировщик вызывается столько же раз, сколько выполняется рекурсия.
Вывод: Профилирование рекурсии удобнее выполнять когда она находится внутри другой функции.
'''