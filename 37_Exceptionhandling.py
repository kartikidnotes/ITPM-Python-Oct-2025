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


# 13. StopIteration

try:
    nums=iter([1,2])
    print(next(nums))
    print(next(nums))
    print(next(nums))
    print(next(nums))
    print(next(nums))
except StopIteration:
    print("Iteration is already finished ")
