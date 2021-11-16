from abc import ABCMeta, abstractmethod

# The Chair Interface
class IChair(metaclass=ABCMeta):
    "The Chair Interface (Product)"

    @staticmethod
    @abstractmethod
    def get_dimensions():
        "The static interface method"

# The Table Interface


class ITable(metaclass=ABCMeta):
    "The Chair Interface (Product)"

    @staticmethod
    @abstractmethod
    def get_dimensions():
        "The static interface method"

# Small Chair


class SmallChair(IChair):
    "The Small Chair Concrete Class implements the ICHair interface"

    def __init__(self) -> None:
        self._height = 40
        self._width = 40
        self._depth = 40

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }

# Small Table
class SmallTable(ITable):
    "The Small Table Concrete Class implements the ITable interface"

    def __init__(self) -> None:
        self._height = 60
        self._width = 100
        self._depth = 60

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }

# Medium Chair
class MediumChair(IChair):
    "The Medium Chair Concrete Class implements the ICHair interface"

    def __init__(self) -> None:
        self._height = 60
        self._width = 60
        self._depth = 60

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }

# Medium Table
class MediumTable(ITable):
    "The Medium Table Concrete Class implements the ITable interface"

    def __init__(self) -> None:
        self._height = 60
        self._width = 110
        self._depth = 60

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }

# Big Chair
class BigChair(IChair):
    "The Big Chair Concrete Class implements the ICHair interface"

    def __init__(self) -> None:
        self._height = 80
        self._width = 80
        self._depth = 80

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }

# Big Table
class BigTable(ITable):
    "The Big Chair Concrete Class implements the ITable interface"

    def __init__(self) -> None:
        self._height = 60
        self._width = 120
        self._depth = 80

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }

# Chair Factory
class ChairFactory:  # pylint: disable=too-few-public-methods
    "The Factory Class"
    
    @staticmethod
    def get_chair(table):
        "A static method to get a table"
        try:
            if table == 'BigChair':
                return BigChair()
            if table == 'MediumChair':
                return MediumChair()
            if table == 'SmallChair':
                return SmallChair()
            raise Exception('Table Not Found')
        except Exception as _e:
            print(_e)
        return None

# Table Factory
class TableFactory:  # pylint: disable=too-few-public-methods
    "The Factory Class"
    
    @staticmethod
    def get_table(table):
        "A static method to get a table"
        try:
            if table == 'BigTable':
                return BigTable()
            if table == 'MediumTable':
                return MediumTable()
            if table == 'SmallTable':
                return SmallTable()
            raise Exception('Table Not Found')
        except Exception as _e:
            print(_e)
        return None

# interface furniture factory
class IFurnitureFactory(metaclass=ABCMeta):
    "Abstract Furniture Factory Interface"

    @staticmethod
    @abstractmethod
    def get_furniture(furniture):
        "The static Abstract factory interface method"

# Furniture Factory
class FurnitureFactory(IFurnitureFactory):
    "The Abstract Factory Concrete Cass"

    @staticmethod
    def get_furniture(furniture):
        "Static get_factory Concrete Class"
        try:
            if furniture in ['SmallChair', 'MediumChair', 'BigChair']:
                return ChairFactory().get_chair(furniture)
            if furniture in ['SmallTable', 'MediumTable', 'BigTable']:
                return TableFactory().get_table(furniture)
            raise Exception('No Factory Found')
        except Exception as _e:
            print(_e)
        return None
        
if __name__ == '__main__':
    # Client
    "Abstract Factory"
    FURNITURE = FurnitureFactory.get_furniture("SmallChair")
    print(f"{FURNITURE.__class__} : {FURNITURE.get_dimensions()}")

    FURNITURE = FurnitureFactory.get_furniture("MediumTable")
    print(f"{FURNITURE.__class__} : {FURNITURE.get_dimensions()}")