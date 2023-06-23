import random
class animal():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def move(self,speed):
        print(self.name,"движеться со скоростью",speed)
    def _info(self):
        print(self.name,self.age,self.sex)

    def __massa(self):
        print(self.name,random.randint(30,60),"кг")
class Wolf(animal):
    def __init__(self,name="Wolf",age="10",sex="Мужской",kol=0):
        super().__init__(name,age,sex)
        self.kol=kol
    def _info(self):
        print(self.name,self.age,self.sex,self.kol)
    def staya(self):
        print("Количество особей в стае",self.kol)

    def __massa(self):
        print(self.name, random.randint(10, 45), "кг")
class Dog(animal):
    def __init__(self,name="Dog",age="10",sex="Мужской"):
        super().__init__(name,age,sex)
    def _info(self):
        print(self.name,self.age,self.sex)
    def move(self):
        print(self.name,"движеться со скоростью",random.randint(1,10))
    def run(self):
        print("Собака бежит")
class Cat(animal):
    def __init__(self, name="Cat", age="10",sex="Мужской"):
        super().__init__(name, age, sex)
    def _info(self):
        print(self.name,self.age,self.sex)
    def sleep(self):
        print("Кот спит")