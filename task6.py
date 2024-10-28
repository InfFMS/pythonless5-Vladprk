# Массив имеет четное число элементов N.
# Заполнить массив случайными числами и
# выполнить реверс отдельно в первой половине и второй половине.
# Пример: ввод N = 6
# [1,2,3,4,5,6]
# Вывод: [3,2,1,6,5,4]
from random import randint as ran
n = int(input())
x = []
for i in range(n):
    elem = ran(0, 10)
    x.append(elem)
x_ = x[::-1]
mas_1 = x_[n//2:]
mas_2 = x_[:n//2]
print(x)
print(mas_1 + mas_2)
