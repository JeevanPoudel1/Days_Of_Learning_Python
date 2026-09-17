class Students:
    print("Balmiki Lincoln students")
    college_name = "Balmiki Lincoln"
    

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new students")

    def hello(self):
        print("hello", self.name)

    def get_marks(self):
        return self.marks

s1 =Students("keshab", 92)
print(s1.name)
print(s1.marks)
s1.hello()
print("You have a total mark",s1.get_marks())