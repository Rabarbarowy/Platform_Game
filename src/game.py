import pygame
from pygame.time import Clock

from src.camera.camera import Camera
from src.constants import INITIAL_COORDINATES
from src.events import EventManager
from src.objects.player import Player
from src.scenes.levels import FirstLevel, SecondLevel
from src.scenes.menu import Menu


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.window = Menu()
        # self.window = FirstLevel()
        # self.window = SecondLevel()
        self.camera = Camera(INITIAL_COORDINATES[0])
        self.clock = Clock()
        self.event = EventManager()
        self.player = Player(INITIAL_COORDINATES, self.camera.y)

    def run_game(self) -> None:
        while True:
            if self.window.view != self.window.old_view:
                if self.window.view == 'menu':
                    self.window = Menu()
                elif self.window.view == 'level1':
                    self.player.reset_statistic()
                    self.window = FirstLevel()
                    self.camera.reset_coordinates(INITIAL_COORDINATES)
                elif self.window.view == 'level2':
                    self.window = SecondLevel()
                    self.player.reset_statistic()
                    self.camera.reset_coordinates(INITIAL_COORDINATES)

            self.clock.tick(60)
            self.window.show(self.player.direction_index, self.camera.x, self.camera.y)
            self.window.repeat(self.player, self.event.clicked, self.event.key)
            self.event.update(self.window.view)

            if not self.event.paused:
                self.camera.update_position(self.player.x, self.player.y)
                if self.window.draw_player:
                    self.player.repeat(
                        self.event.key,
                        self.player,
                        self.window.objects_to_draw,
                    )
                    self.player.show_player(
                        self.window.screen,
                        self.camera.x,
                        self.camera.y,
                        self.event.paused,
                    )
            else:
                self.player.show_player(
                    self.window.screen,
                    self.camera.x,
                    self.camera.y,
                    self.event.paused,
                )
                self.window.pause_menu(self.event.clicked)
                if self.window.pause_index:
                    self.window.pause_index = False
                    self.event.paused = False

            pygame.display.update()
