#1. Вывести на экран столько элементов ряда Фибоначчи, сколько указал пользователь.
# Например, если на ввод поступило число 6, то вывод должен содержать шесть первых чисел ряда Фибоначчи: 1 2 3 5 8 13.
#2. Вычислить факториал введённого числа.
try:
    int_1=int(input("Введите количество элементов Фибоначчи"))
    fib_1 = 0
    fib_2 = 1
    i = 0
    while i < int_1:
        fib_sum = fib_1 + fib_2
        print(fib_sum)
        fib_1 = fib_2
        fib_2 = fib_sum
        i +=1
except ValueError:
    print("Введите количество элементов Фибоначчи")
try:
    int_1=int(input("Введите число"))
    factorial=1
    for i in range(1,int_1+1):
        factorial*=i
    print(factorial)
except ValueError:
    print("Введите число")
