import pygame
from pygame import QUIT
from pygame.key import ScancodeWrapper


class EventManager:
    def __init__(self):
        self.paused = False
        self.clicked = False

    def update(self, scene: str, level_changed: bool) -> None:
        for event in pygame.event.get():
            if event.type == QUIT:
                raise SystemExit

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.clicked = True
            else:
                self.clicked = False

            if scene != 'menu' and not level_changed:
                if event.type == pygame.KEYDOWN and self.key[pygame.K_ESCAPE]:
                    self.paused = not self.paused
            else:
                self.paused = False

    @property
    def key(self) -> ScancodeWrapper:
        return pygame.key.get_pressed()
