from .menu import menu_items

def place_order(item,quantity):
    if item in menu_items:
        price=menu_items[item]*quantity
        return price
    else:
        print("Item not available  ")
        return 0