class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod 
    def hello():
        print("hello")

    def get_average(self):
        sum=0
        for val in self.marks:
            sum +=val
        print("hi", self.name, "your average score is: ",sum/3)


s1 =student("keshab", [90,99,92])
s1.hello()
s1.get_average()

s1.name = "bibek"
s1.get_average()

