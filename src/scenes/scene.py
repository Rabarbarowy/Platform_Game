import pygame


class Scene:
    def __init__(self) -> None:
        self.WIDTH = 800
        self.HEIGHT = 600

        self.back_ground_color = (234, 212, 252)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

    def show(self) -> None:
        self.screen.fill(self.back_ground_color)
