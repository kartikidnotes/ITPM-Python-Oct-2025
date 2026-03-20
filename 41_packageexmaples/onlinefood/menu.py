menu_items={
    "Pizza":300,
    "Burger":250,
    "Pasta":400
}


def show_menu():
    print("======== MENU ============")
    for item,price in menu_items.items():
        print(item, " :: ", price)