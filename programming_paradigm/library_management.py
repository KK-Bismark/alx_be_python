# An implementation of a system that tracks books in a library.

class Book:
    """ Book class """
    def __init__(self, title, author):
        """ initializing the attributes."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out


class Library:
    """Library class to store instances of books."""
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """ Add book to the books in the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """ Check out a book from the library."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        """ Return the book to the library."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """ Storage of available books. """
        available_ones = [book for book in self._books if book.is_available()]
        if not available_ones:
            print("No books are available.")
        else:
            for book in available_ones:
                print(f"{book.title} by {book.author}")
