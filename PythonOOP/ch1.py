class Book():
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute"

    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    def setdiscount(self, amount):
        self._discount = amount


b1 = Book("Tao Te Cheng", "Lao Tzu", 100, 20.00)


print(b1.title)
b1.setdiscount(0.25)
print(b1.getprice())
