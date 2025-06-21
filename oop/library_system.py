#Base class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def details(self):
        return f"Book: {self.title} by {self.author}"
    
# Derived class E-Book

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author) # calls the base constructor
        self.file_size = file_size
        
    def details(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"
    
#Derived class PrintBook

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)# Calls the base constructor
        self.page_count = page_count
        
    def details(self):
        return f"Printook: {self.title} by {self.author}, Page Count: {page_count}"
        
    