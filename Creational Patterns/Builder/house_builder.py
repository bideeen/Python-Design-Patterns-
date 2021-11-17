from abc import ABCMeta, abstractmethod


"The Builder Interface"
class IHouseBuilder(metaclass=ABCMeta):
    "The House Builder Interface"

    @staticmethod
    @abstractmethod
    def set_building_type(buildeing_type):
        "Build type"

    @staticmethod
    @abstractmethod
    def set_wall_material(wall_material):
        "Build material"

    @staticmethod
    @abstractmethod
    def set_number_doors(number):
        "Number of doors"

    @staticmethod
    @abstractmethod
    def set_number_windows(number):
        "Numbers of windows"

    @staticmethod
    @abstractmethod
    def get_result():
        "Return the final product"

# The Product(House)
class House():
    "The Product"
    def __init__(self, building_type="Apartment", doors=0, windows=0, wall_material='Brick'):
        # brick, wood, straw, ice
        self.wall_material = wall_material
        # Apartment, Bungalow, Caravan, Hot, Castle, Duplex
        # HosueBoat, Igloo
        self.building_type = building_type
        self.doors = doors
        self.windows = windows

    def construction(self):
        f"Return a string describing the construct" 
        return f"This is a  {self.wall_material} {self.building_type} with {self.doors} door(s) {self.windows} window(s)."
        
# The Builder Class
class HouseBuilder(IHouseBuilder):
    "The House Builder"

    def __init__(self) -> None:
        self.house = House()

    def set_building_type(self, building_type):
        self.house.building_type = building_type
        return self
    
    def set_wall_material(self, wall_material):
        self.set_wall_material = wall_material
        return self

    def set_number_doors(self, numbers):
        self.house.doors = numbers
        return self

    def set_number_windows(self, number):
        self.house.windows = number
        return self
    
    def get_result(self):
        return self.house

"A Director Class"
class IglooDirector:
    "One of the Directors, that can build a complex representation."
    
    @staticmethod
    def construct():
        """Constructs and returns the final product Note that in this IglooDirector, it has omitted the set_number_of windows call since this Igloo will have no windows."""
        return HouseBuilder().set_building_type("Igloo").set_wall_material("Ice").set_number_doors(1).get_result()

class CastleDirector:
    "One of the Directors, that can build a complex representation."

    @staticmethod
    def construct():
        "Constructs and returns the final product"
        return HouseBuilder().set_building_type("Castle").set_wall_material("Sandstone").set_number_doors(100).set_number_windows(200).get_result()

class HouseBoatDirector:
    "One of the Directors, that can build a complex representation."
    
    @staticmethod
    def construct():
        "Constructs and returns the final product"
        return HouseBuilder().set_building_type("House Boat").set_wall_material("Wood").set_number_doors(6).set_number_windows(8).get_result()


# House Builder Example Code
IGLOO = IglooDirector.construct()
CASTLE = CastleDirector.construct()
HOUSEBOAT = HouseBoatDirector.construct()
print(IGLOO.construction())
print(CASTLE.construction())
print(HOUSEBOAT.construction())