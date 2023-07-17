import pygame

from src.display import Drawable
from src.physic import Physic


class Player(Physic, Drawable):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load('src/assets/images/rabarbarowy.png')
        self.x = 350
        self.y = 0
        self.speed = 6
        self.jump_height = 12

    def move(self, key):
        if key[pygame.K_d]:
            self.x += self.speed
        if key[pygame.K_a]:
            self.x -= self.speed
        if key[pygame.K_SPACE]:
            self.jump()

    def jump(self):
        if self.in_air == False:
            self.graphitization_power -= self.jump_height
            self.in_air = True

    def repeat(self, key, player: object, second_object: object) -> None:
        previous_x = self.x
        previous_y = self.y

        self.move(key)
        self.y = self.graphitization(self.y)
        self.collision(player, second_object, previous_x, previous_y)
