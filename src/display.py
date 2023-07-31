import pygame
from pygame import Rect


class Drawable:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('src/assets/images/brakGrafiki.png')

    def draw(self, screan) -> None:
        screan.blit(self.image, (self.x, self.y))

    @property
    def width(self) -> int:
        return self.image.get_width()

    @property
    def height(self) -> int:
        return self.image.get_height()

    @property
    def hitbox(self) -> Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)
