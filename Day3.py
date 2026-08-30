"""
String Manipulation in Python
"""


astring = "hello world"
print(astring[0:5])  # Output: hello
print(len(astring))  # Output: 11
print(astring.upper())  # Output: HELLO WORLD
print(astring.index("o"))  # Output: 4
print(astring.count("l"))  # Output: 3
print(astring[3:7:2])  # Output: lo
print(astring[::-1])  # Output: dlrow olleh
print(astring.startswith("hello"))  # Output: True
print(astring.endswith("anonsdg"))  # Output: False
afewwords = astring.split(" ")


s = "Hey there! what should this string be?"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))


#conditional statements
"""
    Python supports the usual logical conditions from mathematics:
    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b
"""

x=2
print(x==2) # True because 2 is equal to 2
print(x==3) # False because 2 is not equal to 3

Equipment = "Computer"
if Equipment == "Computer":
    print("I have a Computer")
#I have a computer

name = "Jeevan"
age = 23
if name == "Jeevan" and age == 23:
    print("My name is :", name)
    print("My age is :", age)
#My name is : Jeevan
#My age is : 23



if name in ["Jeevan", "Hari", "Sita"]:
    print("Your name is in the list")
#Your name is in the list


x = [1,2,3,4,5]
y = [1,2,3,4,5]
print(x==y) # True because lists x and y have the same elements
print(x is y) # False because lists x and y are not the same object in memory


number =10
second_number = 20
first_array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
second_array = [1,2,3]

if number > 15:
    print("1")
else:
    print("number is less than 15")
#number is less than 15

if first_array:
    print("2")

if len(second_array) ==2:
    print("3")
elif len(second_array) == 3: #prints(4) because the length of second_array is 3
    print("4")

if len(first_array) + len(second_array) == 5  or len(first_array) + len(second_array) == 23: 
    print("4")#prints(4) because the length of first_array is 20 and second_array is 3