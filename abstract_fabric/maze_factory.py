from abc import abstractmethod, ABC
from enum import Enum
from typing import Union


class MapSite(ABC):

    @abstractmethod
    def enter(self):
        pass


class Maze:
    def __init__(self):
        self.rooms = []

    def addRoom(self, r):
        self.rooms.append(r)

    def roomNo(self, n):
        return self.rooms[n]


class Wall(MapSite):
    def enter(self):
        pass


class Door(MapSite):
    def __init__(self, r1: Room, r2: Room):
        self._room1 = r1
        self._room2 = r2
        self._isOpen = False

    def otherSidefrom(self, room):
        pass

    def enter(self):
        pass


class Room(MapSite):
    def __init__(self, roomNumber):
        self._roomNumber = roomNumber
        self._sides = [None, None, None, None]

    def setSide(self, direction, obj: Union[Wall, Door]):
        self._sides[direction] = obj

    def getSide(self, direction):
        return self._sides[direction]

    def enter(self):
        pass


class Direction(Enum):
    North = 0
    South = 1
    East = 2
    West = 3


class MazeFactory:
    """
    Может создавать компоненты лабиринтов
    """

    @staticmethod
    def makeMaze():
        """Создание лабиринта"""
        return Maze()

    @staticmethod
    def makeWall():
        """Создание стены"""
        return Wall()

    @staticmethod
    def makeRoom(n):
        return Room(n)

    @staticmethod
    def makeDoor(r1, r2):
        return Door(r1, r2)


class EnchantedMazeFactory(MazeFactory):

    @staticmethod
    def makeRoom(n):
        return None


def createMaze(factory: MazeFactory) -> Maze:
    """Производство лабиринтов и компонентов"""
    aMaze = factory.makeMaze()
    r1 = factory.makeRoom(1)
    r2 = factory.makeRoom(2)
    door = factory.makeDoor(r1, r2)

    aMaze.addRoom(r1)
    aMaze.addRoom(r2)

    r1.setSide(Direction.North, Wall())
    r1.setSide(Direction.East, door)
    r1.setSide(Direction.South, Wall())
    r1.setSide(Direction.West, Wall())

    r2.setSide(Direction.North, Wall())
    r2.setSide(Direction.East, Wall())
    r2.setSide(Direction.South, Wall())
    r2.setSide(Direction.West, door)

    return aMaze