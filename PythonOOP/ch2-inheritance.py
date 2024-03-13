class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

class Book(Publication):
    def __init__(self, title, price, author, pages) -> None: 
        super().__init__(title, price)
        self.author = author
        self.pages = pages

b1 = Book("Tao Te Cheng", 15, "Lao Tzu", 81)

