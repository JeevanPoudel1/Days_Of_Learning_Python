class student:
    def __init__(self, name):
        self.name = name

class teacher:
    def __init__(self, teacher_name):
        self.n = teacher_name


s1 = student("apple")
print(s1.name)
del s1
#print(s1.name) creates an error as s1 is deleted

s2 =teacher("a")
print(s2.n)


class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1= Account("123456", "abcde")

print(acc1.acc_no)
#print(acc1.__acc_pass)    #will throw error as the acc_pass is private

#can access as it's inside class
print(acc1.reset_pass())

