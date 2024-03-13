from abc import ABC, abstractmethod

class GraphicShape:
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def calcArea(self):
        pass

class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass

class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def toJSON(self):
        return f"'Circle': {str(self.calcArea())}"
    


c = Circle(10)

print(c.toJSON)