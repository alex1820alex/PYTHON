#Найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
try:
    int_1=int(input("Введите число"))
    minimal=int(str(int_1)[0])
    maximum=int(str(int_1)[0])
    id_minimal=0
    id_maximum=0
    summa=0
    shag=1
    for i in range(len(str(int_1))):
        if minimal>=int(str(int_1)[i]):
            minimal=int(str(int_1)[i])
            id_minimal = i
        if maximum<=int(str(int_1)[i]):
            maximum=int(str(int_1)[i])
            id_maximum = i
    if id_minimal>id_maximum:
        shag=-1
    for i in range(id_minimal+shag,id_maximum,shag):
        summa+=int(str(int_1)[i])
    print(summa)
except ValueError:
    print("Введите  число")
