def polezn(func):
    def warrper():
        print("Полезная работа декоратора до")
        func()
        print("Полезная работа декоратора после")
    return warrper
@polezn
def hello():
    print("Hello")
hello()