'''
for disk in range(3):
    print("#")

def main():
    print_column(3)

def print_column(height):
    for t in range (height):
        print("#\n" * height, end="")

main()



def apple():
    print_square(3)

def print_square(size):
    for i in range(size):
        for j in range (size):
            print("#",end="")
        print()

apple()
'''

def getting_val():
    x =get_int()
    print(f"x is {x}")





def get_int():
    while True:
        try:
            x= int(input("enter value: "))
        
        except ValueError:
            print("x is not integer")
        else:
            return x

getting_val()


#print(f"x is {x}")
