# Shopping Cart Application using Functions

def add_item(cart):
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))

    if name in cart:
        cart[name]['quantity'] += quantity
        print("Item quantity updated!")
    else:
        cart[name] = {'price': price, 'quantity': quantity}
        print("Item added successfully!")


def view_cart(cart):
    if not cart:
        print("Cart is empty!")
        return

    print("-" * 50)
    for item, details in cart.items():
        total = details['price'] * details['quantity']
        print(f"Item: {item} | Price: {details['price']} | Quantity: {details['quantity']} | Total: {total}")
    print("-" * 50)


def remove_item(cart):
    name = input("Enter item name to remove: ")

    if name in cart:
        del cart[name]
        print("Item removed successfully!")
    else:
        print("Item not found in cart!")


def update_quantity(cart):
    name = input("Enter item name to update quantity: ")

    if name in cart:
        add_qty = int(input("Enter quantity to add: "))
        cart[name]['quantity'] += add_qty
        print("Quantity added successfully!")
    else:
        print("Item not found in cart!")



def calculate_total(cart):
    total_amount = 0
    for details in cart.values():
        total_amount += details['price'] * details['quantity']

    print(f"Total Amount to Pay: {total_amount}")


def main():
    cart = {}

    while True:
        print("\n--- Shopping Cart Menu ---")
        print("1. Add Item")
        print("2. View Cart")
        print("3. Remove Item")
        print("4. Update Quantity")
        print("5. Calculate Total")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_item(cart)
        elif choice == '2':
            view_cart(cart)
        elif choice == '3':
            remove_item(cart)
        elif choice == '4':
            update_quantity(cart)
        elif choice == '5':
            calculate_total(cart)
        elif choice == '6':
            print("Thank you for shopping! 😊")
            break
        else:
            print("Invalid choice! Please try again.")


# Run the program
main()