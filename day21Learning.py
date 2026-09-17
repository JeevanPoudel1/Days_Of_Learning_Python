#creating a system that takes the data of student 
# #(such as name, mark,age,subject which are predefined) 
# and store in a text file and then read the data from 
# the text file and display it in a formatted way.

class Student:
    def __init__(self, name, mark, age, subject):
        self.name = name
        self.mark = mark
        self.age = age
        self.subject = subject

    def __str__(self):
        return f"Name: {self.name}, Mark: {self.mark}, Age: {self.age}, Subject: {self.subject}"

class subject:
    def __init__(self, name):
        self.name = name
        #subject_list = ["chemistry", "physics", "biology", "mathematics"]

    def __str__(self):
        return f"Subject: {self.name}"

def write_student_data_to_file(student, filename):
    with open(filename, 'a') as file:
        file.write(str(student) + '\n')

def read_student_data_from_file(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
        for line in data:
            print(line.strip())

print("Welcome to the Student Data Management System!")
print("Please enter the student details.")
name = input("Enter the student's name: ")
age = int(input("Enter the student's age: "))
mark = float(input("Enter the student's mark: "))