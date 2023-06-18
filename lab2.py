#1. В списке, содержащем положительные и отрицательные целые числа, вычислите сумму чётных положительных элементов.
#2. Найти в списке те элементы, значение которых меньше среднего арифметического, взятого от всех элементов списка.
spisok=[1,-2,-3,4,5,6,-7,8,-9]
summa=0
for item in spisok:
    if item>0 and item%2==0:
        summa+=item
print(summa)
summa=0
for item in spisok:
    summa+=item
summa= summa /len(spisok)
print(summa)
for item in spisok:
    if item<summa:
        print(item)