str_1="Карасева Анастасия 2\n" \
      "Бондарев Герман 2\n" \
      "Кулагина Дарья 4\n" \
      "Винокурова Василиса 3\n" \
      "Козлова Дарина 5\n"
with open("text.txt","w") as file:
    for item in str_1:
        file.write(item)
kol_strok=0
with open("text.txt","r") as file:
    str_2 = file.readline()
    while str_2:
        print("Колличество симвалов:",len(str_2),end=" ")
        str_2=str_2.split(" ")
        print("Колличество слов:", len(str_2))
        str_2=file.readline()
        kol_strok+=1
print("kolichrstvo strok:",kol_strok)

