import random
# code by Krish

class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}"

class Library:
    def __init__(self):
        self.books = []

    def generate_id(self): 
        existing_ids = {book.book_id for book in self.books} 
        while True: 
            new_id = random.randint(1, 999999) 
            if new_id not in existing_ids: 
                return new_id

    def add_book(self, book): 
        existing_ids = {b.book_id for b in self.books} 
        if book.book_id in existing_ids: 
            book.book_id = self.generate_id() 
        self.books.append(book) 
        if book.book_id > 10:
            print(f"Book '{book.title}' added successfully with ID {book.book_id}.")

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print(f"Book '{book.title}' issued successfully.")
                else:
                    print(f"Book '{book.title}' is already issued.")
                return
        print("Book not found, Please check your input!")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    print(f"Book '{book.title}' returned successfully.")
                else:
                    print(f"Book '{book.title}' was not issued.")
                return
        print("Book not found. Maybe it is a false return!")

    def display_available_books(self):
        print("\nAvailable Books:")
        found = False
        for book in self.books:
            if book.available:
                print(book)
                found = True
        if not found:
            print("No books available, try to donate some books!")

    def search_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(book)
                return
        print("Book not found. Please check your input!")


def main():
    library = Library()

    library.add_book(Book(1, "Can Machine Think Somthing New, The Rise of Autonomus Intelligence", "Krishnendu Mitra"))
    library.add_book(Book(2, "Data Structures with C", "Jane Smith"))
    library.add_book(Book(3, "Algorithms and Analysis", "Robert Brown"))
    library.add_book(Book(4, "Machine Learning with Coffee", "Andrew Ng"))
    library.add_book(Book(5, "Deep Learning and Core of Intelligence", "Ian Goodfellow"))
    library.add_book(Book(6, "Artificial Intelligence", "Stuart Russell"))
    library.add_book(Book(7, "Computer Networks", "James Kurose"))
    library.add_book(Book(8, "Operating Systems", "Abraham Silberschatz"))
    library.add_book(Book(9, "Data Structures with C", "W. Goddfrede"))
    library.add_book(Book(10, "Software Engineering", "Ian Sommerville"))

    print("Welcome to RCCIIT Library, Please choose your option")
    print("\n----- Library Menu -----")
    print("1. Add a new book")
    print("2. Issue a book")
    print("3. Return a book")
    print("4. Display all available books")
    print("5. Search book by title")
    print("Type 'exit' to quit")
    
    while True:
        choice = input("\nEnter your choice: ")

        if choice.lower() == "exit":
            print("Exiting Library System. Goodbye!")
            break

        elif choice == "1":
            try:
                book_id = 1000 #int(input("Enter Book ID: "))
                title = input("Enter Title: ")
                author = input("Enter Author: ")
                library.add_book(Book(book_id, title, author))
            except ValueError:
                print("Invalid input. Book ID must be a number.")

        elif choice == "2":
            try:
                book_id = int(input("Enter Book ID to issue: "))
                library.issue_book(book_id)
            except ValueError:
                print("Invalid input. Book ID must be a number.")

        elif choice == "3":
            try:
                book_id = int(input("Enter Book ID to return: "))
                library.return_book(book_id)
            except ValueError:
                print("Invalid input. Book ID must be a number.")

        elif choice == "4":
            library.display_available_books()

        elif choice == "5":
            title = input("Enter Title to search: ")
            library.search_by_title(title)

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
