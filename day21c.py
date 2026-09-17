#OOP
class student:
    name = "Jeevan"
    age = 20


s1 = student()
print(s1.name)
print(s1.age)
print(s1)


class car:
    color = "Blue"

car1 = car()
print(car.color)


class college():
    name = "Balmiki Lincoln"
    def __init__(self):
        print("Adding Colleges in Birtamode")

c1= college()
print(c1.name)


class university_student():
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks

d1 = university_student("hridesh",99)
print(d1.name, d1.marks)

d2 = university_student("Bibek", 88)
print(d2.name, d2.marks)


