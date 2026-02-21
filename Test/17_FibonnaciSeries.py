# 0,1,1,2,3,5,8,13,21......

def Fibonacci(n):
    a,b=0,1
    for _ in range(n):
        print(a,end=" ")
        a,b=b,a+b

n=int(input("Enter Range for Series : "))
Fibonacci(n)

