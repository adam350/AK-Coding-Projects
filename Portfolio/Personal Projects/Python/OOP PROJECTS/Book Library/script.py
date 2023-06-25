class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False 

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        for book in self.books:
            if isbn == book.isbn:
                self.books.remove(book)
                return True
        return False
    
    def check_out_book(self, isbn):
        for book in self.books:
            if isbn == book.isbn:
                if book.checked_out:
                    return False
                else:
                    book.checked_out = True
                    return True
        return False 
    
    def check_in_book(self, isbn):
        for book in self.books:
            if isbn == book.isbn:
                if not book.checked_out:
                    return False
                else:
                    book.checked_out = False
                    return True
        return False 
    
    def display_available_books(self):
        available_books = []
        for book in self.books:
            if book.checked_out == False:
                available_books.append(book)
        if len(available_books) == 0:
            print("No available books.")
        else:
            print("Available books: ")
            for book in available_books:
                print(f"{book.title} by {book.author}")

library = Library()

while True:
    action = input("What would you like to do? (add book, remove book, check out book, check in book, display available books or exit): ")

    if action == 'exit':
        break
    elif action == 'add book':
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        isbn = input("Enter the isbn of the book: ")
        book = Book(title, author, isbn)
        library.add_book(book)
    elif action == 'remove book':
        isbn = input("Enter the isbn of the book: ")
        result = library.remove_book(isbn)
        if result:
            print("Book is removed.")
        else: 
            print("Error. Book not found.")
    elif action == 'check out book':
        isbn = input("Enter the isbn of the book: ")
        result = library.check_out_book(isbn)
        if result:
            print("Book is checked out.")
        else: 
            print("Error. Book is not available.")
    elif action == 'check in book':
        isbn = input("Enter the isbn of the book: ")
        result = library.check_in_book(isbn)
        if result:
            print("Book is checked in.")
        else:
            print("Error. Book is not checked out.")
    elif action == 'display available books':
        library.display_available_books()       
    else:
        print("Error. Invalid action.")
