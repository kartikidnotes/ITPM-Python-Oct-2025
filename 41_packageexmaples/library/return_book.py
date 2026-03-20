from .books import book_list

def return_book(book_name):
    book_list.append(book_name)

    print("Book Returned Successfully!!!")
