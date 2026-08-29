one = 1
two = 2
three = 3
print (three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

a,b = 10, 20
print(a, b)

mystring = "hello"
myfloat = 10.0
Myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(Myint, int) and Myint == 20:
    print("Integer: %d" % Myint)



mylist = []
mylist.append(1)
mylist.append(2)
print(mylist[0])

for i in mylist:
    print(i)

number = []
strings = []

number.append(3)
number.append(4)
number.append(5)
strings.append("hello")
strings.append("world")


second_strings = strings[1]

print(number)
print(strings)
print("the second name of the sting is:", second_strings)

addition = number[0] + number[1] + number[2]
print("the addition of the numbers is:", addition)

number.append(8.12)
print(number)
remainder = number[2] % 2
remainder1 = 11 % 3
print("the remainder of the number is:", remainder)
print("the remainder of 11/3 is:", remainder1)

z=object()
x = object()
y = object()

z_list = [z]
x_list = [x]
y_list = [y]
x_list.append(1)
x_list.append(2)
x_list.append(3)

y_list.append("string")
y_list.append([1, 2, 3])

#print(z)

big_list = x_list + y_list
print("z_listcontains %d objects" % len(z_list))
print("x_listcontains %d objects" % len(x_list))
print("y_listcontains %d objects" % len(y_list))
print("big_listcontains %d objects" % len(big_list))   