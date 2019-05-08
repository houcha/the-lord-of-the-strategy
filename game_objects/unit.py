from game_objects.object_properties import speed as speed_mod, health as health_mod, damage as damage_mod
from game_objects import base_object
from abc import ABC
from typing import *


class Unit(base_object.GameObject, health_mod.Health, speed_mod.Speed, ABC):
    def __init__(self, empire, health: int, speed: int, size: Tuple[int, int], image_file: str):
        base_object.GameObject.__init__(self, empire=empire, size=size, image_file=image_file)
        health_mod.Health.__init__(self, health=health)
        speed_mod.Speed.__init__(self, speed=speed)

    def info(self) -> Text:
        result = str()
        result += "Empire: {}\n".format(self.empire.name)
        result += "Health: {}\n".format(self.health)
        result += "Speed: {}\n".format(self.speed)
        return result


class Warrior(Unit, damage_mod.Damage):
    def __init__(self, empire, health: int, speed: int, damage: int, size: Tuple[int, int], image_file: str):
        Unit.__init__(self, empire=empire, size=size, image_file=image_file, health=health, speed=speed)
        damage_mod.Damage.__init__(self, damage=damage)

    def info(self) -> Text:
        """super().info is anti-pattern so we rewrite all method"""
        result = str()
        result += "Empire: {}\n".format(self.empire.name)
        result += "Health: {}\n".format(self.health)
        result += "Speed: {}\n".format(self.speed)
        result += "Damage: {}\n".format(self.damage)
        return result


class ElfWarrior(Warrior):
    pass


class OrcWarrior(Warrior):
    pass


class DwarfWarrior(Warrior):
    pass


class Scout(Unit):
    pass


class ElfScout(Scout):
    pass


class OrcScout(Scout):
    pass


class DwarfScout(Scout):
    pass


class Builder(Unit):
    pass


class ElfBuilder(Builder):
    pass


class OrcBuilder(Builder):
    pass


class DwarfBuilder(Builder):
    pass
