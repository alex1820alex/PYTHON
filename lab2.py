slovar={
    "dog":"sobaka",
    "cat":"koshaka",
    "home":"dom"
}
str_1=input("Введите слово")
for key,value in slovar.items():
    if str_1==key:
        print(value)
        break
    elif str_1==value:
        print(key)
        break
else:
    print("Перевода нет")


