balance=20000

def check_balance():
    print("Your Balance is : ",balance,"\n")


def deposit():
    global balance
    amount=int(input("Enter amount to Deposit : "))
    balance+=amount
    print("Amount Deposited is : ",amount,"\n")
    print("Your Balance is : ",balance,"\n")


def withdraw():
    global balance
    amount=int(input("Enter amount to withdraw : "))
    if amount>balance:
          print("Insufficient Balance to WIthdraw !!!")
    else:
        balance-=amount
        print("Amount Deposited is : ",amount,"\n")
        print("Your Balance is : ",balance,"\n")
        
def menu():
    while True:
        print("============ Menu =============")
        print("1. Check Balance")
        print("2.Deposit")
        print("3. Withdraw")
        print("4. Exit")

        ch=int(input("Enter your choice from Above :  "))
        if ch==1:
            check_balance()
        elif ch==2:
            deposit()
        elif ch==3:
            withdraw()
        elif ch==4:
            print("Thank You For using ATM!!!")
            break
        else:
            print("Invalid Choice ! Please Enter COrrect Option !")

menu()

  
