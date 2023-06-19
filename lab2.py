#1. Дано 2 множества, содержащих названия IT-компаний.
# Найти только те компании, которые содержатся в обоих множествах.
#2. Сгенерировать n множеств. Вывести множества кратные трём и не входящие в первое множество.
import random
mnojistva_1={"Лидер Кодинг","MexiNext","КодЭкспресс","Black Fox Testers"}
mnojistva_2={"HardPlay","Creative Codes","Magma Technology","MexiNext"}
print(mnojistva_1 & mnojistva_2)
kortej=list()
n=int(input("Введите кл-во множеств"))
for i in range(n):
    k=random.randint(1,3)
    mnojistva = set()
    for j in range(k):
        mnojistva.add(random.randint(0,5))
    kortej.append(mnojistva)
print(kortej)
for item in (kortej):
    if len(item)%3==0:
        for i in kortej:
            if i.issuperset(item) and i!=item:
                break
            else:
                print(item)
                break

