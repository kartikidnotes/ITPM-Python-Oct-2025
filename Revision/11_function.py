# block of code which is a reusable code 

# function without arguments 
def demo():
    print("Welcome to Revision Session !!")

demo()

# function with arguments 
def add(a,b):
    print("addition is : ",a+b)

add(5,10)

#func with return statement -- will need extra variable to store the result 
def add(a,b):
    return a+b

result=add(10,10)
print(result)

#factorail
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
    
print(factorial(5))

