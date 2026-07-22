info = {
    "key" : "value",
    "name" : "anshika",
    "learning" : "coding",
    "age" : 35,
}
print(info)

info2 = {
    "name" : "anshika",
    "subjeccts" : ["python","c", "java"],
    "topics" : ("dictonary", "sets"),
    "is_adult" : True,
    "age" : 35 

}
print(info2)
print(type(info))
print(info["name"])
print(info2["subjeccts"])
info["name"] = "ruhi"
info["surname"] = "mittal"
print(info)
null_dict = {}
null_dict["name"] = "vansh"
print(null_dict)

#nested dictonary
student = {
    "name" : "rahul kumar",
    "subjects" : {
        "phy" : 98 ,
        "che" : 94 ,
        "math" : 89 
    }
}
print(student)
print(student["subjects"]["che"])
print(student.keys())
print(list(student.keys()))
print(len(student))
print(student.values())
print(list(student.values()))
print(len(list(student.values())))
print(student.items())
print(list(student.items()))
print(len(list(student.items())))
pairs = list(student.items())
print(pairs[0])
print(student["name"])
print(student.get("name"))
student.update({"city" : "delhi"})
print(student)
new_dict = {"name":"neha kumari","age" : 16 }
student.update(new_dict)
print(student)

collection = {1,2,3,4}
print(collection)
print(type(collection))
collection1 = {1,2,2,3 ,"hello", "world","world",4}
print(collection1)
print(len(collection1))
collection = set()
print(type(collection))
collecti1on = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.remove(1)
print(collection)
collection.add((1,8,6,5))
print(collection)
collection.clear()
print(len(collection))
collection = {"hello","world","python","apnacollage"}
print(collection.pop())
print(collection.pop())
set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))

dictonary = {
    "cat": "a small animal",
    "table" : ["a piece of furniture","list of facts and figurs"]

}

print(dictonary)
language = { 
    "python", "java", "c++", "python", "javascript","java" , "python", "java", "c++", "c"
}
print(language)
print(len(language))













