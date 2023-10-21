import pygame

from src.display import Drawable


class Platform(Drawable):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.image = self.transform_size(pygame.image.load('src/assets/images/platform.png'), 3)
        self.x = x
        self.y = y
        self.frame_position = 0
