#1. Придумать и обработать исключения на TypeError и ValueError.
#2. Известны год, номер месяца и день рождения человека, а также день, год и номер месяца сегодняшнего дня. Определите возраст человека (число полных лет).
from datetime import date
try:
    int_1 = int(input("Введите число"))
    int_1+="adsd"
except (ValueError,TypeError):
    print("Ошибка")
data_peaople = date(2000, 9, 18)
data_now=date.today()
print(((data_now-data_peaople)/365).days,"возраст")