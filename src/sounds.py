import pygame

from src.constants import FPS

pygame.init()


class SoundManager:
    def __init__(self) -> None:
        self.sound_index = 0
        self.music_index = 0
        self.levels_music = pygame.mixer.Sound("src/assets/sounds/background_music1.mp3")
        self.menu_music = pygame.mixer.Sound("src/assets/sounds/menu_music.mp3")
        self.background_music = self.menu_music
        self.background_music.set_volume(0.4)

    def play_sound(self, current_sound, sound_time: int) -> None:
        if self.sound_index == 0:
            current_sound.play()
            self.sound_index = sound_time

    def pause_sounds(self) -> None:
        pygame.mixer.pause()

    def unpause_sounds(self) -> None:
        pygame.mixer.unpause()

    def play_background_music(self) -> None:
        if self.music_index <= 0:
            self.background_music.play()
            self.music_index = self.background_music.get_length() * FPS
        self.music_index -= 1

    def change_music(self, game_view) -> None:
        if game_view == 'menu':
            self.background_music.stop()
            self.background_music = self.menu_music
            self.music_index = 0
            self.background_music.set_volume(0.4)
        elif game_view == 'level1':
            self.background_music.stop()
            self.background_music = self.levels_music
            self.music_index = 0
            self.background_music.set_volume(0.3)
