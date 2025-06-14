# library_management.py

class Book:
    """A class to represent a book."""

    def __init__(self, title, author):
        self.title = title                      # Public title attribute
        self.author = author                    # Public author attribute
        self._is_checked_out = False            # Private attribute to track if the book is checked out

    def check_out(self):
        self._is_checked_out = True             # Mark the book as checked out

    def return_book(self):
        self._is_checked_out = False            # Mark the book as returned

    def is_available(self):
        return not self._is_checked_out         # Return True if the book is not checked out


class Library:
    """A class to manage a collection of books."""

    def __init__(self):
        self._books = []                        # Private list to store all book objects

    def add_book(self, book):
        self._books.append(book)                # Add a Book object to the library

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()                # Check out the matching available book
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()              # Return the matching checked-out book
                return
        print(f"Book '{title}' was not checked out or not found.")

    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")  # Print available books
