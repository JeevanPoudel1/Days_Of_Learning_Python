class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_name(self):
        return self.name

    def get_marks(self):
        return self.marks


def get_student_input():
    """Get one student's name and marks from the user."""
    name = input("Enter student name: ").strip()
    while True:
        try:
            marks = int(input("Enter student marks: "))
            break
        except ValueError:
            print("Invalid marks. Please enter an integer.")
    return Student(name, marks)


def open_marks_file(students):
    """Write a list of Student objects to marks.txt."""
    try:
        with open("marks.txt", "a") as file:
            for student in students:
                file.write(f"{student.get_name()},{student.get_marks()}\n")
        print("Marks added!")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


def main():
    students = []

    # Ask how many students to enter
    while True:
        try:
            n = int(input("How many students do you want to enter? "))
            if n <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    # Collect student data
    for i in range(n):
        print(f"\nStudent {i + 1}:")
        student = get_student_input()
        students.append(student)

    # Save to file
    open_marks_file(students)


if __name__ == "__main__":
    main()