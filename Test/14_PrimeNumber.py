num= int(input("Enter Number to check whether it is Prime???? : "))

if num<=1:
    print("Negative number Cannot be Prime Number !!! ")
else:
    for i in range(2,num):
        if num%i ==0 :
            print("NOT a Prime number !!!")
            break
        else:
            print("Is a PRIME number ")
            break


# i=2
# 4%2==0
# 5%2==0