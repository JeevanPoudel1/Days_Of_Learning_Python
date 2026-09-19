

name = input(str("enter your name"))
name = name.strip().capitalize()
#print("hello, \"friend\"")
print(f"hello, {name}")

x = int(input("enter the x"))
y = int(input("enter the y"))

if x<y:
    print("x is less than y")
elif x>y:
    print("x is greater than y")
else:
    print("x and y is equal")


def main():
    z = int(input("what's z?"))
    if is_even(x):
        print("even")
    else:
        print("odd")

def is_even(n):
    if n%2 ==0:
        return True
    else:
        return False

main()



name_a = input("what's your name")

match name_a:
    case "j":
        print("s")
    case "hridesh":
        print("birtamode")
    case _:
        print("who")

i = 3
while i !=0:
    print("MEOW")
    i = i-1

j =1
while j<=3:
    print("meow")
    j = j+1


for x in [0,1,2]:
    print("a")

for _ in range (3):
    print("b")

print("meow\n" * 3, end="")

while True:
    n = int(input("n=?"))
    if n>0:
        break

for _ in range(n):
    print("meow")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's the value of n"))
        if n>0:
            break
    return n

def meow(n):
    for _ in range (n):
        print("meow")

main()
