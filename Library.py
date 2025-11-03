class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {self.copies} copies available"

class Library:
    def __init__(self):
        self.books = []
        self.manager_id = ["7426938677855"]

    def add_book(self, book, manager_id):
        if manager_id in self.manager_id:
            self.books.append(book)
            print(f"Book added: {book}")
        else:
            print("Access denied: Invalid manager ID")

    def remove_book(self, isbn, manager_id):
        if manager_id not in self.manager_id:
            print("Access denied: Invalid manager ID")
            return
        
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book removed: {book}")
                return
        print("Book not found.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.copies > 0:
                book.copies -= 1
                print(f"Borrowed: {book}")
                return
        print("Book not available.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.copies += 1
                print(f"Returned: {book}")
                return
        print("Book not recognized.")

def main():
    library = Library()

    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. List of Books")
        print("4. Borrow Book")
        print("5. Return Book")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            manager_id = input("Enter manager ID: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            copies = int(input("Enter number of copies: "))
            book = Book(title, author, isbn, copies)
            library.add_book(book, manager_id)
        elif choice == "2":
            manager_id = input("Enter manager ID: ")
            isbn = input("Enter book ISBN to remove: ")
            library.remove_book(isbn, manager_id)
        elif choice == "3":
            library.list_books()
        elif choice == "4":
            isbn = input("Enter book ISBN to borrow: ")
            library.borrow_book(isbn)
        elif choice == "5":
            isbn = input("Enter book ISBN to return: ")
            library.return_book(isbn)
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()