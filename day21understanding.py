def calc_sum(a,b):
    return a + b

def calc_product(a,b):
    return a * b

def calc_difference(a,b):
    return a - b

def calc_quotient(a,b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

def user_input():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers.")
        return None, None

print("Welcome to the calculator program!")
num1, num2 = user_input()

if num1 is not None and num2 is not None:
    print(f"Sum: {calc_sum(num1, num2)}")
    print(f"Product: {calc_product(num1, num2)}")
    print(f"Difference: {calc_difference(num1, num2)}")
    print(f"Quotient: {calc_quotient(num1, num2)}")


print("\nNow, let's modify the print statements to use commas instead of f-strings and curly braces.")
if num1 is not None and num2 is not None:
    # Removed the f and the curly braces, using commas instead:
    print("Sum:", calc_sum(num1, num2))
    print("Product:", calc_product(num1, num2))
    print("Difference:", calc_difference(num1, num2))
    print("Quotient:", calc_quotient(num1, num2))