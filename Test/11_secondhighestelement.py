nums=list(map(int,input("Enter Elements in List : ").split()))

highest=nums[0]
second=-999999

for i in nums:
    if i>highest:
        second=highest
        highest=i
    elif i>second and i!=highest:
        second=i

print("Second highest element is : ",second)


