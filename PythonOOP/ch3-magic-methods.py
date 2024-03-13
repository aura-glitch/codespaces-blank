# Customize objec behavior and integrate with the language
# Define how objects are represented as strings
# Control access to attribute values, both get and set
# Build in comparison and equality testing capabilities
# Allow objects to be called like functions

from typing import Any


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
        self._discount = 0.1

    # __str__ method to return a string
    def __str__(self):
        return f"{self.title} by {self.author}, costs ${self.price}"
    # __repr__ method to return an obj representation
    def __repr__(self):
        return f"title={self.title},author={self.author},price={self.price}"
    
    # __eq__ method checks for equality between two objects
    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare Book to a non-Book")
        return self.title == value.title and self.author == value.author and self.price == value.price
    
    # __ge__ establishes >= relationship with other obj
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare Book to a non-Book")
        return self.price >= value.price
    
    # __lt__ establishes < relationship with other obj
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare Book to a non-Book")
        return self.price < value.price
    

    # __getattribute__ called when an attr is retrieved. Don't
    # directly access the attr name otherwise a recursive loop is created
    def __getattribute__(self, name):
        if name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
        return super().__getattribute__(name)
    
    # __setattr__ called when an attribute value is set. Don't set the attr
    # directly here otherwise a recursive loop causes a crash
    def __setattr__(self, name, value) -> None:
        if name == "price":
            if type(value) is not float:
                raise ValueError("The 'price' attr must be float")
        return super().__setattr__(name, value)
    
    # __getattr__ called when __getattribute__ lookup fails - you can
    # pretty much generate attributes on the fly with this method
    def __getattr__(self, name):
        return name + " is not here"

b1 = Book("Tao Te Cheng", 15.00, "Lao Tzu", 81)
b2 = Book("Bhagavad Gita", 15.00, "Lord Krishna", 81)
b3 = Book("The Bible", 10.00, "God", 500)

# books = [b1, b2, b3]
# books.sort()
# print([book.title for book in books])

print(b1.randomprop)

# print(str(b1))
# print(repr(b1))