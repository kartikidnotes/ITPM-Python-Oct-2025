# ============================================
# Write a File

# f=open("sample.txt","w")
# f.write("Hello World \n")
# f.write("File Handling Program ")
# f.close()


# f=open("sample.txt","w")
# f.write("Python Programming \n")
# f.write("File Handling Program in Python ")
# f.close()

# ==============================================


# creating csv file 

# import csv

# with open("data.csv","w",newline="")as f:
#     writer=csv.writer(f)
#     writer.writerow(["Name","Age"])
#     writer.writerow(["Ajay",22])
#     writer.writerow(["Vijay",20])

#read csv file

# import csv
# with open("data.csv","r")as f:
#     reader=csv.reader(f)
#     for row in reader:
#         print(row)


# #append csv file
# import csv
# with open("data.csv","a",newline="") as f:
#     writer=csv.writer(f)
#     writer.writerow(["Raj",30])
#     writer.writerow(["jay",30])

# #apppending multiple records 
# import csv

# rows=[["Samarath",20],["Apeksha",20],["Pratik",20],["Rohan",25],["Om"],25]

# with open("data.csv","a",newline="") as f:
#     writer=csv.writer(f)
#     writer.writerow(rows)
   


# # rows count

# import csv

# with open("data.csv","r") as f:
#     reader=csv.reader(f)
#     print(len(list(reader)))


# fetch records whose age >21

# import csv

#should have a plain csv 
# with open("data.csv","r") as f:
#     reader=csv.DictReader(f)
#     for row in reader:
#         if int(row["Age"])>21:
#             print(row)


# import csv

# #can have plain and dict data 
# with open("data.csv","r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         if "Age" in row and row["Age"] and row["Age"].isdigit():
#             if int(row["Age"]) > 21:
#                 print(row)


# #convert csv to list
# import csv

# data=[]
# with open("data.csv","r") as f:
#     reader=csv.reader(f)
#     for row in reader:
#         data.append(row)

# print(data)





# =======================================

# # write json file

# import json

# data={"productname":"Mobile Phone","price":10000}

# with open("demo.json","w") as f:
#     json.dump(data,f)


# #multiple records 

# import json 

# students=[
#     {
#         "id":1,
#         "name":"Raj",
#         "course":"Python"
#     },
#      {
#         "id":2,
#         "name":"Ram",
#         "course":"MERN"
#     },
#      {
#         "id":3,
#         "name":"Ajay",
#         "course":"MEAN"
#     },
#      {
#         "id":4,
#         "name":"Jay",
#         "course":"Android"
#     },
#      {
#         "id":5,
#         "name":"Om",
#         "course":"Python"
#     }
# ]

# with open("students.json","w") as f:
#     json.dump(students,f,indent=4)

# print("JSON file created successfully")



# #reads a json file

# import json

# with open("students.json","r") as f:
#     data=json.load(f)

# print(data)



# #convert json file to dictonary 

# import json
# text='{"name":"Raj"}'

# print(json.loads(text))



# #pretty print json
# import json

# data={"name":"Raj","age":30}
# print(json.dumps(data,indent=4))


# write list to json

import json

data=[10,20,30,40]
with open("list.json","w") as f:
    json.dump(data,f)


# read list to json
import json

with open("list.json","r") as f:
    data=json.load(f)
print(data)
