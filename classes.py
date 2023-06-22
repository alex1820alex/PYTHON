import random


class animal():
    def __init__(self,name,age,sex,):
        self.name=name
        self.age=age
        self.sex=sex
    def move(self,speed):
        print(self.name,"движеться со скоростью",speed)
    def info(self):
        print(self.name,self.age,self.sex)

    def massa(self):
        print(self.name,random.randint(30,60),"кг")
