def m_function():
    print("Hello, World!")

m_function() #prints the function call and prints "Hello, World!"

def my_function_with_args(fname, greeting):
    print("Hello, %s, i wish you %s" % (fname, greeting))
my_function_with_args("Emil", "a great year!") #prints "Hello, Emil, From My function!, i wish you a great year!"

def sumodtwonum(a, b):
    return a + b

result = sumodtwonum(5, 10)
print(result) # prints 15


def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    benefits = list_benefits()
    for benefit in benefits:
        print(build_sentence(benefit))
name_the_benefits_of_functions() 
#prints out the benefits of functions in a sentence format


def greet_user(user_name):
    print("Hello, %s!" % user_name)

greet_user("Jeevan")  # prints "Hello, Jeevan!"

def describe_pet(animal_type, name="Buddy"):
    return f"I have a {animal_type} named {name}."

describe_pet("dog")  # prints "I have a dog named Buddy."
describe_pet("cat", name="Whiskers")  # prints "I have a cat named Whiskers."
describe_pet(animal_type="hamster", name="Nibbles")  # prints "I have a hamster named Nibbles."
#describe() creates a typeError



#global variable
global_msg = "I am global!"  # Global variable

def read_global():
    print(global_msg)  # Functions can read global variables

read_global()  # Prints: I am global!


#Local variable
def my_function():
    local_msg = "I belong to the function!"  # Local variable
    print(local_msg)

my_function()  # Prints: I belong to the function!

# This will crash the program:
#print(local_msg)  # NameError: name 'local_msg' is not defined



#shadowing global variable
x = 10  # Global x

def change_x():
    x = 5  # Local x (shadows the global x)
    print("Inside function:", x)

change_x()  # Prints: Inside function: 5
print("Outside function:", x)  # Prints: Outside function: 10
