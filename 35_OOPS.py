# define a class 

class Student:
    id=1
    name="Ram"
    marks=90
    course="Python"

#created the object 
s1=Student()
print("Student ID is : ",s1.id)
print("Student Name is : ",s1.name)
print("Student Marks is : ",s1.marks)
print("Student Course is : ",s1.course)



#create the class and object and use of self keyword to point the current object 
#self keyword -- which will hold and point the current object 

class Student:
    def create_student(self):
        self.id = int(input("Enter ID : "))
        self.name = input("Enter Name : ")
        self.marks = float(input("Enter Marks : "))
        self.course = input("Enter Course : ")

    def show(self):
        print("-------------------------------------------------------------------------")
        print("Student ID is :", self.id)
        print("Student Name is :", self.name)
        print("Student Marks is :", self.marks)
        print("Student Course is :", self.course)


# Object creation
s1 = Student()

# Calling member functions
s1.create_student()
s1.show()



# creating multiple objects 
class Employee:
    def add_emp(self):
        self.id=int(input("Enter ID : "))
        self.name=input("Enter Name :")
        self.salary=float(input("Enter Salary : "))
        self.designation=input("Enter Designation :")
        self.department=input("Enter Department  :")

    def show(self):
        print("--------------------------------------------")
        print("--------------------------------------------")
        print("Employee ID is : ",self.id)
        print("Employee Name is : ",self.name)
        print("Employee Salary is : ",self.salary)
        print("Employee Designation is : ",self.designation)
        print("Employee Department is : ",self.department)

e1=Employee()
e2=Employee()

e1.add_emp()
e2.add_emp()

e1.show()
e2.show()



#Object created Inside loop dynamically and called automatically 5 times 

class Sample:
    def show(self):
        print("Object created !!")

for i in range(5):
    Sample().show()



# s=Sample()
# s.show()



# create a reference variable to an object 


class Car:
    def drive(self):
        print("I'm Driving a Car!!!")

c=Car()
ref=c
ref.drive()


# name="ram"
# n=name



#delete an object 

class A:
    print("Hello")

obj=A()
del obj


#create a class Product create 3 objects and print it 


# ========================================================
# Constructor --> is a special member function which i specifically used to initialize the data members 
# Properties : 1. dont have return type 
#              2. it will not return anything 
#             3. it will not have acess modifiers : private ,public 
#             4. there is no need of function call to call a construtor
#             5. Class name === __init__() == declare a constructor 
                    # _init()_ is used to create a constructor 



#default constructor -- no parameters
class Demo:
    def __init__(self):
        print("Default Constructor is Created !!! ")

Demo()



#Parameterized Constructor (which will have parameters )

class Student:
    def __init__(self,name):
        print(name)

Student("Ram Kapoor")
        


# 2 parameters 

class Addition:
    def __init__(self,a,b):
        print(a+b)

Addition(10,80)


class Square:
    def __init__(self,num):
        print(num*num)
    
Square(5)


class Rectangle:
    def __init__(self,l,b):
        print("Area of Rectangle is : ",l*b)

Rectangle(10,5)


# constructor input from user

class User:
    def __init__(self):
        self.name=input("Enter Your Name : ")

u=User()
print("My name is : ",u.name)


# constructor with user input and function 

class Demo:
    def __init__(self):
        self.num=20

    def show(self):
        print("Number is : ",self.num)


d=Demo()
d.show()



# OOPS : Real Time Entity -- Real time programming
# Pillars : 1. Encapsulation
#           2. Abstraction
#           3. Inheritence
#           4. Polymorphism 


# Encapsulation : data members (variables) and member function (function) are bind together in one wrap 
# eg : medicine capsule 



# public variable
class A:
    num=10

print("Variable from class A is : ",A().num)


#public method 
class Demo:
    def show():
        print("This is a show function with public modifier")

Demo().show()


# variable as private

class A:
    def __init__(self):
        self.__x=30
    def show(self):
        print(self.__x)

A().show()

#public
# x=30

# #private
# __x=30


# make a method as priavte


class A:
    def __show(self):
        print("This is show method whch is priavte ")

    def call(self):
        self.__show()

A().call()



#protected 
# to access the protected data member it is necessary to use inheritance 

