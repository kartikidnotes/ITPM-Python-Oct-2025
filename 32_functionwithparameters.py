
#positional Arguments 
def student(name,marks):
    print(name,marks)

student("Ram",90)


def minnum(a,b):
    if a>b:
        print(a)
    else:
        print(b)
    
minnum(20,70)


#keyword arguments
def emp(name,salary):
    print(name,salary)

emp(salary=50000,name="Ram")


def maxnum(a,b):
    if a>b:
        print(a)
    else:
        print(b)

maxnum(b=9,a=5)

#default arguments 
def country(name,countryname="India"):
    print(name,countryname)

country("Rahul")
country("John","USA")



def multiply(num,factor=2):
    print(num*factor)

multiply(2)
multiply(5*3)
#5*3 will be considered as one number stored in num variable 
multiply(5*3,3)
multiply(5,3)

#positional Arguments 
def student(name,marks):
    print(name,marks)

student("Ram",90)


def minnum(a,b):
    if a>b:
        print(a)
    else:
        print(b)
    
minnum(20,70)


#keyword arguments
def emp(name,salary):
    print(name,salary)

emp(salary=50000,name="Ram")


def maxnum(a,b):
    if a>b:
        print(a)
    else:
        print(b)

maxnum(b=9,a=5)

#default arguments 
def country(name,countryname="India"):
    print(name,countryname)

country("Rahul")
country("John","USA")



def multiply(num,factor=2):
    print(num*factor)

multiply(2)
multiply(5*3)
#5*3 will be considered as one number stored in num variable 
multiply(5*3,3)
multiply(5,3)

