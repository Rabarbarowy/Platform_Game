import pygame

from src.constants import FPS

pygame.init()


class SoundManager:
    def __init__(self):
        self.moving = pygame.mixer.Sound('src/assets/sounds/kroki.mp3')
        self.index = 0

    def play_sound(self):
        if self.index == 0:
            self.moving.play()
            self.index = FPS

        self.index -= 1
