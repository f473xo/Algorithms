"""
Задание 1.
Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""


from collections import Counter, deque


class Coding:
    def __init__(self, string):
        self.s = string
        self.code = {}
        self.sort(self.s)

    def sort(self, item):
        self.count = Counter(item)
        self.sort_item = deque(sorted(self.count.items(), key=lambda i: i[1]))
        self.res = self.processing(self.sort_item)
        self.created_tabs(self.res)

    def processing(self, obj):
        if len(obj) != 1:
            weight = obj[0][1] + obj[1][1]
            comb = {0: obj.popleft()[0],
                    1: obj.popleft()[0]}
            for inx, el in enumerate(obj):
                if weight != el[1]:
                    continue
                else:
                    obj.insert(inx, (comb, weight))
                    break
            else:
                obj.append((comb, weight))
            return self.processing(obj)
        else:
            return obj[0][0]

    def created_tabs(self, item, code=''):
        if not isinstance(item, dict):
            self.code[item] = code
        else:
            self.created_tabs(item[0], code=f'{code}0')
            self.created_tabs(item[1], code=f'{code}1')

    def __str__(self):
        self.result = ''
        for el in self.s:
            self.result += str(self.code[el]) + ' '
        return self.result

    def decoding(self, item):
        check_list = item.split(' ')
        res = ''
        for char in check_list:
            for el in self.code.items():
                if char in el:
                    res += el[0]
        return res


s = "pew pew!"
a = Coding(s)
print(a)
print(a.decoding(str(a)))
