# При анализе данных, собранных в рамках научного эксперимента,
# бывает полезно удалить самое большое и самое маленькое значение.
# Сымитруем данные списком длины N со случайными числами в диапазоне от 0 до 1000
# Удалите из этого списка все значения, которые на 30 % отличаются
# от среднего значения списка
from random import randint as ran
n = int(input())
x = []
mas_itog = []
summ = 0
for i in range(n):
    elem = ran(0, 1000)
    summ += elem
    x.append(elem)
sr_arifm = summ/n
print(sr_arifm)
for i in range(n):
    if 1.3*sr_arifm < x[i] or x[i] < 0.7*sr_arifm:
        x[i] = -1
    else:
        mas_itog.append(x[i])
print(mas_itog)
print(len(mas_itog))