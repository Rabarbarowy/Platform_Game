import pygame
from pygame.time import Clock

from src.events import EventManager
from src.objects.platform import Platform
from src.objects.player import Player
from src.scenes.scene import Scene


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.window = Scene()
        self.clock = Clock()
        self.event = EventManager()
        self.player = Player()
        self.platform = Platform()

    def run_game(self) -> None:
        while True:
            self.clock.tick(60)
            self.window.show()
            self.player.draw(self.window.screan)
            self.platform.draw(self.window.screan)
            self.event.update()
            self.player.repeat(self.player, self.platform)

            pygame.display.update()

