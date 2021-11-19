"The Singleton Game"
"""--------------------"""
"A Game Interface"
from abc import ABCMeta, abstractmethod

class IGame(metaclass=ABCMeta):
    "A Game Interface"
    @staticmethod
    @abstractmethod
    def add_winner(position, name):
        "Must implement add_winner"


"A Leaderboard Sigleton Class"
class Leaderboard():
    "The Leaderboard as a Singleton"
    _table = {}

    def __new__(cls):
        return cls

    @classmethod
    def print(cls):
        print("------------Leaderboard------------")
        for key, value in sorted(cls._table.items()):
            print(f"|\t{key}\t|\t{value}\t|")
        print()

    @classmethod
    def add_winner(cls, position, name):
        "A class level method"
        cls._table[position] = name

"Game 1"
class Game1(IGame):
    "Game1 implements IGame"

    def __init__(self) -> None:
        self.leaderboard = Leaderboard()

    def add_winner(self, position, name):
        self.leaderboard.add_winner(position, name)

"Game 2"
class Game2(IGame):
    "Game2 implements IGame"

    def __init__(self) -> None:
        self.leaderboard = Leaderboard()

    def add_winner(self, position, name):
        self.leaderboard.add_winner(position, name)

"Game 3"
class Game3(IGame):
    "Game3 implements IGame"

    def __init__(self) -> None:
        self.leaderboard = Leaderboard()

    def add_winner(self, position, name):
        self.leaderboard.add_winner(position, name)


# The Client
# All games share and manage the same leaderboard because it is a singleton.
GAME1 = Game1()
GAME1.add_winner(2, "Cosmo")
GAME2 = Game2()
GAME2.add_winner(3, "Sean")
GAME3 = Game3()
GAME3.add_winner(1, "Emmy")

GAME1.leaderboard.print()
GAME2.leaderboard.print()
GAME3.leaderboard.print()