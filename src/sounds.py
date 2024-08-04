import pygame

from src.constants import FPS
from src.objects.player import Player

pygame.init()


class SoundManager:
    def __init__(self) -> None:
        self.sound_index = 0
        self.run_sound = pygame.mixer.Sound('src/assets/sounds/moving.mp3')
        self.current_sound = self.run_sound
        self.stop = False

    def play_sound(self) -> None:
        if self.sound_index == 0:
            self.current_sound.play()
            self.sound_index = FPS

    def use_manager(self, player: Player) -> None:
        if self.sound_index != 0:
            self.sound_index -= 1
        if player.running_left or player.running_right and not player.in_air:
            self.current_sound = self.run_sound
            self.play_sound()
            if player.frozen:
                self.current_sound.stop()
        else:
            self.current_sound.stop()
            self.sound_index = 0
