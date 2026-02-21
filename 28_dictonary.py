# 

# print(d)

# access specific Attribute
# print(d["name"])

# # Add key and Value
# d["age"]=20
# print(d)

# for k,v in d.items():
#     print(k,v)

#remove key and value
# d.pop("age")
# print(d)


# d=[{"id":1,"name":"Ram","age":20,"marks":90},{"id":1,"name":"Ram","age":20,"marks":90},{"id":1,"name":"Ram","age":20,"marks":90},{"id":1,"name":"Ram","age":20,"marks":90}]

# find keys and values 
# d={"id":1,"name":"Ram","age":20,"marks":90}
# print(d.keys())
# print(d.values())

# # check key existence
# print("name" in d)
# print("address" in d)

# merge two dict
# a={"a":1}
# b={"b":2}
# a.update(b)
# print(a)

# # length of dict
# d={"id":1,"name":"Ram","age":20,"marks":90}
# print(len(d))

# # copy dict to another 
# c={"id":2,"name":"Raj"}
# c=d.copy()
# print(c)


# get()
# d={"name":"Ram"}
# print(d.get("age","Key Not Found!!!"))
# if true --> return value on that particular Key
#     false --> return the given message 

# find keys with max value
# d={"a":10,"b":20,"c":2,"d":30}
# print(max(d,key=d.get))

# dict comprehension
# squares={n:n*n for n in range(1,10)}
# print(squares)

# list
# squares=[n*n for n in range(1,10)]
# print(squares)

# design student marks dict
students={}

while True:
    print("1. Add student 2.Display Students 3. Exit")
    ch=int(input("Enter Any one of option :"))

    if ch==1:
        name=input("Enter Name :")
        marks=int(input("Enter Marks :"))
        students[name]=marks
    elif ch==2:
        print(students)
    else :
        break