class A:
    _x=20

class B(A):
    def show(self):
        print("Value of x in Parent Class is : ",self._x)

B().show()




#getter and setter method 

class Student:
    def set(self,id,name):
        self.__name=name
        self.__id=id

    def get(self):
        return self.__name, self.__id
     
s=Student()
s.set(1,"Kartiki")
print(s.get())



# user input in encapsulation

class User:
    def set(self):
        self.__uname=input("Enter Username : ")
        self.__pwd=input("Enter Password : ")

    def get(self):
        print("USername is : ",self.__uname)
        print("Password is : ",self.__pwd)


u=User()
u.set()
u.get()




#Product Details 

class Product:
    def set(self):
        self.__pid=int(input("Enter Product Id :  "))
        self.__name=input("Enter Product Name : ")
        self.__price=float(input("Enter Price : "))

    def get(self):
        print("=========== Product Details =======")
        print("Product ID is : ",self.__pid)
        print("Product Name is : ",self.__name)
        print("Product Price is : ",self.__price)

p=Product()

p.set()
p.get()



# Atm Pin Verification 

class Atm:
    def __init__(self):
        self.__pin=1234

    def verify(self,p):
        print(p==self.__pin)

Atm().verify(1234)



# Inheritance --> Acquring the properties from another
# 2 min classes
# 1 -- base class / parent class 
# 2 -- derived class/child class

# Types : 1. single
#     2. multilevel
# 3. hierichial 
# 4. multiple
# 5. hybrid

#pass -- do nothing -- skip particular line 
# Single Inheritance : one parent - one child 

class A:
    def show(self):
        print("I'm in Parent Classs")

class B(A):
    pass

B().show()




#Single Inheritance

class Employee:
    def emp_info(self):
        self.name=input("Enter your name : ")


class Info(Employee):
    def show(self):
        print("Employee Name is : ",self.name)


i=Info()
i.emp_info()
i.show()



class Bank:
    def bank_name(self):
        self.bname=input("Enter YOur Bank name : ")

class Account(Bank):
    def display(self):
        print("My bank name is : ",self.bname)

a=Account()
a.bank_name()
a.display()




class Student:
    def info(self):
        self.id=int(input("Enter ID : "))
        self.name=input("Enter Name : ")
        self.per=float(input("Enter Pwercentage : "))

class Result(Student):
    def show(self):
        print("============= Result ===========")
        print("Roll No is : ",self.id)
        print("Student Name is : ",self.name)
        print("Student Percentage is : ",self.per)


r=Result()
r.info()
r.show()


class Vehicle:
    def type(self):
        self.vtype=input("Enter Vehicle type : ")

class Car(Vehicle):
    def show(self):
        print("Vehicle Type is : ",self.vtype)

c=Car()
c.type()
c.show()


class User:
    def userdet(self):
        self.username=input("Enter Username : ")
        self.password=input("enter Password : ")

class Login(User):
    def show(self):
        print("============== USer Details ============")
        print("UserName is : ",self.username)
        print("Pssword is : ",self.password)


log=Login()
log.userdet()
log.show()






#Multilevel 

class Company:
    def company(self):
        self.cname=input("Enter Company Name : ")


class Employee(Company):
    def emp(self):
        self.ename=input("Enter Employee Name : ")
        self.esal=int(input("Enter Employee Salary : "))


class Salary(Employee):
    def show(self):
        print("========== Employee Details ============")
        print("Company Name : ",self.cname)
        print("Employee Name : ",self.ename)
        print("Employee Salary: ",self.esal)


s=Salary()
s.company()
s.emp()
s.show()




# College -- Student -- result

class College:
    def col_name(self):
        self.cname=input("Enter College Name : ")


class Student(College):
    def stud_info(self):
        self.id=int(input("Enter Roll no : "))
        self.sname=input("Enter Student Name : ")
        self.per=float(input("Enter Percentage : "))


class Result(Student):
    def show(self):
        print("================ Student Reult ==================")
        print("College Name : ",self.cname)
        print("Student Roll no : ",self.id)
        print("Student Name : ",self.sname)
        print("Percentage : ",self.per)


res=Result()
res.col_name()
res.stud_info()
res.show()# College -- Student -- result

