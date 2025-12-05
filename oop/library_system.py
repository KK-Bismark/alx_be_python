# A python program that  implement a Library class demonstrating composition
# by managing a collection of books.


class Book:
    def __init__(self, title: str, author: str):
        """Initializes the instance attributes."""
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """Initializes the attributes unique to this class."""
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """Initializes attributes unique to this class."""
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Adds a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)
