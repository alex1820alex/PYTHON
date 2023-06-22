#Создать класс и вызвать пять объектов этого класса.
class peaple():
    def __init__(self,age,first_name,last_name,toll,sex):
        self.age=age
        self.first_name=first_name
        self.last_name = last_name
        self.toll=toll
        self.sex=sex

    def hello(self):
        print("Привет", self.first_name,self.last_name,"ваш возраст",self.age,"рост",self.toll,"пол",self.sex)
human1=peaple(26,"Никита","Петроясян","173см","мужчина")
human1.hello()