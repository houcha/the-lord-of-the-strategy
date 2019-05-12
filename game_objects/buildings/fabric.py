from abc import ABC, abstractmethod
from typing import Tuple
# project modules #
import image as img
from game_objects.buildings import barrack, mine, wall
from game_objects import races


class Manufacture:
    """Abstract Factory"""

    def create_fabric(self, empire):
        if empire.race == races.ELVES:
            return ElvesFabric(empire)
        elif empire.race == races.ORCS:
            return OrcsFabric(empire)
        elif empire.race == races.DWARFS:
            return DwarfsFabric(empire)


class Fabric(ABC):
    """Template Method"""

    def __init__(self, empire):
        self.empire = empire

    @abstractmethod
    def build_barrack(self, size: Tuple[int, int]) -> barrack.Barrack:
        pass

    @abstractmethod
    def build_mine(self, size: Tuple[int, int]) -> mine.Mine:
        pass

    @abstractmethod
    def build_wall(self, size: Tuple[int, int]) -> wall.Wall:
        pass


class ElvesFabric(Fabric):
    def build_barrack(self, size: Tuple[int, int]) -> barrack.Barrack:
        return barrack.ElvesBarrack(health=15,
                                    cost=20,
                                    empire=self.empire,
                                    image=img.get_image(self.empire).BARRACK,
                                    size=size)

    def build_mine(self, size: Tuple[int, int]) -> mine.Mine:
        return mine.Mine(health=10,
                         cost=10,
                         reload=60,
                         empire=self.empire,
                         image=img.get_image(self.empire).MINE,
                         size=size)

    def build_wall(self, size: Tuple[int, int]) -> wall.Wall:
        return wall.Wall(health=10,
                         cost=5,
                         empire=self.empire,
                         image=img.get_image(self.empire).WALL,
                         size=size)


class OrcsFabric(Fabric):
    def build_barrack(self, size: Tuple[int, int]) -> barrack.Barrack:
        return barrack.OrcsBarrack(health=15,
                                   cost=20,
                                   empire=self.empire,
                                   image=img.get_image(self.empire).BARRACK,
                                   size=size)

    def build_mine(self, size: Tuple[int, int]) -> mine.Mine:
        return mine.Mine(health=10,
                         cost=10,
                         reload=60,
                         empire=self.empire,
                         image=img.get_image(self.empire).MINE,
                         size=size)

    def build_wall(self, size: Tuple[int, int]) -> wall.Wall:
        return wall.Wall(health=10,
                         cost=5,
                         empire=self.empire,
                         image=img.get_image(self.empire).WALL,
                         size=size)


class DwarfsFabric(Fabric):
    def build_barrack(self, size: Tuple[int, int]) -> barrack.Barrack:
        return barrack.DwarfsBarrack(health=30,
                                     cost=20,
                                     empire=self.empire,
                                     image=img.get_image(self.empire).BARRACK,
                                     size=size)

    def build_mine(self, size: Tuple[int, int]) -> mine.Mine:
        return mine.Mine(health=20,
                         cost=10,
                         reload=60,
                         empire=self.empire,
                         image=img.get_image(self.empire).MINE,
                         size=size)

    def build_wall(self, size: Tuple[int, int]) -> wall.Wall:
        return wall.Wall(health=20,
                         cost=5,
                         empire=self.empire,
                         image=img.get_image(self.empire).WALL,
                         size=size)
