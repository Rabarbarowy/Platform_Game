import pygame

from src.constants import WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND_IMAGE
from src.sprite import Sprite


class Scene:
    def __init__(self) -> None:
        self.width = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT

        self.background = Background()

        self.background_color = (234, 212, 252)
        self.background_image = self.background.img
        self.screen = pygame.display.set_mode((self.width, self.height))

    def show(self, direction_index) -> None:
        self.screen.fill(self.background_color)
        if direction_index + 250 + WINDOW_WIDTH >= self.background.width:
            self.screen.blit(self.background_image.convert(), (-self.background.width + WINDOW_WIDTH, 0))
        elif direction_index + 250 <= 0:
            self.screen.blit(self.background_image.convert(), (0, 0))
        else:
            self.screen.blit(self.background_image.convert(), (-direction_index - 250, 0))


class Background(Sprite):
    def __init__(self):
        self.img = self.transform_size(BACKGROUND_IMAGE, 4)
        self.width = self.img.get_width()
