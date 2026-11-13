
# Library Management System

class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity
        self.available = quantity


class Library:
    def __init__(self):
        self.books = {}
        self.issued_books = []

    # Add Book
    def add_book(self):
        book_id = input("Enter Book ID: ")

        if book_id in self.books:
            print("Book ID already exists.")
            return

        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        quantity = int(input("Enter Quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        book = Book(book_id, title, author, quantity)
        self.books[book_id] = book

        print("Book added successfully.")

    # View All Books
    def view_books(self):
        if len(self.books) == 0:
            print("No books available.")
            return

        for book in self.books.values():
            print("Book ID:", book.book_id)
            print("Title:", book.title)
            print("Author:", book.author)
            print("Total Quantity:", book.quantity)
            print("Available Quantity:", book.available)
            print()

    # Search Book
    def search_book(self):
        search = input("Enter Book ID or Title: ").lower()
        found = False

        for book in self.books.values():
            if (book.book_id.lower() == search or
                    book.title.lower() == search):

                print("Book ID:", book.book_id)
                print("Title:", book.title)
                print("Author:", book.author)
                print("Available Quantity:", book.available)

                found = True

        if not found:
            print("Book not found.")

    # Issue Book
    def issue_book(self):
        book_id = input("Enter Book ID: ")

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]

        if book.available == 0:
            print("Book is not available.")
            return

        student = input("Enter Student Name: ")

        if student == "":
            print("Student name is required.")
            return

        record = {
            "book_id": book_id,
            "student": student
        }

        self.issued_books.append(record)
        book.available -= 1

        print("Book issued successfully.")

    # Return Book
    def return_book(self):
        book_id = input("Enter Book ID: ")
        student = input("Enter Student Name: ")

        for record in self.issued_books:
            if (record["book_id"] == book_id and
                    record["student"].lower() == student.lower()):

                self.issued_books.remove(record)
                self.books[book_id].available += 1

                print("Book returned successfully.")
                return

        print("Issued book record not found.")

    # Delete Book
    def delete_book(self):
        book_id = input("Enter Book ID: ")

        if book_id not in self.books:
            print("Book not found.")
            return

        for record in self.issued_books:
            if record["book_id"] == book_id:
                print("Book is currently issued.")
                return

        del self.books[book_id]
        print("Book deleted successfully.")

    # View Issued Books
    def view_issued_books(self):
        if len(self.issued_books) == 0:
            print("No books are currently issued.")
            return

        for record in self.issued_books:
            print("Book ID:", record["book_id"])
            print("Student Name:", record["student"])
            print()

    # Main Menu
    def menu(self):
        while True:
            print("\n1. Add Book")
            print("2. View All Books")
            print("3. Search Book")
            print("4. Issue Book")
            print("5. Return Book")
            print("6. Delete Book")
            print("7. View Issued Books")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_book()

            elif choice == "2":
                self.view_books()

            elif choice == "3":
                self.search_book()

            elif choice == "4":
                self.issue_book()

            elif choice == "5":
                self.return_book()

            elif choice == "6":
                self.delete_book()

            elif choice == "7":
                self.view_issued_books()

            elif choice == "8":
                print("Program closed.")
                break

            else:
                print("Invalid choice. Try again.")


# Create Library Object
library = Library()
library.menu()
