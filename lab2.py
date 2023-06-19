#Дана строка. Сохранить в ней только первые вхождения символов, удалив все остальные.
# Результат вывести в виде кортежа.
str_1="Hello World"
str_2=str_1
kortej=()
for i in range(len(str_1)):
    if str_1[i] not in kortej:
        kortej+=(str_1[i],)

print(kortej)


