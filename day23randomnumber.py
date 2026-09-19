import random

randomvar = random.randint(0, 10)

while True:
    input_from_user = int(input("Enter a number"))
    if (input_from_user == randomvar):
        print("success")
        break

    else:
        print("Sorry the value was", randomvar)

print("-----Game Over-----")
