class Book:
    def __init__(self, title, author, ISBN, num_copies):
        self.__title = title
        self.__author = author
        self.__ISBN = ISBN
        self.__num_copies = num_copies

    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_ISBN(self):
        return self.__ISBN
    
    def get_num_copies(self):
        return self.__num_copies
    
    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_ISBN(self, ISBN):
        self.__ISBN = ISBN

    def set_num_copies(self, num_copies):
        self.__num_copies = num_copies

    def __str__(self):
        return f"Title: {self.__title}\nAuthor: {self.__author}\nISBN: {self.__ISBN}\nCopies available: {self.__num_copies}"
    
class Member:
    def __init__(self, name, member_id):
        self.__name = name
        self.__member_id = member_id
        self.__books_borrowed = []

    def get_name(self):
        return self.__name
    
    def get_member_id(self):
        return self.__member_id
    
    def get_books_borrowed(self):
        return self.__books_borrowed

    def set_name(self, name):
        self.__name = name

    def set_member_id(self, member_id):
        self.__member_id = member_id

    def borrow_book(self, book):
        self.__books_borrowed.append(book)

    def return_book(self, book):
        if book in self.__books_borrowed:
            return self.__books_borrowed.remove(book)

    def __str__(self):
        return f"Name: {self.__name}\nMember_ID: {self.__member_id}\n"
    
class Library:
    def __init__(self):
        self.__books = []
        self.__members = []

    def add_books(self, book):
        return self.books.append(book)
    
    def add_members(self, member):
        return self.members.append(member)
    
    def borrow_book(self, book, member):
        if book.get_num_copies() < 0:
            
