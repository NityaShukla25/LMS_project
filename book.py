class Book:
    def __init__(self, book_id, name, author):
        self.book_id = book_id
        self.name = name
        self.author = author

    def show_book(self):
        print(self.book_id, self.name, self.author)
