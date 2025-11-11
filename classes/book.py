import json
class Book:
    def __init__(self,title:str,author:str,ISBN:int):
        self.title=title
        self.author=author
        self.ISBN=ISBN
        self.is_avilable=True
    def book_save(self,json_file):
        with open(json_file, "w") as file:
            json_book=json.dump(({"title":self.title,"author":self.author,"ISBN":self.ISBN}), file)
            file.write(json_book)
