#inbuilt Exceptions

# # 1. zero division

# try:
#     a=int(input("Enter first number "))
#     b=int(input("Enter second number "))
#     print(a/b)
# except ZeroDivisionError:
#     print("Cannot Divide a number by 0")
    


# # 2. datatype Value invalid

# try:
#     num=int("abc")
# except ValueError:
#     print("Invalid Value to Int Datatype ")


# # 3. TypeError 
# try:
#     print(10+"hello")
# except TypeError:
#     print("Different Datatypes cannot be added in same variable ")
# finally:
#     print("Hello World!!!")


# # 4. NameError

# try:
#     print(num)
# except NameError:
#     print("Variable is not Declared till now but used it ")


# # 5. Index Out Of range

# try:
#     lst=[10,20,30,40]
#     print(lst[10])
# except IndexError:
#     print("Index Out Of Range ")


# # 6.KeyError : Dictonary,json

# try:
#     data={"name":"Raj"}
#     print(data["age"])
# except KeyError:
#     print("Key doesnot Found / Exist ")


# # 7.FileNotFound

# try:
#     f=open("abc.txt")
# except FileNotFoundError:
#     print("File DOest not Found!!")


# # 8. attribute Error

# try:
#     num=10
#     num.append(20)
# except AttributeError:
#     print("Attribute Not Found :: Variable type must be list,tuple")


# # 9. ImportError 

# try:
#     import xyzmodule
# except ImportError:
#     print("Module Doesn't Exists or Module Not Found ")


# # 10. ModuleNotfound

# try:
#     import xyzmodule
# except ModuleNotFoundError:
#     print("Module Doesn't Exists or Module Not Found ")


# # 11. OverFlow Error

# import math

# try:
#     print(math.exp(10000))
# except OverflowError:
#     print("Number too large ")

# # 12. AssertionError

# try:
#     num=-5
#     assert num>0
# except AssertionError:
#     print("Assertion is Failed ")


# # 13. StopIteration

# try:
#     nums=iter([1,2])
#     print(next(nums))
#     print(next(nums))
#     print(next(nums))
#     print(next(nums))
#     print(next(nums))
# except StopIteration:
#     print("Iteration is already finished ")


# # 14. Indentation Error 

# try:
#     for i in range (3): 
#     print (i)
# except IndentationError:
#     print("Indentation Error Please Check Syntax ")


# # 15. KeyboardInterupt

# try:
#     while True:
#         pass
# except KeyboardInterrupt:
#     print("Program Interuppted ")

# ==================================================================

# #else block
# try:
#     print(10/2)
# except:
#     print("Error")
# else:
#     print("Program is successfully Executed ")


# #catch all exception

# try:
#     a=int(input())
# except Exception as e:
#     print(e)


# #custom exception
# try:
#     num=int("demo")
# except ValueError as e:
#     print("Custom Exception :: ",e)


# #nested exception

# try:
#     # a=int("demo")
#     try:
#         print(10/0)
#     except ZeroDivisionError:
#         print("Cannot divide by 0 : exception by Inner except block ")
# except:
#     print("Check Datatype :: Outer Try except")



# #raise exception
# age=15
# if age<18:
#     raise Exception("Not Eligible For Voting")
# else:
#     print("Eligible for Voting")


# #finally with return
# def fun():
#     try:
#         return 1
#     finally:
#         print("Always IN Running mode")

# print(fun())


# ===================================== CUSTOM EXCEPTION ============================

# #SYNTAX

# class MyError(Exception):
#     pass

# raise MyError("this is a custome exception ")


# # 1. Age Validation

# class AgeCalculate(Exception):
#     pass

# age=int(input("Enter age :: "))

# if age<18:
#     raise AgeCalculate("You are not eligible for Voting ")
# else:
#     print("Eligible for Voting")



# # Password Check -- min -- 8 
# class PasswordCheckerError(Exception):
#     pass

# password=input("Enter Password :: ")

