# Заполнить массив длины N случайными числами в интервале [-100,100] и
# переставить элементы так, чтобы все положительные элементы
# стояли в начала массива, а все отрицательные и нули в конце.
# Пример: ввод N = 6
# [20, -90, 15, -34, 10, 0]
# Вывод: [20, 15, 10, -90, -34, 0]
from random import randint as ran
n = int(input())
x = []
mad_mas = []
for i in range(n):
    elem = ran(-100, 100)
    x.append(elem)
x.sort(reverse=True)
for i in range(n):
    if x[i] == 0:
        x[i] = 101
        mad_mas.append(0)
mas_itog = []
for i in range(n):
    if x[i] != 101:
        mas_itog.append(x[i])
print(mas_itog + mad_mas)
