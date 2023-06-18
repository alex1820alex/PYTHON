#1. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
#2. Сжать массив, удалив из него все элементы, величина которых находится в интервале [а, b].
# Освободившиеся в конце массива элементы заполнить нулями.
import random
mas=list()
for i in range(10):
    mas.append(random.randint(0,100))
for item in mas:
    print(item,end=' ')
print()
min_1=1000
min_2=1000
for item in mas:
    if min_1>=item:
        min_2 = min_1
        min_1=item
print(min_1,min_2)
a=int(input("введите интервал"))
b=int(input(""))
for item in mas:
    if a<=item<=b:
        mas.pop(mas.index(item))
        mas.append(0)
for item in mas:
    print(item,end=' ')