# if len(password)<8:
#     raise PasswordCheckerError("Password length must be minimum 8 Characters ")
# else:
#     print("Password set successfully ")


# # 3. Atm withdrawl

# class WithdrawError(Exception):
#     pass

# balance=50000
# amt=float(input("enter amount to withdraw :: "))

# if amt>balance:
#     raise WithdrawError("Insufficient Error ")
# else:
#     balance=balance-amt
#     print("Amount Withdrwan Successfully !!! ")
#     print("Current Balance :: ",balance)


# # 4 Email validation

# class EmailValidError(Exception):
#     pass

# email=input("enter email id :: ")

# if "@" not in email:
#     raise EmailValidError("Must Include @ sign in email ")
# else:
#     print("Valid Email ID ")


# # 5. Username Validation

# class UserNameError(Exception):
#     pass

# username=input("Enter Username :: ")

# if len(username)>8:
#     raise UserNameError("Username must be less than 8 characters ")
# else:
#     print("User Created ")


# # 6. Product Stock Product

# class StockCheckError(Exception):
#     pass

# stock=20

# order=int(input("Enter Quantity :: "))

# if order>stock:
#     raise StockCheckError("Product Out Of Stock ")
# else:
#     stock=stock-order
#     print("Order Placed Successfully")
#     print("Current Stock :: ",stock)


# # 7. Check the temperature

# class TempCheckError(Exception):
#     pass

# temp=float(input("Enter Temperature :: "))

# if temp>50:
#     raise TempCheckError("Temperature too high !!!")
# else:
#     print("Temperature is Normal ")



#  # 8. Salary Validation

# class SalaryError(Exception):
#     pass

# salary=int(input("Enter Salary :: "))

# if salary<10000:
#     raise SalaryError("Salary is low ")
# else:
#     print("Salary is : ",salary)


# # 9. Login attempt 

# class LoginError(Exception):
#     pass

# attempts=int(input("Enter Attempts for Login :: "))

# if attempts>3:
#     raise LoginError("Account is Blocked For 24 Hours ")
# else:
#     print("Login Done")



# #10 File Size
# class FileSizeError(Exception):
#     pass

# size=int(input("Enter Size Of File :: "))

# if size>5:
#     raise FileSizeError("File Too Large ")
# else:
#     print("File Uploaded")


# # 11. mobile number

# class MobileError(Exception):
#     pass

# mobile=input("Enter Mobile Number :: ")

# if len(mobile)!=10:
#     raise MobileError("Invalid number , Mobile number must be 10 digit only ")
# else:
#     print("Valid Mobile Number ")


# # 12 MARKS VALIDATION 

# class MarksError(Exception):
#     pass

# marks=int(input("Enter Mobile Number :: "))

# if marks<0 and marks>100:
#     raise MarksError("Marks Entered is Incorrect ")
# else:
#     print("Valid Marks")


# #13 Check Internet Data Limit 

# class DataLimitError(Exception):
#     pass

# datalimit=int(input("Enter Data Usage(GB) :: "))

# if datalimit>2:
#     raise DataLimitError("Daily Data Limit HAs Exceeded!!!")
# else:
#     print("Data is Still Left ")


# # 14 Cart Limit =10 
# class CartError(Exception):
#     pass

# items=int(input("enter Number of Items :: "))

# if items>10:
#     raise CartError("Cart Limit is only 10 Products ")
# else:
#     print("Item Added to Cart Successfully")

# #15. Exam Attendence -- 75

# class AttendenceError(Exception):
#     pass

# attendence=int(input("Enter Attendnce Percentage :: "))

# if attendence<75:
#     raise AttendenceError("Not Eligible For Exam - Low attendence")
# else:
#     print("Eligible For Exam ")


# # 16. OTP length =6 Digit

# class OTPError(Exception):
#     pass

# otp=input("Enter OTP :: ")

# if len(otp)!=6:
#     raise OTPError("Invalid OTP ")
# else:
#     print("OTP Verified successfully ")
