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

        self.max_jump_height = 100
        self.min_jump_height = 12
        self.jump_height = self.min_jump_height
        self.jumping = False

    def move(self, key) -> None:
        if key[pygame.K_d]:
            self.x += self.speed
        if key[pygame.K_a]:
            self.x -= self.speed
        if key[pygame.K_SPACE]:
            self.jumping = True
            self.jump()
        # else:
        #     self.jumping = False

    def jump(self) -> None:
        if not self.in_air:
            self.graphitization_power -= self.jump_height
            # self.y -= self.jump_height
            self.in_air = True

    def repeat(self, key: ScancodeWrapper, player: object, second_object: object) -> None:
        previous_x = self.x

        self.move(key)
        self.y = self.graphitization(self.y)
        self.collision(player, second_object, previous_x)
