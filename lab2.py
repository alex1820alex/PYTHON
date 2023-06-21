from kalkulyator.pacet2 import func2, func3
from kalkulyator.pacet1 import func1

rezult=int(input("Введите число:"))
while rezult:
    str1=input("Введите +,-,*,/")
    if str1=="+":
        rezult= func1.plus(rezult)
        print("Результат:",rezult)
    elif str1=="-":
        rezult= func2.minus(rezult)
        print("Результат:", rezult)
    elif str1=="*":
        rezult= func3.umnojenie(rezult)
        print("Результат:", rezult)
    elif str1=="/":
        rezult= func3.delenie(rezult)
        print("Результат:", rezult)
    else:
        break