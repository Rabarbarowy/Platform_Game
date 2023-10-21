import pygame

from src.display import Drawable


class Platform(Drawable):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.image = pygame.image.load('src/assets/images/platform.png')
        self.x = x
        self.y = y
        self.frame_position = 0
