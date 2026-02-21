nums=list(map(int,input("Enter Numbers in List : ").split()))
positive=[]
negative=[]

for i in nums:
    if i>=0:
        positive.append(i)
    else:
        negative.append(i)

print("Positive numbers : ",positive)
print("Negative numbers : ",negative)