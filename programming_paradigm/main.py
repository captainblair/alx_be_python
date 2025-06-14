from library_management import Book, Library  # import our two classes

def main():
    library = Library()  # create a library instance
    library.add_book(Book("Brave New World", "Aldous Huxley"))  # add book 1
    library.add_book(Book("1984", "George Orwell"))  # add book 2

    print("Available books after setup:")  # label for output
    library.list_available_books()  # show all available books

    library.check_out_book("1984")  # check out one book
    print("\nAvailable books after checking out '1984':")  # label for output
    library.list_available_books()  # show remaining books

    library.return_book("1984")  # return the checked-out book
    print("\nAvailable books after returning '1984':")  # label for output
    library.list_available_books()  # show books again

if __name__ == "__main__":
    main()  # run the program
