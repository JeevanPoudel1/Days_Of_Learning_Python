class addition:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

class subtraction:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def sub(self):
        return self.a - self.b

class multiplication:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def mul(self):
        return self.a * self.b

class division:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def div(self):
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        else:
            return self.a / self.b

calculator = (addition(10, 5),
              subtraction(10, 5),
                multiplication(10, 5),
                division(10, 0), # This will raise a ValueError when div() is called
                division(10, 2)) # This will work fine


print("Addition:", calculator[0].add())  # prints 15
print("Subtraction:", calculator[1].sub())  # prints 5 
print("Multiplication:", calculator[2].mul())  # prints 50
print("Division:", calculator[4].div())  # prints 5.0
print("Division:", calculator[3].div())  # prints infinite or raises ValueError
