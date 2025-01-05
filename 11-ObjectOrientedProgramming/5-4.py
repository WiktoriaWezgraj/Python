'''E-book is a digital book that can be read using a computer or other electronic devices (electronic book readers). 
Write a program in which define a class that describes states and behaviors of an e-book. 
Each book has a title, author, number of pages and the current page number that is currently being read. 
It is possible to open a book - then we can read it. If a book is open, it is possible to go to the next or previous page.

Place the class describing e-books in a separate file/module. In the main program file, try using the e-book:

Create a book with a title, author, number of pages 
(check how to set the initial values of the fields at the time of creating the object using the __init__ method / constructor 
and passing the initial values as arguments to the method call)
Open a book
Display a book status (title, author, page numbers, current page no)
Read a few pages
Display a book status
Close a book
Read a few pages (it should not be possible to perform this operation - display the message that the book is closed).'''

class Ebook:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page_no = 0
    def open(self):
        self.is_open = True
    def close(self):
        self.is_open = False
    def show_status(self):
        if self.is_open:
            print(f'Book is open. Page {self.current_page_no}')
        else:
            print('Book is closed')
    def read(self, numofpages):
        if self.is_open:
            if numofpages <= self.pages-self.current_page_no:
            
                self.current_page_no += numofpages
            else:
                print('You cant perform this operation with book closed.')

ebook = Ebook('Harry Potter', 'Rowling', 360)
ebook.open()
ebook.read(25)
ebook.show_status()
ebook.close()
ebook.read(5)

        