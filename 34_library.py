books = []

def add_book():
    bid = int(input("Enter Book Id : "))
    title = input("Enter Book Name : ")
    books.append({"id": bid, "title": title, "issued": False})
    print("Book Added Successfully !!!")


def issue_book():
    bid = int(input("Enter Book ID to issue : "))
    for b in books:
        if b["id"] == bid:
            if not b["issued"]:
                b["issued"] = True
                print("Book Issued Successfully !!!")
            else:
                print("Book Not Available !!")
            return
    print("Invalid Book ID")


def return_book():
    bid = int(input("Enter Book ID to return : "))
    for b in books:
        if b["id"] == bid:
            if b["issued"]:
                b["issued"] = False
                print("Book Returned Successfully !!!")
            else:
                print("Book was not issued")
            return
    print("Invalid Book ID")


def display_books():
    if len(books) == 0:
        print("No books in the library")
        return

    print("Library Books:")
    for book in books:
        if book["issued"] == True:
            print(book["id"], "-", book["title"], "(Issued)")
        else:
            print(book["id"], "-", book["title"], "(Available)")



def book_menu():
    while True:
        print("\n============== MENU ==============")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Display Books")
        print("5. Exit Library")

        ch = int(input("Enter Choice : "))

        if ch == 1:
            add_book()
        elif ch == 2:
            issue_book()
        elif ch == 3:
            return_book()
        elif ch == 4:
            display_books()
        elif ch == 5:
            print("Thank you for Visiting our Library !!!")
            break
        else:
            print("Enter Valid Choice from Above !!!!")


book_menu()
