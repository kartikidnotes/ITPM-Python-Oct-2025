# inbuilt functions

nums=[10,20,30]
print(len(nums))
print(sum(nums))

# func with argument
def mult(a,b):
    print(a*b)

mult(5,4)

# func with return statment
def square(n):
    return n*n

result=square(5)
print("Square of number is : ",result)


#lambda function
square=lambda x:x*x
print(square(10))

#Positional Argument 
def sub(a,b):
    print(a-b)

sub(10,5)

# Keyword Argument
def sub(a,b):
    print(a-b)

sub(b=20,a=10)


# Default argument function
def power(base,exp=2):
    print(base**exp)

power(5)
power(5,3)

# variable length function

def total(*n):
    sum=0
    for i in n:
        sum+=i
    print(sum)

total(10,20,30,40,50)
total(10,20,30)
total(10,20)