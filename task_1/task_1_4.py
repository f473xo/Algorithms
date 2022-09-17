# Основы Python. Лекция 3, задание 1.


from sys import getsizeof
from collections import namedtuple

def num_translate_adv(value):
    values = {
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять",
    }
    print(f'Размер словаря {getsizeof(num_translate_adv)}')

    print(f'{values.get(value, "Такого слова нет")}')


def new_func(number):
    numbers = namedtuple('numbers', 'one, two, three, four, five,'
                                          'six, seven, eight, nine, ten')
    translate = numbers(one='один', two='два', three='три',
                     four='четыре', five='пять', six='шесть', seven='семь',
                     eight='восемь', nine='девять', ten='десять')
    print(f'Размер кортежа {getsizeof(translate)}')
    return f'{getattr(translate, number.lower(), "Такой цифры нет")}'


if __name__ == '__main__':
    num_translate_adv('one')
    print(new_func('four'))

'''
Размер словаря 144
один
Размер кортежа 120
четыре
'''