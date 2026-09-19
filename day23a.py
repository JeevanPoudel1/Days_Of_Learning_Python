class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7)*self.radius **2

    def perimeter(self):
        return 2*(22/7)* self.radius

c1 =circle(21)
print(c1.area())
print(c1.perimeter())


class employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showdetails(self):
        print("role = ", self.role)
        print("depratment = ", self.department)
        print("salary = ", self.salary)

class engineer(employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("engineer", "IT", "75,000")

e1 = employee("accountant", "finance", "90,000")
e1.showdetails()

engg1 = engineer("elon musk", "41")
engg1.showdetails()



class order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price>order2.price

order1 = order("chips", 20)
order2 = order("tea", 50)

print (order2 > order1)