"The Factory Concept"
from abc import ABCMeta, abstractmethod

class IProduct(metaclass=ABCMeta):
    "A Hypothetical Class Interface"

    @staticmethod
    @abstractmethod

    def create_object():
        "an abtract interface method"

class ConcreteProductA(IProduct):
    "A Cncrete Class that implements the IProduct interface"

    def __init__(self) -> None:
        self.name = "ConcreteProductA"
        
    def create_object(self):
        return self

class ConcreteProductB(IProduct):
    "A Cncrete Class that implements the IProduct interface"

    def __init__(self) -> None:
        self.name = "ConcreteProductB"
        
    def create_object(self):
        return self
    
class ConcreteProductC(IProduct):
    "A Cncrete Class that implements the IProduct interface"

    def __init__(self) -> None:
        self.name = "ConcreteProductC"
        
    def create_object(self):
        return self

class Creator:
    "The Factory Class"

    @staticmethod
    def create_object(some_property):
        "A static method to get a concrete product"
        if some_property == 'a':
            return ConcreteProductA()
        if some_property == 'b':
            return ConcreteProductB()
        if some_property == 'c':
            return ConcreteProductC()
        return None

# The Client
PRODUCT = Creator().create_object('c')
print(PRODUCT.name)