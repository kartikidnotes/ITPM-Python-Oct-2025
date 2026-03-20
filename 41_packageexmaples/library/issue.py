from .books import book_list

def issue_book(book_name):
    if book_name in book_list:
        book_list.remove(book_name)

        print("Book Issue Successfully ")
    else:
        print("Book Not Available !!!")