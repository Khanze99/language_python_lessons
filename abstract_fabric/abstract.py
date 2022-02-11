from .maze_factory import MazeFactory as F, Direction, Maze, Room, Door, Wall


class EnchantedRoom(Room):
    def __init__(self, n, spell):
        super().__init__(n)
        self.spell = spell


class DoorNeedingSpell(Door):
    def __init__(self, r1, r2):
        super().__init__(r1, r2)


class RoomWithABomb(Room):
    def __init__(self, n):
        super().__init__(n)


class BombedWall(Wall):
    def __init__(self):
        self.is_bombed = False


class BombedMazeFactory(F):

    @staticmethod
    def makeWall():
        return BombedWall()

    @staticmethod
    def makeRoom(n):
        return RoomWithABomb(n)


class EnchantedMazeFactory(F):

    @classmethod
    def makeRoom(cls, n):
        return EnchantedRoom(n, cls.castSpell())

    @staticmethod
    def makeDoor(r1, r2):
        return DoorNeedingSpell(r1, r2)

    @staticmethod
    def castSpell():
        pass


def createMaze(factory: F) -> Maze:
    aMaze = factory.makeMaze()
    r1 = factory.makeRoom(1)
    r2 = factory.makeRoom(2)
    aDoor = factory.makeDoor(r1, r2)

    aMaze.addRoom(r1)
    aMaze.addRoom(r2)

    r1.setSide(Direction.North, factory.makeWall())
    r1.setSide(Direction.East, aDoor)
    r1.setSide(Direction.South, factory.makeWall())
    r1.setSide(Direction.West, factory.makeWall())

    r2.setSide(Direction.North, factory.makeWall())
    r2.setSide(Direction.East, factory.makeWall())
    r2.setSide(Direction.South, factory.makeWall())
    r2.setSide(Direction.West, aDoor)

    return aMaze