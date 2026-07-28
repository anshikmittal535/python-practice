f = open("demo.txt" , "r")
data = f.read()
print(data)
print(type(data))


line1 = f.readline()
print(line1)
f.close()

f = open("sample.txt" , "a")
f.write("\n i vansh balo")

f.close()

f = open("demo.text", "r+")
f.write("abc")
print(f.read())
f.close()

f = open("demo.text", "w+")
# f.write("abc")
print(f.read())
f.write ("abc")
f.close()

with open("demo.text" , "r")as f :
    data = f.read()
    print(data)  

with open ("practice.text","w")as f :
    f.write("Hii everyone\nwe are learning file I/O\n")
    f.write("using python.\n I like programming in python.")

with open("practice.text", "r")as f :
    data = f.read()

new_data =  data.replace("java", "python")
print(new_data)

with open ("practice.text","w")as f :
    f.write(new_data)

def check_for_word(): 
    word = "learning"
    with open("practice.text", "r")as f :
        data = f.read()
        if(data.find(word) != -1):
            print("found")
        else: 
            print("not found")

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open ("practice.text","r")as f:
        while data :
            data = f.readline()
            if (word in data):
                print(line_no)
            line_no += 1

    return -1
check_for_line()



