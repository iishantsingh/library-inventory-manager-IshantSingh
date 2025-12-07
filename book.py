FILENAME = 'library.txt'

#-------------------------Book Class---------------------------------
class Book:
    def __init__(self,title,author,isbn,status='available'):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {self.status}'
    
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        if self.status == "issued":
            self.status = "available"
            return True
        return False

    def is_available(self):
        return self.status == "available"
    
#-------------------------Inventory Class---------------------------------
class LibraryInventory:
    def __init__(self):
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            with open(FILENAME, 'r') as f:
                for line in f:
                    title, author, isbn, status = line.split(',')
                    self.books.append(Book(title, author, isbn, status))
        except FileNotFoundError:
            pass 

    def save_books(self):
        with open(FILENAME,'w') as f:
            for book in self.books:
                f.write(f'{book.title},{book.author},{book.isbn},{book.status}\n')

    def add_book(self,book):
        self.books.append(book)
        self.save_books()

    def search_by_title(self,title):
        return [book for book in self.books if title.lower() in book.title.lower()]
    
    def search_by_isbn(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def display_all(self):
        return self.books
    
#-------------------------Main Menu---------------------------------
def main():
    inv = LibraryInventory()

    while True:
        print("\n====== Library Menu ======")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book by Title")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            inv.add_book(Book(title, author, isbn))
            print("Book added!")

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            book = inv.search_by_isbn(isbn)
            if book and book.issue():
                inv.save_books()
                print("Book issued!")
            else:
                print("Not available.")

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            book = inv.search_by_isbn(isbn)
            if book and book.return_book():
                inv.save_books()
                print("Book returned!")
            else:
                print("Cannot return.")

        elif choice == "4":
            books = inv.display_all()
            if not books:
                print("No books found.")
            for b in books:
                print(b)

        elif choice == "5":
            title = input("Enter title to search: ")
            results = inv.search_by_title(title)
            if results:
                for b in results:
                    print(b)
            else:
                print("No books found.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()