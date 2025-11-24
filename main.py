from stock import add_book, delete_book, show_all_books
from operation import borrow_book, return_book, renew_book

def main():
    while True:
        print("----- Library Menu -----")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Show All Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Renew Book")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            delete_book()
        elif choice == "3":
            show_all_books()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            renew_book()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()
