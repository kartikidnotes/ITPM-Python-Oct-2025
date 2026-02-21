list1=list(map(int,input("Enter Numbers : ").split()))
list2=list(map(int,input("Enter Numbers : ").split()))

common=[]

for i in list1:
    for j in list2:
        if i==j:
            common.append(i)
            break

print("Common Elements are : ",common)



