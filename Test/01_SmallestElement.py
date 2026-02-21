nums=list(map(int,input("Enter Numbers : ").split()))

n=int(input("enter N :"))
temp=nums[:]

for _ in range(n-1):
    smallest=temp[0]
    idx=0
    for i in range(1,len(temp)):
        if temp[i]<smallest:
            smallest=temp[i]
            idx=i
    temp.pop(idx)

nsmallest=temp[0]
for i in temp:
    if i<nsmallest:
        nsmallest=i

print("Nth Smallest Element is : ",nsmallest)







