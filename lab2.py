#1. В текстовый файл построчно записаны фамилия и имя каждого учащегося класса и их оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов, и посчитать средний балл по классу.
#2. Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.
str_1="Карасева Анастасия 2 \n" \
      "Бондарев Герман 2 \n" \
      "Кулагина Дарья 4 \n" \
      "Винокурова Василиса 3 \n" \
      "Козлова Дарина 5 \n"
str_3=""
sredni_bal=0
delitel=0
with open("text.txt","w") as file:
    for item in str_1:
        file.write(item)
with open("text.txt","r") as file:
    str_2 = file.readline()
    while str_2:
        for i in range(len(str_2)):
            if str_2[i].isdigit() and int(str_2[i]) < 3:
                for j in range(i+1):
                    str_3 += str_2[j]
                print(str_3)
                str_3 = ""
            elif str_2[i].isdigit():
                sredni_bal+=int(str_2[i])
        delitel += 1
        str_2= file.readline()
print("sredni bal po klassu",sredni_bal/delitel)




file = open('test2.txt', 'w')
str1=input("Введите строку:")+'\n'
while str1:
    file.writelines(str1)
    str1=input("Введите строку:")
    if not str1:
        break
    else:
        str1+="\n"

file.close()
with open('test2.txt', 'r') as file:
    text = file.readline()
    while text:
        print(text,end="")
        text = file.readline()


