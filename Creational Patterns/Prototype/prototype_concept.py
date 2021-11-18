"The Prototype Concept"
from abc import ABC, ABCMeta, abstractmethod

class IPrototype(metaclass=ABCMeta):
    "interface with clone method"
    @staticmethod
    @abstractmethod
    def clone():
        """The clone, deep or shallow.
        It is up to yu how you want to implement 
        the details in your concrete class"""

class MyClass(IPrototype):
    "A Concrete Class"

    def __init__(self, field):
        self.field = field

    def clone(self):
        "This clone method uses a shallow copy technique. "
        return type(self)(self.field)
        # a shallow copy is returned

    def __str__(self):
        return f"{id(self)}\ttype={type(self.field)}"

"The Client"
# Create object containing a list
OBJECT1 = MyClass([1,2,3,4])
print(f"OBJECT1 {OBJECT1}")
# Clone object 1
OBJECT2 = OBJECT1.clone()
OBJECT2.field[1]  = 101

# Comparing OBJECT1 and OBJECT2
print(f"OBJECT2 {OBJECT2}")
print(f"OBJECT1 {OBJECT1}")