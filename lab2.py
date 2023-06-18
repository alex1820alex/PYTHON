try:
    str_1=int(input("Введите число"))
    if str_1%5==0:
        print("Это число",str_1,"делиться на 5")
    else:
        print("Это число",str_1,"не делиться на 5")


except ValueError:
    print("Введите число")
