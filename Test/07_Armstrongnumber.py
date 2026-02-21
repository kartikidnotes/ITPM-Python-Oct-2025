num=int(input("Enter Number : "))
temp=num
digits=0
t=num
while t>0:
    digits+=1
    t//=10
sum=0
while temp>0:
    d=temp%10
    # ** -- power
    sum+=d**digits
    temp//=10

if sum==num:
    print("Armstrong Number ")
else:
    print("Not a Armstrong Number")