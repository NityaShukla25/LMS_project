from book import Book

books = []

def add_book():
    book_id = input("Enter Book ID: ")
    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    b = Book(book_id, name, author)
    books.append(b)
    print("Book Added Successfully!\n")


def delete_book():
    book_id = input("Enter Book ID to delete: ")
    for b in books:
        if b.book_id == book_id:
            books.remove(b)
            print("Book Deleted!\n")
            return
    print("Book not found!\n")


def show_all_books():
    print("Book List: \n")
    for b in books:
        b.show_book()
