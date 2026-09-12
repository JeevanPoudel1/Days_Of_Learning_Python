# Simple Terminal Calculator
print("PYTHON CALCULATOR")


while True:

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "5":
        print("Calculator closed.")
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = num1 + num2

        elif choice == "2":
            result = num1 - num2

        elif choice == "3":
            result = num1 * num2

        elif choice == "4":
            if num2 == 0:
                print("Error: Cannot divide by zero!")
                continue

            result = num1 / num2

        else:
            print("Invalid choice!")
            continue

        print(f"\nResult: {result}")

    except ValueError:
        print("Please enter valid numbers.")
