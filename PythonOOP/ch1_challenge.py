class Stock():
    def __init__(self, ticker, price, company) -> None:
        self.ticker = ticker
        self.price = price
        self.company = company
    
    def get_description(self):
        return f"{self.ticker}: {self.company} -- ${self.price}"
    
msft = Stock('MSFT', 50, 'Microsoft')

print(msft.get_description())