class Person:
    __name = "anonymus"

    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome())




class car:
    color = "black"
    @staticmethod
    def start():
        print("car Started")

    @staticmethod
    def stop():
        print("car stopped")


class toyotacar(car):
    def __init__(self, name):
        self.name = name

class Fortuner():
    def __init__(self, type):
        self.type = type
'''
car1 = toyotacar("fortuner")
car2 = toyotacar("prius")

print(car1.name)
print(car1.start())
print(car1.color)
'''

car1 = Fortuner("disel")
car.start()