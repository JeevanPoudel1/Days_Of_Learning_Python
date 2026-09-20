import csv
'''
names = []
for name in range(3):
    names.append(input("what's your name"))

for nam in sorted(names):
    print(f"hello, {nam}")

name = input("what's your name?")
with open("practice.txt", "a") as file:
    file.write(f"{name}\n")

#file.close()
with open("practice.txt", "r") as file:
    lines = file.readline()

for line in lines:
    print("hello", line.rstrip())

with open("practice.txt", "r") as file:
    for line in file:
        print("hello", line.rstrip())
names = []
with open("practice.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello,{name}")
students=[]
with open("names.csv") as file:
    for line in file:
        name, house= line.strip().split(",")
        print(f"{name} is in {house}")

for student in sorted(students):
    print(students)

students = []

with open("students.csv") as file:
    for line in file:
        name,house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}") 


students = []

with open("students.csv") as file:
    reader =csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted (students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

'''

