class Library:

    def __init__(self, listofbooks):
        self.books = listofbooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print(" *", book)

    def borrowBook(self, bookname):
        if bookname in self.books:
            print(f"You have been issued {bookname}. Please keep it safe and return it within 30 days")
            self.books.remove(bookname)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else."
                  " Please wait until the book is available")
            return False

    def returnBook(self, bookname):
        self.books.append(bookname)
        print("Thanks for returning book! Hope you enjoyed reading it")


class Student:

    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of book you want to return: ")
        return self.book


if __name__ == "__main__":
    centralLibrary = Library(["Python", "C++", "Java", "Dot Net", "Scala"])
    # centralLibrary.displayAvailableBooks()

    student = Student()

    while True:
        welcomeMsg = '''\n====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library! Have a great day ahead")
            exit()
