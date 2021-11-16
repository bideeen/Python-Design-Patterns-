# Car Factory
from abc import ABCMeta, abstractmethod

class ICar(metaclass=ABCMeta):
    "The Car Intgerface"

    @staticmethod
    @abstractmethod
    def get_dimensions():
        "A static interface method"

class SmallCar(ICar):
    "The Small Car Concrete Class implements the ICar interfaces"

    def __init__(self):
        self._length = 4011
        self._width = 1775
        self._height = 1578

    def get_dimensions(self):
        return {
            "length": self._length,
            "width": self._width,
            "height": self._height
        }

class MediumCar(ICar):

    "The Medium Car Concrete Class implements the ICar interfaces"

    def __init__(self):
        self._length = 4709
        self._width = 1827
        self._height = 1435

    def get_dimensions(self):
        return {
            "length": self._length,
            "width": self._width,
            "height": self._height
        }

class BigCar(ICar):

    "The Big Car Concrete Class implements the ICar interfaces"

    def __init__(self):
        self._length = 4851
        self._width = 1902
        self._height = 1346

    def get_dimensions(self):
        return {
            "length": self._length,
            "width": self._width,
            "height": self._height
        }

class CarFactory:
    "The Car Factory"

    @staticmethod
    def get_car(car):
        "A static method to get a car"
        if car == "BigCar":
            return BigCar()
        if car == "MediumCar":
            return MediumCar()
        if car == "SmallCar":
            return SmallCar()
        return None

if __name__ == '__main__':
    cars = ['BigCar', 'MediumCar', 'SmallCar']
    for i in cars:
        Cars = CarFactory().get_car(i)
        print(f"{i}: {Cars.get_dimensions()}")
    
