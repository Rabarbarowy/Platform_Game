import pygame


class Scene:
    def __init__(self) -> None:
        self.WITDH = 800
        self.HEIGHT = 600

        self.back_ground_color = (234, 212, 252)
        self.screan = pygame.display.set_mode((self.WITDH, self.HEIGHT))

    def show(self) -> None:
        self.screan.fill(self.back_ground_color)
