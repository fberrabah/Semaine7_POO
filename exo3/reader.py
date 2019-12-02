# coding: utf8

class Reader():
    
    def __init__(self):
        self.book = None
        self.page = 0

    def borrow_book(self, librairy, title):
        try: 
            self.book = librairy.get_book(title)
        except Exception as e:
            print(e)

    def go_to_page(self, page_number):
        if page_number <= len(self.book.pages):
            self.book.current_page = page_number
        

    def next_page(self):
        if self.book.current_page < len(self.book.pages) -1:
            self.book.current_page +=1
            return True
        else:
            return False
        

    def previous_page(self):
        if self.book.current_page > 0:
            self.book.current_page  -= 1

    def read(self):

        print(self.book.pages[self.book.current_page])

    def read_book(self):
        if self.book:
            while self.next_page():
                self.read()
            self.go_to_page(-1)

