# Book class
class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        self.available = copies > 0

    # Method to issue a book
    def issue_book(self):
        if self.copies > 0:
            self.copies -= 1
            self.available = self.copies > 0
            print(f"Book issued: {self.title}")
        else:
            print(f"Book not available: {self.title}")

    # Method to return a book
    def return_book(self):
        self.copies += 1
        self.available = True
        print(f"Book returned: {self.title}")

    # Method to check availability
    def is_available(self):
        return self.available

    # Display book details
    def show_details(self):
        print("Title       :", self.title)
        print("Author      :", self.author)
        print("ISBN        :", self.isbn)
        print("Copies      :", self.copies)
        print("Available   :", self.is_available())
        print("-----------------------------")


# Create multiple Book objects
b1 = Book("Python Basics", "Guido", "ISBN101", 3)
b2 = Book("Data Structures", "Mark Allen", "ISBN102", 1)

# Initial status
print("Initial Book Status:")
b1.show_details()
b2.show_details()

# Issue books
b1.issue_book()
b2.issue_book()
b2.issue_book()   # trying to issue when not available

# Return books
b2.return_book()

# Final status
print("\nFinal Book Status:")
b1.show_details()
b2.show_details()
