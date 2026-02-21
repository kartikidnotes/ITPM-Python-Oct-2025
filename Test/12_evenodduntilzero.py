even=[]
odd=[]

while True:
    num=int(input("Enter numbers (Enter 0 to STOP !!) : "))
    if num==0:
        break
    if num % 2 ==0:
        even.append(num)
    else :
        odd.append(num)

print("Even numbers : ",even)
print("Odd numbers : ",odd)
