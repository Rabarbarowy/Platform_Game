import pygame
from pygame.time import Clock

from src.camera.camera import Camera
from src.constants import INITIAL_COORDINATES
from src.events import EventManager
from src.objects.objects import VisibleObject, Spike
from src.objects.player import Player
from src.scenes.levels import FirstLevel
from src.scenes.menu import Menu
from src.scenes.window import Scene


class Game:
    # platform = pygame.image.load('src/assets/images/platform.png')
    # platform2 = pygame.image.load('src/assets/images/platform2.png')
    # spike = pygame.image.load('src/assets/images/spikes.png')
    def __init__(self) -> None:
        pygame.init()
        # self.window = Scene()
        self.window = Menu()
        self.camera = Camera(INITIAL_COORDINATES[0])
        self.clock = Clock()
        self.event = EventManager()
        self.player = Player(INITIAL_COORDINATES, self.camera.y)

        # self.platforms = [
        #     VisibleObject(290, 300, self.platform, 3, True),
        #     VisibleObject(-300, 500, self.platform, 3, True),
        #     VisibleObject(-100, 400, self.platform, 3, True),
        #     VisibleObject(400, 400, self.platform, 3, True),
        #     VisibleObject(640, 500, self.platform, 3, True),
        #     VisibleObject(1000, 400, self.platform, 3, True),
        #     VisibleObject(1200, 350, self.platform2, 3, True),
        # ]
        #
        # self.spikes = [
        #     Spike(640, 479, self.spike, 3)
        # ]

    def run_game(self) -> None:
        while True:
            self.clock.tick(60)
            self.camera.update_position(self.player.x, self.player.y)
            self.window.show(self.player.direction_index, self.camera.x, self.camera.y)
            self.window.repeat(self.player)

            if self.window.view != self.window.old_view:
                if self.window.view == 'menu':
                    self.window = Menu()
                elif self.window.view == 'level1':
                    self.window = FirstLevel()

            # for platform in self.platforms:
            #     platform.draw(self.window.screen, self.camera.x, self.camera.y, False)
            #
            # for spike in self.spikes:
            #     spike.draw(self.window.screen, self.camera.x, self.camera.y, False)
            #     spike.attacking(self.player)

            self.event.update()

            if self.window.draw_player:
                self.player.repeat(
                    self.window.screen,
                    self.camera.x,
                    self.camera.y,
                    self.event.key,
                    self.player,
                    self.window.objects_to_draw,
                    # self.platforms,
                )

            pygame.display.update()
