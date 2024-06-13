import pygame
from pygame.time import Clock

from src.camera.camera import Camera
from src.constants import INITIAL_COORDINATES, FPS
from src.events import EventManager
from src.objects.player import Player
from src.scenes.levels import LevelChanger
from src.scenes.menu import Menu
from src.sounds import SoundManager


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.window = LevelChanger()
        self.camera = Camera(INITIAL_COORDINATES[0])
        self.clock = Clock()
        self.event = EventManager()
        self.player = Player(INITIAL_COORDINATES, self.camera.y)
        self.sound_manager = SoundManager()
        # self.window.view = 'level2'

    def run_game(self) -> None:
        while True:
            if self.window.view != self.window.old_view:
                if self.window.view == 'menu':
                    # self.window = Menu()
                    self.window.menu()
                elif self.window.view == 'level1':
                    self.player.reset_statistic()
                    self.window.level1()
                    # self.window = FirstLevel()
                    self.camera.reset_coordinates(INITIAL_COORDINATES)
                elif self.window.view == 'level2':
                    self.window.level2()
                    # self.window = SecondLevel()
                    self.player.reset_statistic()
                    self.camera.reset_coordinates(INITIAL_COORDINATES)

            self.clock.tick(FPS)
            self.window.show(self.player.direction_index, self.camera.x, self.camera.y)
            self.window.repeat(self.player, self.event.clicked, self.event.key)
            self.event.update(self.window.view)
            self.sound_manager.use_manager(self.player)

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
