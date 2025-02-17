import pygame
from pygame.time import Clock

from src.camera.camera import Camera
from src.constants import INITIAL_COORDINATES, FPS
from src.events import EventManager
from src.objects.player import Player
from src.scenes.levels import LevelChanger
from src.sounds import SoundManager


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.window = LevelChanger()
        self.camera = Camera(INITIAL_COORDINATES[0])
        self.clock = Clock()
        self.event = EventManager()
        self.player = Player(INITIAL_COORDINATES, self.camera.y)
        self.sounds_manager = SoundManager()

    def run_game(self) -> None:
        while True:
            self.sounds_manager.play_background_music()
            if not self.event.paused:
                if self.window.view != self.window.old_view:
                    self.sounds_manager.change_music(self.window.view)
                    self.window.change_level(self.player)
                    if self.window.reset_player_stats:
                        self.camera.reset_coordinates(INITIAL_COORDINATES)
                        self.player.reset_statistic()
                self.window.show_up_in_new_level(self.player.x, self.player.y)
            if self.window.frozen_player:
                self.player.froze()
                if self.window.invisible_player:
                    self.player.invisible = True
                else:
                    self.player.invisible = False
            else:
                self.player.frostbite()

            self.clock.tick(FPS)
            self.window.show(self.player.direction_index, self.camera.x, self.camera.y)
            self.event.update(self.window.view)

            if not self.event.paused:
                self.window.repeat(self.player, self.event.clicked, self.event.key)
                self.sounds_manager.unpause_sounds()
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
                    self.window.draw_laser(self.camera.x, self.camera.y)
                    self.window.draw_buttons()
            else:
                self.sounds_manager.pause_sounds()
                self.player.show_player(
                    self.window.screen,
                    self.camera.x,
                    self.camera.y,
                    self.event.paused,
                )
                self.window.draw_laser(self.camera.x, self.camera.y)
                self.window.pause_menu(self.event.clicked)
                if self.window.pause_index:
                    self.window.pause_index = False
                    self.event.paused = False

            self.window.draw_buttons()
            pygame.display.update()
