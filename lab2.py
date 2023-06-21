def generait_derict(str1):
    mnojestva=set()
    for i in range(len(str1)):
        mnojestva.add(str1[i])
    key=0
    derict=dict()
    for item in mnojestva:
        for i in range(len(str1)):
            if item==str1[i]:
                key+=1
        derict[item]=key
        key = 0
    for key,val in derict.items():
        print(key,val,end=" ")

str1=input("Введите строку")
generait_derict(str1)
