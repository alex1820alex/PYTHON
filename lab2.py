rezult=int(input("Введите число:"))
while rezult:
    str1=input("Введите +,-,*,/")
    if str1=="+":
        chislo2 = int(input("Введите второе число"))
        rezult=(lambda x,y:x+y)(rezult,chislo2)
        print("Результат:",rezult)
    elif str1=="-":
        chislo2 = int(input("Введите второе число"))
        rezult = (lambda x, y: x - y)(rezult, chislo2)
        print("Результат:",rezult)
    elif str1=="*":
        chislo2 = int(input("Введите второе число"))
        rezult = (lambda x, y: x * y)(rezult, chislo2)
        print("Результат:",rezult)
    elif str1=="/":
        chislo2 = int(input("Введите второе число"))
        rezult = (lambda x, y: x / y)(rezult, chislo2)
        print("Результат:",rezult)
    else:
        break