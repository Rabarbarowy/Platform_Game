import pygame
from pygame.time import Clock

from src.camera.camera import Camera
from src.events import EventManager
from src.objects.platform import Platform
from src.objects.player import Player
from src.scenes.scene import Scene


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.window = Scene()
        self.camera = Camera()
        self.clock = Clock()
        self.event = EventManager()
        self.player = Player()
        self.platforms = [Platform(330, 400), Platform(50, 400), Platform(450, 500)]

    def run_game(self) -> None:
        while True:
            self.clock.tick(60)
            self.window.show()
            self.camera.update_position(self.player.x, self.player.y)
            self.player.draw(self.window.screan, self.camera.x, self.camera.y)
            for platform in self.platforms:
                platform.draw(self.window.screan, self.camera.x, self.camera.y)

            self.event.update()
            self.player.repeat(self.event.key, self.player, self.platforms)

            pygame.display.update()

