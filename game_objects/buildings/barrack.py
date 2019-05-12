import pygame
from game_objects import unit as unit_mod
from game_objects.buildings import base_building
from abc import ABC, abstractmethod
import exceptions
from images import image as img
from typing import *
import time


class Barrack(base_building.Building, ABC):
    """Factory & Template Method"""

    def create_builder(self):
        size = 90, 90
        rect = self._get_unit_rect(size)
        self._assert_creation_place_is_free(rect)
        unit = self._create_builder(size=size)
        self._action_after_unit_creation(unit, rect)
        return unit

    def create_scout(self):
        size = 90, 90
        rect = self._get_unit_rect(size)
        self._assert_creation_place_is_free(rect)
        unit = self._create_scout(size=size)
        self._action_after_unit_creation(unit, rect)
        return unit

    def create_warrior(self):
        size = 90, 90
        rect = self._get_unit_rect(size)
        self._assert_creation_place_is_free(rect)
        unit = self._create_warrior(size=size)
        self._action_after_unit_creation(unit, rect)
        return unit

    @abstractmethod
    def _create_builder(self, size: Tuple[int, int]) -> unit_mod.Builder: 
        pass

    @abstractmethod
    def _create_scout(self, size: Tuple[int, int]) -> unit_mod.Scout: 
        pass

    @abstractmethod
    def _create_warrior(self, size: Tuple[int, int]) -> unit_mod.Warrior: 
        pass

    def _get_unit_rect(self, size: Tuple[int, int]) -> pygame.Rect:
        rect = pygame.Rect(self.rect.topleft, size)
        rect.centerx = self.rect.centerx
        rect.top = self.rect.bottom + 20
        return rect

    def _assert_delay_is_over(self, delay: int, last_call_time: int):
        difference = time.time() - last_call_time
        if difference < delay:
            raise exceptions.CreationTimeError(
                "Can't create unit - not enough time's passed since previous call.\nTime remained: {}".format(
                    difference))

    def _assert_creation_place_is_free(self, rect: pygame.Rect):
        sprite = pygame.sprite.Sprite()
        sprite.rect = rect
        if pygame.sprite.spritecollideany(sprite, self._all_objects):
            raise exceptions.CreationPlaceError("Can't create unit - place is occupied")

    def _action_after_unit_creation(self, unit: unit_mod.Unit, rect: pygame.Rect):
        self.empire.army.recruit_unit(unit=unit)
        unit.rect = rect
        unit.update_position()

    @property
    def no_interaction_commands(self) -> List[Tuple[pygame.Surface, Callable, Text]]:
        return [(img.get_image(self.empire).SCOUT, self.create_scout, 'create scout'),
                (img.get_image(self.empire).BUILDER, self.create_builder, 'create builder'),
                (img.get_image(self.empire).WARRIOR, self.create_warrior, 'create warrior'),
                (img.get_image().UPGRADE, self.upgrade, 'Upgrade'),
                (img.get_image().REMOVE, self.destroy, 'Remove')]


class ElvesBarrack(Barrack):
    def _create_builder(self, size: Tuple[int, int]) -> unit_mod.Builder:
        return unit_mod.ElfBuilder(empire=self.empire,
                                   health=2,
                                   speed=12,
                                   cost=10,
                                   image=img.get_image(self.empire).BUILDER,
                                   size=size)

    def _create_scout(self, size: Tuple[int, int]) -> unit_mod.Scout:
        return unit_mod.ElfScout(empire=self.empire,
                                 health=3,
                                 speed=12,
                                 damage=1,
                                 fight_distance=300,
                                 cost=5,
                                 image=img.get_image(self.empire).SCOUT,
                                 size=size)

    def _create_warrior(self, size: Tuple[int, int]) -> unit_mod.Warrior:
        return unit_mod.ElfWarrior(empire=self.empire,
                                   health=5,
                                   speed=6,
                                   damage=2,
                                   fight_distance=500,
                                   cost=10,
                                   image=img.get_image(self.empire).WARRIOR,
                                   size=size)


class OrcsBarrack(Barrack):
    def _create_builder(self, size: Tuple[int, int]) -> unit_mod.Builder:
        return unit_mod.OrcBuilder(empire=self.empire,
                                   health=2,
                                   speed=6,
                                   cost=10,
                                   image=img.get_image(self.empire).BUILDER,
                                   size=size)

    def _create_scout(self, size: Tuple[int, int]) -> unit_mod.Scout:
        return unit_mod.OrcScout(empire=self.empire,
                                 health=3,
                                 speed=6,
                                 damage=2,
                                 fight_distance=500,
                                 cost=10,
                                 image=img.get_image(self.empire).SCOUT,
                                 size=size)

    def _create_warrior(self, size: Tuple[int, int]) -> unit_mod.Warrior:
        return unit_mod.OrcWarrior(empire=self.empire,
                                   health=5,
                                   speed=3,
                                   damage=4,
                                   fight_distance=50,
                                   cost=10,
                                   image=img.get_image(self.empire).WARRIOR,
                                   size=size)


class DwarfsBarrack(Barrack):
    def _create_builder(self, size: Tuple[int, int]) -> unit_mod.Builder:
        return unit_mod.DwarfBuilder(empire=self.empire,
                                     health=4,
                                     speed=6,
                                     cost=3,
                                     image=img.get_image(self.empire).BUILDER,
                                     size=size)

    def _create_scout(self, size: Tuple[int, int]) -> unit_mod.Scout:
        return unit_mod.DwarfScout(empire=self.empire,
                                   health=6,
                                   speed=6,
                                   damage=1,
                                   fight_distance=500,
                                   cost=10,
                                   image=img.get_image(self.empire).SCOUT,
                                   size=size)

    def _create_warrior(self, size: Tuple[int, int]) -> unit_mod.Warrior:
        return unit_mod.DwarfWarrior(empire=self.empire,
                                     health=10,
                                     speed=3,
                                     damage=1,
                                     fight_distance=50,
                                     cost=10,
                                     image=img.get_image(self.empire).WARRIOR,
                                     size=size)
