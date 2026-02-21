# store your data in key and value pair 
# mutable form
# keys must be unique

student={"name":"ram","age":30}
print(student)

# printing keys from dict
for key in student:
    print(key," : ",student[key])

# add and update values in dict 
emp={}
emp["id"]=101
emp["name"]="Raj"
emp["salary"]=10000

print(emp)
emp["salary"]=30000
print(emp)
