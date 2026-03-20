from onlinefood import show_menu,place_order,generate_bill

show_menu()

item=input("Enter Item Name :: ")
qty=int(input("Enter Quantity :: "))

total=place_order(item,qty)

generate_bill(total)