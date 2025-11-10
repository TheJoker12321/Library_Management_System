class Book:
    def __init__(self , title : str, author : str, isbn : str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.isavailable = True

    def __str__(self):
        return f"This book called {self.title} ,its author is {self.author}, its isbn is {self.isbn} and is available = {self.isavailable}"

    def is_available(self):
        return self.isavailable