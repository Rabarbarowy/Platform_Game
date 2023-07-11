import pygame

from src.display import Drawable


class Platform(Drawable):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load('src/assets/images/platform.png')
        self.x = 330
        self.y = 400
