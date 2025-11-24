from stock import books

def borrow_book():
    book_id = input("Enter Book ID to borrow: ")
    print("Borrowed Book ID:", book_id, "\n")


def return_book():
    book_id = input("Enter Book ID to return: ")
    print("Returned Book ID:", book_id, "\n")


def renew_book():
    book_id = input("Enter Book ID to renew: ")
    print("Renewed Book ID:", book_id, "\n")
