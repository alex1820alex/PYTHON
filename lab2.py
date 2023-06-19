#1. Найти максимальный элемент диагонали матрицы.
#2. Вычислить количество отрицательных элементов под главной диагональю матрицы.
import random
m=3
n=3
mas=[]
maximum=-100
for i in range(n):
    mas_0=[]
    for j in range(m):
        mas_0.append(random.randint(-100,100))
    mas.append(mas_0)
for item in mas:
    print(item)
for i in range(n):
    for j in range(m):
        if j == i and maximum < mas[i][j]:
            maximum = mas[i][j]
print(maximum)
coust=0
for i in range(n):
    for j in range(m):
        if j < i and mas[i][j]<0:
            coust+=1
print(coust)