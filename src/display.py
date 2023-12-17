import pygame
from pygame import Rect

from src.animation import AnimateSprite
from src.sprite import Sprite


class Drawable(AnimateSprite):
    def __init__(self) -> None:
        super().__init__()
        Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('src/assets/images/brak_grafiki.png')

    def draw(self, screan, camera_x: int, camera_y: int, static: bool) -> None:
        if not static:
            screan.blit(self.image, (self.x - camera_x, self.y - camera_y))
        else:
            screan.blit(self.image, (camera_x, camera_y))

    @property
    def width(self) -> int:
        return self.image.get_width()

    @property
    def height(self) -> int:
        return self.image.get_height()

    @property
    def hitbox(self) -> Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)
