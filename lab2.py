#В зависимости от выбора пользователя, вычислить площадь круга, прямоугольника или треугольника.
#Для вычисления площади каждой фигуры должна быть написана отдельная функция.
import math
def treugl(a,b,c):
    p=a+b+c
    sqr = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return sqr
def krug(r):
    sqr=math.pi*int(r)**2
    return sqr
def pryamougl(a,b):
    sqr=int(a)*int(b)
    return sqr
rezult=1
sqr=0.0
list1=list()
while rezult:
    argument=input("Введите аргумент")
    if argument.isdigit():
        list1.append(argument)
    else:
        break
print(list1)
if len(list1)==1:
    print(krug(list1[0]))
if len(list1)==2:
    print(pryamougl(list1[0],list1[1]))
if len(list1)==3:
    print(treugl(int(list1[0]),int(list1[1]),int(list1[2])))
