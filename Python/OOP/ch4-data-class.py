from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20,40))

@dataclass
class Book:
        title: str = "No Title"
        author: str = "No Author"
        pages: int = 0
        price: float = field(default_factory=price_func)
        _discount: float = 0.1
        
        def __post_init__(self):
            self.description = f"{self.title}, by {self.author} with {self.pages} pages"
        
        def bookinfo(self):
            return f"{self.title}, by {self.author}"

b1 = Book("Tao Te Cheng", "Lao Tzu", 88)
b2 = Book("Bhagavad Gita", "Lord Krishna", 100)
b3 = Book("Tao Te Cheng", "Lao Tzu", 88)

# print(b1)

# print(b1 == b3)
# print(b1 == b2)

# print(b1.bookinfo())
print(b1.description)


@dataclass(frozen=True)
class ImmutableClass:
     value1: str = "Value1"
     value2: int = 0



obj = ImmutableClass()

obj.value1 = "Something else"

print(obj.value1)


