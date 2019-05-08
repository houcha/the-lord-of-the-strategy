"""Every game object has fields of this class,
so every game entity is inherited from one of these"""


import pygame
from game_objects import races
from abc import ABC, abstractmethod
from interface import window, interface
from typing import *


class GameEntity(ABC):
    def __init__(self, race):
        if race in races.races:
            self.race = race
        else:
            races.RaceError("Unknown race: {}".format(race))

    @abstractmethod
    def info(self) -> Text:
        pass


class GameObject(GameEntity, window.Window, ABC):

    cost: int
    icon_image: pygame.Surface

    def __init__(self, race, image_file: str, size: Tuple[int, int], icon_file: str = None):
        GameEntity.__init__(self, race)
        window.Window.__init__(self, size, image=pygame.image.load(image_file))
        if icon_file is None:
            self.icon_image = pygame.image.load(image_file)
        else:
            self.icon_image = pygame.image.load(icon_file)

    def handle(self, mouse_pos: Tuple[int, int]):
        self.change_state(window.ActiveWindowState(self))
        interface.Interface().handle_object_click(self)

    @property
    @abstractmethod
    def commands(self):
        pass
