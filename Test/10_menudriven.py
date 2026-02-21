def add(a,b): 
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b if b!=0 else "Cannot divide it "

while True:
    print("******* Menu **************")
    print("\n 1. Add \n 2. Subtract  \n 3. Multipliction \n 4. Division : ")
    ch=int(input("Enter Your Choice : "))

    if ch==5:
        break

    a=int(input("Enter a :  "))
    b=int(input("Enter b :  "))

    if ch==1:
        print(add(a,b))
    elif ch==2:
        print(sub(a,b))
    elif ch==3:
        print(mult(a,b))
    elif ch==4:
        print(div(a,b))

