# Введите массив длины N с клавиатуры и найдите (за один проход)
# количество элементов, имеющих максимальное значение.
n = int(input())
x = []
mas_itog = []
max_znach = -10*100
for i in range(n):
    elem = int(input())
    x.append(elem)
    if x[i] > max_znach:
        max_znach = x[i]
        mas_itog = []
        mas_itog.append(x[i])
    if x[i] == max_znach:
        mas_itog.append(x[i])
print(len(mas_itog) - 1)
