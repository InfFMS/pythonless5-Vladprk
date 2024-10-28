# Напишите программу, которая удаляет дубликаты из списка длины N.
# Пример работы:
# Пример: ввод N = 8
# [10, 20, 10, 20, 30, 40, 30, 50]
# После удаления дублей:  [10, 20, 30, 40, 50]
from random import randint as ran
n = int(input())
x = []
mad_mas = []
for i in range(n):
    elem = ran(0, 10)
    x.append(elem)
for i in range(n):
    mad_mas_ = str(mad_mas)
    if mad_mas_.find(str(x[i])) == -1:
        mad_mas.append(x[i])
print(mad_mas)
