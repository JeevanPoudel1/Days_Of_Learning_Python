class student:
    name = "anonymous"
    @classmethod
    def changeName(cls, name):
        cls.name = name

'''
    def changename(self, name):
        self.__class__.name ="jeevan"
        student.name = "jeevan"
'''


s1 = student()
s1.changeName("jeevan")
print(s1.name)
print(student.name)



class college:
    def __init__(self, phy, chem, math):
        self.phy =phy
        self.chem= chem
        self.math = math
        

    #def calcpercentage(self):
    #   self.percentage = str((self.phy + self.chem+self.math)/3) +"%"

    @property
    def percentage(self):
        return  str((self.phy + self.chem+self.math)/3) +"%"


collegestdn = college(98, 99, 90)
print(collegestdn.percentage)

collegestdn.phy = 90
print(collegestdn.phy)
print(collegestdn.percentage)

#print(collegestdn.calcpercentage)


class complex:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def shownumber(self):
        print(self.real, "i +", self.image, "j")

    def __add__(self, num2):
        newreal= self.real + num2.real
        newimage = self.image + num2.image
        return complex(newreal, newimage)

    def __sub__(self, num2):
            newreal= self.real - num2.real
            newimage = self.image - num2.image
            return complex(newreal, newimage)

num1 = complex(1,3)
num1.shownumber()

num2 = complex(6,7)
num2.shownumber()

#num3 = num1.add(num2)
#num3.shownumber()

num3 = num1 + num2
num3.shownumber()

num4 = num1 - num2
num4.shownumber()
