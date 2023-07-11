import pygame
from pygame import QUIT


class EventManager:
    def update(self) -> None:
        for event in pygame.event.get():
            if event.type == QUIT:
                raise SystemExit

    @property
    def key(self):
        return pygame.key.get_pressed()
