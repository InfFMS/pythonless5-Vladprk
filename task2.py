# Заполните массив длины N случайными числами в интервале [0,5].
# Определить, есть ли в нем элементы с одинаковыми значениями, стоящие рядом.
# Если есть, то выведете значение и индекс повторяющихся элементов
# Если нет, то написать "Нет"
# Пример: ввод N = 7
# [1, 2, 3, 3, 2, 2, 1]
# Вывод:
# значение:3 индексы 2 и 3
# значение:2 индексы 4 и 5
from random import randint as ran
mas = []
mas_i = [7]
element = 0
count = 1
x1 = 7
b = False
n = int(input())
for i in range(n):
    x = ran(0, 5)
    mas.append(x)
    if x == x1:
        if mas_i[-1] != i-1:
            mas_i.append(i-1)
            mas_i.pop(mas_i.index(7))
        b = True
        element = x
        mas_i.append(i)
    else:
        if b:
            result = ''.join(str(mas_i))
            print(f'значение: {element}, индексы {result}')
            b = False
            mas_i = [7]
        else:
            mas_i = [7]
    x1 = x
print(mas)





