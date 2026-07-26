def calc_sum(a , b):
    sum = a + b
    print(sum)
    return sum 

calc_sum(5 , 10)

calc_sum(2 , 10) 

# function  defination
def calc_sum(a ,b): # parameters
    return a + b

sum =  calc_sum(1 ,2) # function call ; arguments 
print(sum)

def print_hello():
    print("Hello")

output = print_hello()
print(output)

# average of 3 numbers

def calc_avg(a ,b ,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg


result =  calc_avg(1 ,2 ,3)
print(result)


print("anshika" ,end = " " ) #sep =  " "
print ("mittal") # end = "/n"

cities = ["delhi" , "puna", "madras" , "gurgaon", "noida", "mumbai"]
heros = ["sharukhkhan" , " thor" , " iornman"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heros)

print(heros[0] , end = " " ),
print(cities[4])

def print_list(list):
    for item in list :
        print(item) 

print_list(heros)
print_list(cities)



def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

calc_fact(6)

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val , "INR")

converter(1)
converter(675)

def number():
    x = int(input("enter a number: "))
    if x % 2 == 0 :
        print("EVEN")
    if x % 2 != 0:
        print("ODD")

number()

#recursive function
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    print("END")

 
show(5) #5 , 4 = n-1 ,3 = n-2 ,2 = n-3 , 1= n-4

def fact(n):
    if(n==1 or n == 0):
        return 1
    return fact(n-1)*n

print(fact(4))




    










