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
    def __init__(self,name,age,sex,kol):
        super().__init__(name,age,sex)
        self.kol=kol
    def staya(self):
        print("Количество особей в стае",self.kol)
class Dog(animal):
    def __init__(self,name,age,sex):
        super().__init__(name,age,sex)

    def run(self):
        print("Собака бежит")
class Cat(animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)

    def sleep(self):
        print("Кот спит")