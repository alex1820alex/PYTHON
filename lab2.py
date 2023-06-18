try:
    int_1=int(input("Введите высоту треугольника"))
    for i in range(1,int_1+1):
        for j in range(i):
            print("$",end=' ')
        print()


except ValueError:
    print("Введите высоту треугольника")
