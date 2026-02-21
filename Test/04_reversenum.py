num=int(input("Enter Number : "))
temp=num

rev=0

while temp>0:
    rev=rev*10+temp%10
    temp//=10


if num==rev:
    print("Palindrome number")
else:
    print("Not a Palindrome number ")