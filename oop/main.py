from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)

    print(my_book)        # __str__ output
    print(repr(my_book))  # __repr__ output

    del my_book           # __del__ output

if __name__ == "__main__":
    main()
