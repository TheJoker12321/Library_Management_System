import json

class JasonSapared:
    def book_created(self,json_file):
        with open(json_file,"r") as file:
            for i in file:
                new_book=Book(i['title'],i['auther'],i['ISBN'],True)
book=JasonSapared
book.book_created("json_file.json")