# # Online Shopping Cart


# products={
#     "laptop":50000,
#     "mobile phone":20000,
#     "headphone":2000
# }

# total=0

# try:
#     item=input("Enter product name :: ").lower()

#     if item not in products:
#         raise Exception("Product name is invalid !!!!")
    
#     quantity=int(input("Enter Product Qunatity :: "))

#     if quantity<=0:
#         raise Exception("Quantity Must be minimum 1 ")

#     price=products[item]*quantity
#     total=total+price

#     print("Total Bill is :: ",total)

# except ValueError as e:
#     print("Invalid Input ",e)

# except Exception as e:
#     print("Error : ",e)

# finally:
#     print("Thank You For Visit !! ")



# # Username and password Authentication

# username="admin"
# password="admin@1234"

# try:
#     uname=input("Enter Username :: ")
#     upass=input("Enter Password :: ")

#     if uname=="" and upass=="":=
#         raise ValueError("All Fields Are Compulsary !!! ")
    
#     if uname==username and upass==password:
#         print("Login Successful")
#     else:
#         raise Exception("Invalid Username or Password ")
# except ValueError as e:
#     print("Input Error : ",e)
# except Exception as e:
#     print("Login Failed :: ",e)


# # Movie Ticket Booking

# class SeatNotAvailable(Exception):
#     pass

# availabe_seats=10

# while True:
#     print("================ Book Ticket ===============")
#     print("\n 1. Book Ticket ")
#     print("\n 2. Exit")

#     choice=int(input("Enter Choice :: "))

#     if choice==1:
#         try:
#             ticket_count=int(input("Enter Number of tickets you want to book :: "))

#             if ticket_count>availabe_seats:
#                 raise SeatNotAvailable("Enough seats are not Available !!! ")
            
#             availabe_seats=availabe_seats-ticket_count
#             print("Booking done Successfully !!")
#             print("Remaining Seats :: ",availabe_seats)

#         except SeatNotAvailable as e:
#             print("Error :: ",e)
    
#     elif choice==2:
#         print("Thank You For Booking ")
#         break
#     else:
#         print("Invalid Choice")


# ATM Project

class InsufficientBalance(Exception):
    pass

balance=50000

while True:
    print("=========== Menu ==================")
    print("1. Display Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice=int(input("Enter Choice :: "))

    if choice==1:
        print("Your Current Balance is :: ",balance)
    elif choice==2:
        amt=int(input("Enter Amount To Deposit :: "))
        balance=balance+amt
        print("Amount Deposited Successfully ")
        print("Your Current Balance is :: ",balance)
    elif choice==3:
        amt=int(input("Enter Amount To Deposit :: "))
        try:
            if amt>balance:
                raise InsufficientBalance("Insufficient Balance to withdraw!!!")
            balance=balance-amt
            print("Amount Withdraw Successfully ")
            print("Your Current Balance is :: ",balance)
        except InsufficientBalance as e:
            print("Error :: ",e)
    elif choice==4:
        print("Thank YOu For Using ATM ")
        break
    else:
        print("Invalid Choice ")          





