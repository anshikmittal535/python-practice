count = 1
while count<= 5 :
    print("Hello")
    count += 1 
    print(count)

#print numbers from 1 to 5 
i = 1 
while i <= 5 :
    print(i)
    i+=1
    print("loop ended")

i = 5 
while i >= 1 :
    print(i)
    i-=1 

i = 1
while i <= 100 :
    print(i)
    i+=1

i = 100 
while i >= 1 :
    print(i)
    i-=1   

i = 1
while i<= 10 :
    print(3*i)
    i += 1

i = 1
while i <= 10 :
    print(i**2)
    i += 1

nums =  [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx <= len(nums) - 1 :
    print(nums[idx])
    idx +=1
nums = (1,4,16,25,36,49,64,81,100)

X = 36
i = 0 
while i < len(nums):
    if(nums[i] == X ):
        print("found at index",i)
    i += 1
i = 1 
while i <= 5 :
    print(i)
    if(i == 3):
        break
    i +=1 

i = 0
while i<= 5 :

    if(i == 3):
        i += 1
        continue
    print(i)
    i +=1

nums = [1,2,3,4,5]
for val in nums : 
    print(val)
veggis = ["potato"," tomato","brijal", "lady finger"]
for val  in veggis :
    print(val)

tup = (1,2,3,4,5,6,7,8)
for num in tup :
    print (num)

list = [1,4,9,16,25,36,49,64,81,100]
for el in list :
    print (el) 

tup = (1,4,9,16,25,36,49,64,81,100,49)

x = 49
idx = 0
for el   in tup : 
    if el == x :
        print("number of found at idx", idx)
    idx += 1

seq = range (5)
for i in seq:
    print(i)

for i in range (10) : #range (stop)
    print (i)

for i in range (2,10) : # range (start, stop)
    print (i)

for i in range (2,100,2) :
    print(i)

for i in range (1,101) :
    print(i)

for i in range (100,0, -1):
    print (i) 

n = int(input("enter number:"))

for i in range (1,11) :
    print(n*i)

for i in range (5) :
    pass 
print("some useful work ")


n = 5 

sum = 0 
for i in range (1 , n+1) :
    sum += i 



