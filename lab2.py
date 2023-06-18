try:
    int_1=int(input("Введите трехзначное число"))
    if 100<int_1<1000:
        summa=int(str(int_1)[0])+int(str(int_1)[1])+int(str(int_1)[2])
        print("Сумма трех цифр числа:",summa)
    else:
        print("Не трехзначное число")
except ValueError:
    print("Введите число")