"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет
Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}
Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""


from uuid import uuid4
import hashlib


def hash_url_str(url, a):

    address = input('Введите exit для выхода.\nАдрес: ')
    if address == 'exit':
        return 'Выход'
    else:
        result = hashlib.sha256(salt.encode() + address.encode()).hexdigest()
        print(result)
        if result in url:
            print(f'Хэш уже добавлен')
            return hash_url_str(url, a)
        else:
            print(f'Добавление хэша. {url.append(result)}')
            return hash_url_str(url, a)


url_address = []
salt = uuid4().hex
print(hash_url_str(url_address, salt))
