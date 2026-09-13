students = []

def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    students.append({"name": name, "age": age})
    print("Student added successfully!")

def display_students():
    if not students:
        print("No students found.")
    else:
        print("\n--- Student List ---")
        for i, student in enumerate(students, 1):
            print(f"{i}. Name: {student['name']}, Age: {student['age']}")

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")