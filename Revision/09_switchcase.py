# it will allow you to give multiple options to user

day=int(input("Enter Day number : "))
match day:
    case 1:
        print("Mon")
    case 2:
        print("Tue")
    case 3:
        print("Wed")
    case _:
        print("Invalid")


a=10
b=20
op=input("Enter input : + , - : ")

match op:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case _:
        print("Invalid ")