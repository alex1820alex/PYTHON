#1. В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.
# Словом считается последовательность непробельных символов, идущих подряд. Слова разделены одним или большим числом пробелов или символами конца строки.
#2. Дан текст: в первой строке задано число строк, далее идут сами строки. Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
str_1="2\nlol keks hello keks nix pitrom\nkrim moon lol sex keks lol\n"
str_2=""
list_1=list()
dict_1=list()
key=0
for i in range(len(str_1)):
    if str_1[i]!=" " and str_1[i]!="\n":
        str_2+=str_1[i]
    else:
        list_1.append(str_2)
        str_2=""
for item in list_1:
    print(item,end=" ")
print()

set_1=set(list_1)
for item in set_1:
    for item_2 in list_1:
       if item_2==item:
           key+=1
    dict_1.append([key,item])
    key=0
for item in dict_1:
    print(item, end=" ")
print()
maximum=0
for i in range(len(dict_1)):
    if dict_1[i][0]>=maximum:
        maximum=dict_1[i][0]
dict_2=list()
for item in dict_1:
    if maximum==item[0]:
        dict_2.append(item)
minimum=100
for i in range(len(dict_2)):
    if minimum>=len(dict_2[i][1]):
        minimum=len(dict_2[i][1])
for i in range(len(dict_2)):
    if minimum==len(dict_2[i][1]):
        print(dict_2[i][1])