class College:
    def col_name(self):
        self.cname=input("Enter College Name : ")


class Student(College):
    def stud_info(self):
        self.id=int(input("Enter Roll no : "))
        self.sname=input("Enter Student Name : ")
        self.per=float(input("Enter Percentage : "))


class Result(Student):
    def show(self):
        print("================ Student Reult ==================")
        print("College Name : ",self.cname)
        print("Student Roll no : ",self.id)
        print("Student Name : ",self.sname)
        print("Percentage : ",self.per)


res=Result()
res.col_name()
res.stud_info()
res.show()




# Device -- Mobile --- Smartphones

class Device:
    def device(self):
        self.brand=input("Enter Device Brand :: ")

class Mobile(Device):
    def mobile(self):
        self.os=input("Enter OS of Mobile :: ")

class SmartPhone(Mobile):
    def show(self):
        print("============== Device Info ======================")
        print("Device is : ",self.brand)
        print("OS in Mobile is : ",self.os)

sm=SmartPhone()
sm.device()
sm.mobile()
sm.show()


# Bank Example

class Account:
    def acc_det(self):
        self.accno=int(input("Enter Account number :: "))
        self.name=input("Enter Name :: ")

    
class SavingAccount(Account):
    def savingcal(self):
        self.amount=float(input("enter Amount For Saving Account :: "))
        self.s_rate=4
        self.s_interest=(self.amount*self.s_rate)/100

class RecurringAccount(SavingAccount):
    def recurringcal(self):
        self.amount=float(input("Enter Amount For Recurring Account :: "))
        self.months=int(input("Enter Months :: "))
        self.r_rate=7
        self.r_interest=(self.amount*self.r_rate*self.months)/100


class Display(RecurringAccount):
    def show(self):
        print("=================== Account Details =======================")
        print("Account Number : ",self.accno)
        print("Account Holder Name : ",self.name)
        print("Saving Interest  : ",self.s_interest)
        print("Recurring Interest : ",self.r_interest)

    

disp=Display()
disp.acc_det()
disp.savingcal()
disp.recurringcal()
disp.show()




# Single Inheritance --> Library Management

#parent class
class Library:
    #constructor 
    def __init__(self):
        self.library_name="Central Library Of Pune! "

    def show(self):
        print("Library Name Is : ",self.library_name)
    

class BookIssue(Library):
    def issue_book(self):
        self.sname=input("Enter Student NAme : ")
        self.bname=input("Enter Book Name : ")
        print("Book Issued Successfullly !!!! ")

    def showdetails(self):
        print("================== Details =================")
        #called one function from my parent class -- child class
        self.show()
        print("Student Name : ",self.sname)
        print("Book Name : ",self.bname)


obj=BookIssue()
obj.issue_book()
obj.showdetails()





#grandparent class
class Institute:
    def __init__(self):
        self.iname="IT Preneur! "

    def show(self):
        print("Institute NAme :: ",self.iname)

#parent class
class Course(Institute):
    def getcourse(self):
        self.cname=input("Enter your Course Name :: ")
    
    def showcourse(self):
        print("Course Name :: ",self.cname)


#child class
class Student(Course):
    def getstudent(self):
        self.sname=input("Enter Student Name :: ")
    
    def showstudent(self):
        self.show()
        self.showcourse()
        print("Student Namee :: ",self.sname)


obj=Student()
obj.getstudent()
obj.getcourse()
obj.showstudent()




class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
class Student(Person):
    def __init__(self, name, age,marks):
        super().__init__(name, age)
        self.marks=marks

    def display(self):
        print("=========== Details =============")
        print("Name :: ",self.name)
        print("Age :: ",self.age)
        print("Marks :: ",self.marks)

s1=Student("Ram",20,80)
s2=Student("Raj",22,55)
s3=Student("Jay",24,70)

s1.display()
s2.display()
s3.display()


# Multiple Inheritance : 2 or more 2 parent classes and more than 1 child 


class Father:
    def father(self):
        self.fname=input("Enter Father Name :: ")

class Mother:
    def mother(self):
        self.mname=input("Enter Mother Name :: ")


