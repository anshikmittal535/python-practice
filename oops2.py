class Student:
    def __init__(self , name):
        self.name = name

s1 = Student("shardha")
print(s1)

del(s1)


class Account :
    def __init__(self , account_no , account_pass):
        self.account_no = account_no
        self.__account_pass = account_pass

    def reset_pass(self):
        print(self.__acc__pass)

acc1 = Account("12345" , "abcde")

print(acc1.account_no)
# print(acc1.__account_pass)

class person:
    __name = "anonymous"

    def __hello( self):
        print("hello person!")

    def welcome(self):
        self.__hello()

p1 = person()
print(p1.welcome())


class Car:
    color ="Black"
    @staticmethod 
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class Toyotacar(Car):
    def __init__(self , name ):
        self.name = name

car1 = Toyotacar("fortuner")
car2 = Toyotacar("prius")

print(car1.name)
print(car1.start())
print(car1.color)


#
class car:
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped..")

class Toyotacar(car):
    def __init__(self , brand):
        self.brand = brand


class fortuner(Toyotacar):
    def __init__(self , type):
        self.type = type

car1 = fortuner("diesel")
car1.start()

class A:
    varA = "welcome to class A" 

class B:
    varB = "welcome to class B"

class C(A ,B):
    varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)

# super enharetence

class car:
    def __init__(self , type):
        self.type = type


    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped..")

class Toyotacar(car):
    def __init__(self , name , type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = Toyotacar("plus" , "electric")

print(car1.type)
        
class person:
    name = "anonymous"
    def changename(self , name):
        self.__class__.name = "rahul"

@classmethod
def changename(cls , name):
    cls.name = name

p1 = person()
p1.changename("rahul kumar")
print(p1.name)
print(person.name)  

# property decorator

class student:
    def __init__(self , phy , chem , math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((self.phy + self.chem + self.math )/3) + "%"  # percentage

    # def calcpercentage(self):
       # self.percentage = str((self.phy + self.chem + self.math) /3) + "%"

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = student(98 , 97 ,99)
print(stu1.percentage)

stu1.phy = 86
# print(stu1.phy)
# stu1.calcpercentage()
print(stu1.percentage)

class complex:
    def __init__(self , real , img):
        self.real = real
        self.img = img

    def shownumber(self):
        print(self.real ,"i +" , self.img , "j")

    def __add__(self , num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return complex(newReal , newImg)

num1 = complex(1 ,3)
num1.shownumber()

num2 = complex(4 ,6)
num2.shownumber()

# num3 = num1.add(num2)
num3 = num1 + num2
print(num3)
num3.shownumber()

# def __sub__(self , num2): # substraction
    # newREal = self.real - num2.real
    # newImg = self.Img - num2.img
    # return complex(newREal , newImg)


class circle :
    def __init__(self , radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2* 3.14 * self.radius
    
    
c1 = circle(21)
print(c1.area())
print(c1.perimeter())






                   




 
    

    







     



