# local scope

def show():
    x=10
    print(x)

show()

# print(x) -- error x is not defined 


# global scope 
x=20

def show():
    x=30
    print(x)

show()
print(x)


#global keyword 

x=10

def change():
    global x
    x=50

change()
print(x)