class Child(Father,Mother):
    def show(self):
        self.cname=input("Enter Child Name : ")
        print("============ Details ==========")
        print("My name is :: ",self.cname)
        print("My Father name is :: ",self.fname)
        print("My Mother name is :: ",self.mname)


obj=Child()
obj.father()
obj.mother()
obj.show()



class Camera:
    def cam(self):
        self.camera=input("Enter Camera Sprcification :: ")

class Company:
    def company(self):
        self.companyname=input("Enter Company Name :: ")

class Smartphone(Camera,Company):
    def show(self):
        print("=========== SmartPhone Details ==============")
        print("Company name :: ",self.companyname)
        print("Camera specification :: ",self.camera)


s=Smartphone()
s.cam()
s.company()
s.show()



class Employee:
    def emp(self):
        self.salary=float(input("Enter Salary :: "))

class Bonus:
    def bonus(self):
        self.bonus_amt=float(input("Enter Bonus :: "))


class Salary(Employee,Bonus):
    def show(self):
        print("Total salary is :: ",self.salary+self.bonus_amt)

s=Salary()
s.emp()
s.bonus()
s.show()


class Printer:
    def print_doc(self):
        print("Printing the Document !!!!   ")


class Scanner:
    def scan_doc(self):
        print("Scanning the Documents !!!")

class AllHardware(Printer,Scanner):
    pass

a=AllHardware()
a.print_doc()
a.scan_doc()

        

class Music:
    def music(self):
        song=input("Enter Song Name :: ")
        print("Playing song :: ",song)


class Video:
    def video(self):
        movie=input("Enter Movie Name :: ")
        print("Playing Movie :: ",movie)

class MediaPlayer(Music,Video):
    pass

m=MediaPlayer()
m.music()
m.video()




class Music:
    def music(self):
        song=input("Enter Song Name :: ")
        print("Playing song :: ",song)


class Video:
    def video(self):
        movie=input("Enter Movie Name :: ")
        print("Playing Movie :: ",movie)

class MediaPlayer(Music,Video):
    def show(self):
        self.music()
        self.video()

m=MediaPlayer()
m.show()


# multilevel -- Parent -- child1 -- child2 -- child3 

# hierarchical -- parent -- child1
#                 parent -- child2  
#                 parent -- child3
#                 parent -- child4

class Bank:
    def bank(self):
        self.bname=input("Enter Bank Name :: ")

class Savings(Bank):
    def show(self):
        # self.bank()
        print(self.bname," Saving Account ")
        # print(self.bank()," Saving Account ")



class Current(Bank):
    def display(self):
        print(self.bname," Current Account ")
        # print(self.bank," Current Account ")



s=Savings()
s.bank()
s.show()

c=Current()
c.bank()
c.display()


#print the address of current object 


class Vehicle:
    def vehicle(self):
        self.vehtype=input("Enter Vehicle Type :: ")


class Car(Vehicle):
    def car(self):
        self.vehicle()
        self.cname=input("enter Car Name :: ")
        self.cbrand=input("Enter Brand Name :: ")

    def show(self):
        print("=========== Details ==========")
        print("Vehicle Type :: ",self.vehtype)
        print("Car Name :: ",self.cname)
        print("Car Brand :: ",self.cbrand)


class Bike(Vehicle):
    def bike(self):
        self.vehicle()
        self.bname=input("enter Bike Name :: ")
        self.bbrand=input("Enter Brand Name :: ")

    def show(self):
        print("=========== Details ==========")
        print("Vehicle Type :: ",self.vehtype)
        print("Bike Name :: ",self.bname)
        print("Bike Brand :: ",self.bbrand)


c=Car()
c.car()
c.show()

b=Bike()
b.bike()
b.show()



class Employee:
    def emp(self):
        self.cname=input("Enter Company Name :: ")


class Trainer(Employee):
    def trainer(self):
        self.emp()
        self.tname=input("Enter Trainer Name :: ")
        self.tskill=input("Enter Trainer Skill :: ")
        self.texp=int(input("Enter Trainer Experience :: "))
    def show(self):
        print("========== TRAINER DETAILS ===========")
        print("Company Name :: ",self.cname)
        print("Trainer Name :: ",self.tname)
        print("Trainer Skill :: ",self.tskill)
        print("Trainer exoerience :: ",self.texp)


