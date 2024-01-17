import pygame
from pygame.time import Clock

from src.camera.camera import Camera
from src.events import EventManager
from src.objects.objects import VisibleObject, Spike
from src.objects.player import Player
from src.scenes.scene import Scene


class Game:
    platform = pygame.image.load('src/assets/images/platform.png')
    platform2 = pygame.image.load('src/assets/images/platform2.png')
    spike = pygame.image.load('src/assets/images/spikes.png')

    def __init__(self) -> None:
        pygame.init()
        self.window = Scene()
        self.camera = Camera()
        self.clock = Clock()
        self.event = EventManager()
        self.player = Player([350, 0], self.camera.y)

        self.platforms = [
            VisibleObject(290, 300, self.platform, 3),
            VisibleObject(-300, 500, self.platform, 3),
            VisibleObject(-100, 400, self.platform, 3),
            VisibleObject(400, 400, self.platform, 3),
            VisibleObject(640, 500, self.platform, 3),
            VisibleObject(1000, 400, self.platform, 3),
            VisibleObject(1200, 350, self.platform2, 3),
        ]

        self.spikes = [
            Spike(640, 479, self.spike, 3)
        ]

    def run_game(self) -> None:
        while True:
            self.clock.tick(60)
            self.window.show()
            self.camera.update_position(self.player.x, self.player.y)

            for platform in self.platforms:
                platform.draw(self.window.screen, self.camera.x, self.camera.y, False)

            for spike in self.spikes:
                spike.draw(self.window.screen, self.camera.x, self.camera.y, False)
                spike.attacking(self.player)

            self.event.update()

            self.player.repeat(
                self.window.screen,
                self.camera.x,
                self.camera.y,
                self.event.key,
                self.player,
                self.platforms,
            )

            pygame.display.update()
