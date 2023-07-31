import pygame
from pygame import QUIT
from pygame.key import ScancodeWrapper


class EventManager:
    def update(self) -> None:
        for event in pygame.event.get():
            if event.type == QUIT:
                raise SystemExit

    @property
    def key(self) -> ScancodeWrapper:
        return pygame.key.get_pressed()
