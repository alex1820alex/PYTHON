#Написать функцию, которая определяет количество разрядов введённого целого числа.
def razryad(int1):
    razryad_chisla=0
    while int1>1:
        int1=int1/10
        razryad_chisla+=1
    return razryad_chisla
int1=int(input("Введите число"))
print("Разряд числа=",razryad(int1))