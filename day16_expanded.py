def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")

    with open("students.txt", "a") as file:
        file.write(name + "," + age + "\n")

    print("Student added!")


def display_students():
    try:
        with open("students.txt", "r") as file:
            students = file.readlines()

        if not students:
            print("No students found.")
        else:
            print("\n--- Students ---")
            for i, student in enumerate(students, 1):
                name, age = student.strip().split(",")
                print(i, name, age)

    except FileNotFoundError:
        print("No student data found.")


def remove_student():
    display_students()

    try:
        number = int(input("Enter student number to remove: "))

        with open("students.txt", "r") as file:
            students = file.readlines()

        if 1 <= number <= len(students):
            students.pop(number - 1)

            with open("students.txt", "w") as file:
                file.writelines(students)

            print("Student removed!")
        else:
            print("Invalid student number.")

    except ValueError:
        print("Please enter a number.")


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Remove Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        remove_student()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")