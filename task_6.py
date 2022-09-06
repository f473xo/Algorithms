"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""


import random


def guessing_game(num=random.randint(0, 100), attempt=10):
    if attempt > 0:
        trying = int(input("Угадайте число: "))
        if trying == num:
            print("Вы победили!")
        elif trying > num:
            print("Перебор.")
            attempt -= 1
            return guessing_game(num=num, attempt=attempt)
        elif trying < num:
            print("Недобор.")
            attempt -= 1
            return guessing_game(num=num, attempt=attempt)
    else:
        print(f"Тренируйте интуицию ведь правильный ответ: {num}")


guessing_game()
