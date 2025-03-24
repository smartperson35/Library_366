#Interaction for user using the library sytem
print("       __  __       __")
print("|   |  |_) |_)  /\  |_) \/")
print("|__ |  |_) | \ /  \ ) \  |")
print("__________________________")
name = input("What is your name? ")
print(f"Hello {name}!")
#Define the Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True #Default state is available
    def borrow(self):
        if self.is_available == False:
            return True
        return False
    def return_book(self):
        self.is_available = True
#Define the Member class
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = [] #List to track borrowed books
    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title} is not available.")
    def return_book(self, book):
        if book in self.borrowed_books:
           book.return_book()
           self.borrowed_books.remove(book)
           print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} does not have '{book.title}'.")
#Define the Libray class
class Library:
    def __init__(self):
        self.books = [] #List to store books
    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' by {book.author} to the library.")
    def display_books(self):
        print("Books in the library:")
        for book in self.books:
            status = "Available" if book.is_available else "Borrowed"
            print(f"  - {book.title} by {book.author} ({status})")
#Main interaction
#Create a Library
Library = Library()
#Add books to the Library
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")
book3 = Book("To Kill to Makingbird", "Haper Lee")
Library.add_book(book1)
Library.add_book(book2)
Library.add_book(book3)
#Create a Member
member = Member(name)
#Member interacts with the library
Library.display_books       
member.borrow_book(book1)       # Borrow the book
Library.display_books()         # Display status of books
member.return_book(book1)       # Return the book
Library.display_books()         # Display status of books again