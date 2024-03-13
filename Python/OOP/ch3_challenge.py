from abc import ABC, abstractmethod
# Challenge: use a magic method to make stocks and bonds sortable
# Stocks should sort from low to high on price
# Bonds should sort from low to high on yield

class Asset(ABC):
    def __init__(self, price):
        self.price = price

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __lt__(self, value):
        pass


class Stock(Asset):
    def __init__(self, ticker, company, price):
        super().__init__(price)
        self.ticker = ticker
        self.company = company

    def __str__(self):
        return f"{self.ticker}: {self.company} -- ${self.price}"
    
    def __lt__(self, value):
        return self.price < value.price
    
class Bond(Asset):
    def __init__(self, description, duration, price, yieldAmt):
        super().__init__(price)
        self.description = description
        self.duration = duration
        self.yieldAmt = yieldAmt

    def __str__(self):
        return f"{self.description} - {self.duration}yr - ${self.price} : {self.yieldAmt}%"

    def __lt__(self, value):
        return self.yieldAmt < value.yieldAmt



msft = Stock("MSFT", "Microsoft", 155.00)
googl = Stock("GOOG", "Google", 300.00)
amzn = Stock("AMZN", "Amazon", 100)

stocks = [msft, googl, amzn]
stocks.sort()

b1 = Bond("30 year fixed", 30, 5, 11)
b2 = Bond("15 year fixed", 15, 50, 20)
b3 = Bond("150 year fixed", 150, 10, 80)

bonds = [b1, b2, b3]
bonds.sort()

print([bond.description for bond in bonds])
print('-------')
print([stock.ticker for stock in stocks])