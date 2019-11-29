# coding: utf8

class Reader():
    
    def __init__(self):
        self.book = None
        self.page = 0

    def borrow_book(self, librairy):
        if name not in self.book:
            self.books[name] = list(book)
        else:
            self._books[name].append(book)

    def go_to_page(self):
        self.page = page
        

    def next_page(self):
        return self.page+1
        

    def previous_page(self):
        if page==1:
            return
        return self.page-1  

    def read(self):
        return self.page

    def read_book(self):
        self.page=len(self.book.pages)

