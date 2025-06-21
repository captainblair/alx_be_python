# Book class tracks individual book data and availability
class Book:
    def __init__(self, title, author):
        self.title = title  # public attribute for book title
        self.author = author  # public attribute for author name
        self._is_checked_out = False  # private flag to track if book is checked out

    def check_out(self):
        self._is_checked_out = True  # sets the book as unavailable

    def return_book(self):
        self._is_checked_out = False  # makes the book available again

    def is_available(self):
        return not self._is_checked_out  # returns True if book is available


# Library class manages a collection of books
class Library:
    def __init__(self):
        self._books = []  # private list to hold all books in the library

    def add_book(self, book):
        self._books.append(book)  # adds a book to the library collection

    def check_out_book(self, title):
        for book in self._books:  # loop through books
            if book.title == title and book.is_available():  # match title and availability
                book.check_out()  # mark the book as checked out
                print(f"Checked out '{title}'")  # confirmation message
                return
        print(f"Sorry, '{title}' is not available.")  # shown if not found or unavailable

    def return_book(self, title):
        for book in self._books:  # loop through books
            if book.title == title and not book.is_available():  # match title and confirm it's checked out
                book.return_book()  # mark it as returned
                print(f"Returned '{title}'")  # confirmation message
                return
        print(f"'{title}' is either not in the library or not checked out.")  # if not found or already returned

    def list_available_books(self):
        available = [book for book in self._books if book.is_available()]  # filter available books
        if not available:
            print("No books available right now.")  # message when none available
        for book in available:
            print(f"{book.title} by {book.author}")  # list each available book
