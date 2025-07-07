class Book:
    def __init__(self, title: str, pages: int):
        self.title = title
        self.pages = pages
        self.pages_read = 0

    def read(self, num):
        if num+self.pages_read > self.pages:
            raise PagesExceed(
                f"You exceeded the page count"
            )
        self.pages_read += num
        print(f"You've now read {self.pages_read}/{self.pages} of the book.")

class PagesExceed(ValueError):
    pass

book = Book("Metamorphosis", 50)
book.read(4)
book.read(30)
book.read(50)