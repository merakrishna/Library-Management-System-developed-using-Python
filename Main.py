
class Library:
    def __init__(self, book_file="books.txt"):
        self.book_file = book_file
        self.load_books()

    def load_books(self):
        try:
            with open(self.book_file, "r") as f:
                self.books = [line.strip().split(",") for line in f.readlines()]
        except FileNotFoundError:
            self.books = []

    def save_books(self):
        with open(self.book_file, "w") as f:
            for book in self.books:
                f.write(",".join(book) + "\n")

    def add_book(self, title, author):
        self.books.append([title, author, "Available"])
        self.save_books()
        print("Book added successfully!")

    def view_books(self):
        print("\n---- Library Books ----")
        for b in self.books:
            print(f"Title: {b[0]} | Author: {b[1]} | Status: {b[2]}")
        print("-------------------------")

    def issue_book(self, title):
        for b in self.books:
            if b[0] == title:
                if b[2] == "Available":
                    b[2] = "Issued"
                    self.save_books()
                    print("Book issued successfully!")
                else:
                    print("Book already issued!")
                return
        print("Book not found!")

    def return_book(self, title):
        for b in self.books:
            if b[0] == title:
                if b[2] == "Issued":
                    b[2] = "Available"
                    self.save_books()
                    print("Book returned successfully!")
                else:
                    print("Book was not issued!")
                return
        print("Book not found!")


library = Library()

while True:
    print("\n1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        library.add_book(title, author)

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        title = input("Enter title of book to issue: ")
        library.issue_book(title)

    elif choice == "4":
        title = input("Enter title of book to return: ")
        library.return_book(title)

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
