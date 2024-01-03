import pygame
from pygame.time import Clock

from src.camera.camera import Camera
from src.events import EventManager
from src.objects.objects import VisibleObject, Heart
from src.objects.player import Player
from src.scenes.scene import Scene


class Game:
    platform = pygame.image.load('src/assets/images/platform.png')
    platform2 = pygame.image.load('src/assets/images/platform2.png')
    heart = pygame.image.load('src/assets/images/heart.png')
    life_bar = pygame.image.load('src/assets/images/life_bar.png')

    def __init__(self) -> None:
        pygame.init()
        self.window = Scene()
        self.camera = Camera()
        self.clock = Clock()
        self.event = EventManager()
        self.player = Player()

        self.life_bars = [
            Heart(self.player.x - 300, self.camera.y - self.player.y + 20)
        ]
        self.life_bars[0].heart_beating(len(self.life_bars))
        self.life_bars.append(VisibleObject(self.life_bars[0].x + self.life_bars[0].width - 23, self.camera.y - self.player.y + 20, self.life_bar, 2))

        self.platforms = [
            VisibleObject(290, 300, self.platform, 3),
            VisibleObject(-300, 500, self.platform, 3),
            VisibleObject(-100, 400, self.platform, 3),
            VisibleObject(640, 500, self.platform, 3),
            VisibleObject(830, 450, self.platform, 3),
            VisibleObject(1000, 400, self.platform, 3),
            VisibleObject(1200, 350, self.platform, 3),
        ]

    def run_game(self) -> None:
        while True:
            self.clock.tick(60)
            self.window.show()
            self.camera.update_position(self.player.x, self.player.y)

            for platform in self.platforms:
                platform.draw(self.window.screan, self.camera.x, self.camera.y, False)

            self.life_bars[0].heart_beating(len(self.life_bars))

            for life_bar in self.life_bars:
                life_bar.draw(self.window.screan, life_bar.x, life_bar.y, True)

            self.life_bars[0].draw(self.window.screan, self.life_bars[0].x, self.life_bars[0].y, True)

            self.event.update()

            self.player.repeat(
                self.window.screan,
                self.camera.x,
                self.camera.y,
                self.event.key,
                self.player,
                self.platforms
            )

            pygame.display.update()
