# Заполните массив длины N случайными числами в интервале [0,100].
# Определить, есть ли в нем элементы с одинаковыми значениями,
# не обязательно стоящие рядом.
# Если есть, то выведете значение и индекс повторяющихся элементов
# Если нет, то написать "Нет"
# Пример: ввод N = 6
# [1, 2, 3, 2, 5, 10]
# Вывод:
# значение:2 индексы 1 и 3
from random import randint as ran
n = int(input())
x = []
mas_i = []
for i in range(n):
    elem = ran(0, 100)
    x.append(elem)
for i in range(n):
    a = x.index(x[i])
    znach = x[i]
    mas_i.append(a)
    x[i] = -1
    for j in range(0, n):
        if znach == x[j] != -1:
            mas_i.append(x.index(x[j]))
            x[j] = -1
    if len(mas_i) > 1:
        result = ', '.join(map(str, mas_i))
        print(f'значение: {znach}; индексы: {result}')
    else:
        x[i] = znach
    mas_i = []
