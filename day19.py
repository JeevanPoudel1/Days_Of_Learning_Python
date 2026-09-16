
from unicodedata import name


try:
    marks = {}
    x = int(input("Enter the number of subjects: "))
    marks.update({input("Enter subject name: "): 
                  int(input("Enter marks: ")) 
                  for _ in range(x)})
    print(marks)
except ValueError:
    print("Invalid input. Please enter a valid number.")

subject_name = list(marks.keys())[0]
marks_value = list(marks.values())[0]
with open("marks.txt.txt", "a") as file:
        file.write(subject_name + "," + str(marks_value) + "\n")

print("Marks added!")

subject = {
    "python","java","c++","javascript"
}

print(subject)
print(type(subject))
print(len(subject))
print(subject.pop())
print("After pop:",subject)
values = {1, 2, 3, 4, 5}
print(values)
print(type(values))