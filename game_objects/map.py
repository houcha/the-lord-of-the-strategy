import pygame
# project modules #
import configs
import singleton


class Map(pygame.sprite.Sprite, metaclass=singleton.Singleton):

    image: pygame.Surface
    rect: pygame.Rect
    color = (40, 150, 40)

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(configs.MAP_SIZE)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

    def clear(self):
        self.image.fill(self.color)
