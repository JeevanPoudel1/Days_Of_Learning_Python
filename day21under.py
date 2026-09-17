f = open("marks.txt", "r")
data =f.read()
print(data)

f= open("marks.txt", "a")
f.write("New student data")
f.close()

f = open("marks.txt", "r")
data =f.read()
print(data)
f.close()


