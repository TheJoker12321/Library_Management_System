from classes.books.book import Book
from classes.users.user import User
class Library:
    max_day_for_lend = 14
    def __init__(self):
        self.books = {}
        self.users = {}

    def register_user(self, user : User):
        self.users[user.user_id] = user

    def add_book(self, book : Book):
        self.books[book.isbn] = book

    def perform_borrow(self, user_id, isbn):
        if user_id not in self.users[user_id].user_id:
            raise AttributeError("this user not in users.")
        if not self.books[isbn].is_available:
            raise "this book not found"
        book = self.books[isbn]
        self.users[user_id].borrow_book(book)
        book.isavailable = False


    def return_borrow(self, user_id, isbn):
        if user_id not in self.users[user_id].user_id:
            raise AttributeError("this user not in users.")
        if not self.books[isbn].is_available:
            raise "this book not found"
        user = self.users[user_id]
        book = self.books[isbn]
        if book.is_available():
            raise
        if book not in user.borrowed_books:
            raise
        user.return_book(book)
        book.isavailable = True

