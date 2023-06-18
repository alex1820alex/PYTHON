try:
    int_1=int(input("Введите десятизначное число"))
    summa=0
    if len(str(int_1))<10:
        for i in range(len(str(int_1))):
            summa+=int(str(int_1)[i])
        print(summa)
    else:
        print("Введите десятизначное число")

except ValueError:
    print("Введите десятизначное число")
