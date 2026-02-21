# Ordered,Immutable,Faster than List ,allows duplicate elements

t=(10,20,30)
print(t[0])
print(t[2])



# count elements in tuple
# total element == length()
# specific element == if -- 20 elements

t=(10,20,30,20,10,40,50,60,20,20)
count=0

for i in t:
    if i==20:
        count+=1

print("Count of 20 elements is : ",count)