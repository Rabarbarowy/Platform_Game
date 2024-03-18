import pygame

from src.objects.objects import Button
from src.scenes.window import Scene


class Menu(Scene):
    def __init__(self) -> None:
        super().__init__()
        self.draw_player = False

        self.buttons = [
            Button(430, 200, pygame.image.load('src/assets/images/buttons/play.png'), 'play'),
            Button(430, 500, pygame.image.load('src/assets/images/buttons/exit.png'), 'exit'),
        ]
