# give two integers in the first line, and more than two integers in the third line
a, b = map(int, input().split())
array = input().split()
total = 0
for each in array:
    total = total + int(each)
print(a, b, total)  # prints the first two integers from the first line and the sum of the integers of the second line