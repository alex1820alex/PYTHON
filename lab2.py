#Написать функцию, которая определяет количество разрядов введённого целого числа.
def plus(chislo):
    chislo2=int(input("Введите второе число"))
    rezult=chislo+chislo2
    return rezult
def minus(chislo):
    chislo2 = int(input("Введите второе число"))
    rezult = chislo - chislo2
    return rezult
def umnojenie(chislo):
    chislo2 = int(input("Введите второе число"))
    rezult = chislo * chislo2
    return rezult
def delenie(chislo):
    chislo2 = int(input("Введите второе число"))
    rezult = chislo / chislo2
    return rezult
rezult=int(input("Введите число:"))
while rezult:
    str1=input("Введите +,-,*,/")
    if str1=="+":
        rezult=plus(rezult)
        print("Результат:",rezult)
    elif str1=="-":
        rezult=minus(rezult)
        print("Результат:", rezult)
    elif str1=="*":
        rezult=umnojenie(rezult)
        print("Результат:", rezult)
    elif str1=="/":
        rezult=delenie(rezult)
        print("Результат:", rezult)
    else:
        break


