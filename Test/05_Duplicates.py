nums=list(map(int,input("Enter Numbers : ").split()))
unique=[]

for i in nums:
    found=False
    for j in unique:
        if i==j:
            found=True
    if not found:
        unique.append(i)

print("After removing Duplicates : ",unique)