class Developer(Employee):
    def dev(self):
        self.emp()
        self.dname=input("Enter Developer Name :: ")
        self.dskill=input("Enter Developer Skill :: ")
        self.dexp=int(input("Enter Developer Experience :: "))
    def show(self):
        print("========== DEVELOPER DETAILS ===========")
        print("Company Name :: ",self.cname)
        print("Developer Name :: ",self.dname)
        print("Developer Skill :: ",self.dskill)
        print("Developer experience :: ",self.dexp)

    
t=Trainer()
t.trainer()

d=Developer()
d.dev()

t.show()
d.show()



class Shape():
    def defineshape(self):
        self.sname=input("Enter Shape Name :: ")
        self.sides=int(input("Enter Sides of Shape :: "))

class Circle(Shape):
    def circle(self):
        self.defineshape()

    def show(self):
        print("Shape Name :: ",self.sname)
        print("Shape Sides :: ",self.sides)
        print("\n\n")

class Square(Shape):
    def sqaure(self):
        self.defineshape()

    def show(self):
        print("Shape Name :: ",self.sname)
        print("Shape Sides :: ",self.sides)
        print("\n\n")
    

class Rectangle(Shape):
    def rectangle(self):
        self.defineshape()

    def show(self):
        print("Shape Name :: ",self.sname)
        print("Shape Sides :: ",self.sides)
        print("\n\n")

class Pentagon(Shape):
    def pentagon(self):
        self.defineshape()

    def show(self):
        print("Shape Name :: ",self.sname)
        print("Shape Sides :: ",self.sides)
        print("\n\n")

c=Circle()
c.defineshape()

s=Square()
s.defineshape()

r=Rectangle()
r.defineshape()

p=Pentagon()
p.defineshape()

print("========= Details ==========")
c.show()
s.show()
r.show()
p.show()



class Account:
    def acc(self):
        self.accno=int(input("Enter Account Number :: "))


class Loan(Account):
    def show(self):
        print("Loan Approved for Account number :: ",self.accno)

class Deposit(Account):
    def show(self):
        print("Amount Deposited for Account number :: ",self.accno)


l=Loan()
l.acc()
l.show()


d=Deposit()
d.acc()
d.show()




class Application:
    def app(self):
        self.appname=input("Enter Application Name :: ")


class Website(Application):
    pass

class MobileApp(Application):
    pass

class Product(Website,MobileApp):
    def show(self):
        print("Application which has website and mobile app is :: ",self.appname)


p=Product()
p.app()
p.show()


class University:
     def univerity(self):
        self.uname=input("Enter University Name :: ")


class College(University):
    pass

class Course(University):
    pass

class Student(College,Course):
    def show(self):
        print("University Name : : ",self.uname)

s=Student()
s.univerity()
s.show()


# super() is used to call *methods or constructor of the parent class* from the child class.

# It is mainly used in *Inheritance*.

# ---

#  Why We Use super()?

# 1. To call parent class constructor
# 2. To call parent class methods
# 3. To avoid rewriting same code
# 4. To follow proper OOP structure

# ---
# Basic Syntax

# python
# super().method_name()


# For constructor:

# python
# super().__init__(arguments)



# Super Function Programs

# constructor call using super()

class Person:
    def __init__(self,name):
        self.name=name
        print("Parent Constructor is called")

class Student(Person):
    def __init__(self, name,grade):
        super().__init__(name)
        self.grade=grade
        print("Student Constructor is Called ")
        print("Name : ",self.name)
        print("Grade : ",self.grade)


s1=Student("Ram","A+")




# method calling using super()

class Animal:
    def colour(self):
        print("Animal is in different colours ")

class Cat(Animal):
    def colour(self):
        super().colour()
        print("Cat Colour is White")

c=Cat()
c.colour()




#Real time Example

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def display(self):
        print("Name is :: ",self.name)
        print("Salary is :: ",self.salary)

class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department=department

    def display(self):
        super().display()
        print("Department Name :: ",self.department)
        print("====================================")



m1=Manager("Ram",30000,"HR")
m2=Manager("Raj",50000,"Admin")

m1.display()
m2.display()
