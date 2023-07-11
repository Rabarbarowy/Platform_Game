import pygame
from pygame import QUIT


class EventManager:
    def update(self) -> None:
        for event in pygame.event.get():
            if event.type == QUIT:
                raise SystemExit
