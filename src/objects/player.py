import pygame
from pygame.key import ScancodeWrapper

from src.display import Drawable
from src.physic import Physic


class Player(Physic, Drawable):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load('src/assets/images/rabarbarowy.png')
        self.x = 350
        self.y = 0
        self.speed = 6

        self.jump_height = 9
        self.jumping = False

    def move(self, key) -> None:
        if key[pygame.K_d]:
            self.x += self.speed
        if key[pygame.K_a]:
            self.x -= self.speed
        if key[pygame.K_SPACE]:
            self.jump()

    def jump(self) -> None:
        self.graphitization_power -= 0.3
        if not self.in_air:
            self.graphitization_power -= self.jump_height
            self.in_air = True

    def repeat(self, key: ScancodeWrapper, player, second_objects) -> None:
        previous_x = self.x

        self.move(key)
        self.y = self.graphitization(self.y)

        for every_object in second_objects:
            self.collision(player, every_object, previous_x)
            if not self.in_air:
                break
