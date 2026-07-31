class Student :
    name = "karan"
    def __init__(self):
        print("adding new student in database .")

s1 = Student()
print(s1)
print(s1 .name)

s2 = Student()
print(s2.name)

class car:
    color = "blue"
    brand = "mercedes"

c1 = car()
print(c1.color)
print(c1.brand)

#default constructer
def __init__(self):
    pass

class Human:
    name = "Anshika"
    # parameterized constructer
    collage_name = "ABC collage"
    def __init__(self , fullname , marks):
        self.name = fullname
        self.marks = marks
        print("I am learning python")
        print(self)
H1 = Human("karan", 97)
print(H1.name , H1.marks)

H2 = Human("Arjun" , 87)
print(H2.name , H2.marks)

print("vansh agarwal")
print(H2.collage_name) 


class Vish:
    def  __init__(self , fullname, marks):
        self. name =  fullname
        self.marks = marks
    def welcome(self):
        print("welcome college", self.name)

    def get_marks(self):
        return self.marks
v1 = Vish("soumya" , 97)
v1.welcome() 
print(v1.get_marks())

class Student:
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks

    def get_averge(self):
        sum = 0 
        for value in self.marks:
            sum += value
        print("Hi" , self.name , "your averge score is :" , sum/3)

s1 = Student("maithili" , [87,90,98])
s1.get_averge()

class Student:
    @staticmethod #decorator
    def hello():
        print("hello")

Student.hello()

# abstraction
class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False 

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")


car1 = car()
car1.start()

# encapsulation

class Account:
    def __init__(self , bal , acc):
        self.balance = bal 
        self.account_no  = acc


        # debit method 
    def debit(self , amount):
        self.balance -= amount
        print("Rs" , amount , "was debited")
        print("total balance = " , self.get_balance())

    def credit(self , amount):
        self.balance += amount
        print("Rs" , amount , "was credited")
        print("total balance =" , self.get_balance())

    def get_balance(self):
        return(self.balance)    
            

acc1 = Account(10000 , 12345 )
print(acc1.balance)
print(acc1.account_no)
acc1.debit(1000)
acc1.credit(500)

            

    
    
    





