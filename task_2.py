"""
Задание 2.
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections
defaultdict(list)
int(, 16)
reduce
2) через ООП
вспомните про перегрузку методов
__mul__
__add__
"""


from collections import defaultdict

dig = '0123456789ABCDEF'
hex_num_dict = defaultdict(list)


def create(string):
    digit_list = []
    for i in string.upper():
        if i in dig:
            digit_list.append(i)
        else:
            raise ValueError('Недопустимое число')
    return digit_list


def add_num(hex_dict):
    res = hex(int(''.join(hex_dict[0]), 16) + int(''.join(hex_dict[1]), 16))
    return create(res[2:])


def mul_num(hex_dict):
    res = hex(int(''.join(hex_dict[0]), 16) * int(''.join(hex_dict[1]), 16))
    return create(res[2:])


def get_numbers():
    try:
        hex_num_dict[0] = create(input('Введите первое число: '))
        hex_num_dict[1] = create(input('Введите второе число: '))
    except ValueError:
        print('Неверный ввод.')
    else:
        print(f'Сумма чисел: {add_num(hex_num_dict)}\n'
              f'Произведение чисел: {mul_num(hex_num_dict)}')


if __name__ == '__main__':
    get_numbers()
