def sum(a,b):
    return a + b

a = 1
b = 2
c = sum(a,b)
print(c)



y = 5
x = 2
sum = lambda p,q: p + q
c = sum(x,y)
print(c)


#sum = lambda j,k: j + k
l = [2,4,7,3,14,19]
for i in l:
    my_lambda = lambda J : (J % 2) == 1
    print(my_lambda(i))