import random
n=int(input("Введите количество строк"))
m=int(input("Введите количество столбцов"))
mas=[]
for i in range(n):
    mas_0=[]
    for j in range(m):
        mas_0.append(random.randint(-100,100))
    mas.append(mas_0)
for item in mas:
    print(item)
coust=0
for i in range(n):
        coust=0
        for j in range(m):
            coust+=mas[i][j]
            print(mas[i][j],end=" ")
        print("=", coust)



