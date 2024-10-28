# Заполнить массив длины N случайными числами в диапазоне от 10 до 100000 и
# отобрать в другой массив все числа, которые состоят из одинаковых цифр.
# Используйте для этого логическую функцию.
# Пример: ввод N = 4
# [12, 77, 5555, 97]
# Вывод: [77, 5555]
from random import randint as ran


def proverka(n):
    n_ = str(n)
    b = True
    for i in range(len(n_)-1):
        if n_[i] != n_[i+1]:
            return False
    if b:
        return True


n = int(input())
x = []
mad_mas = []
for i in range(n):
    elem = ran(0, 100000)
    x.append(elem)
    if proverka(elem):
        mad_mas.append(elem)
print(mad_mas)
