import pygame
from pygame.key import ScancodeWrapper

from src.display import Drawable
from src.physic import Physic


class Player(Physic, Drawable):
    def __init__(self) -> None:
        super().__init__()
        self.source_image = pygame.image.load('src/assets/images/rabarbarowy.png')
        self.image = self.transform_size(self.source_image, 3)
        self.x = 350
        self.y = 0
        self.speed = 6

        self.jump_height = 9
        self.jumping = False

        self.graphitization_index = GraphitizationIndex(self.width, self.height)

    def move(self, key) -> None:
        if key[pygame.K_d]:
            self.x += self.speed
        if key[pygame.K_a]:
            self.x -= self.speed
        if key[pygame.K_SPACE]:
            self.jump()

    def jump(self) -> None:
        if not self.graphitization_power >= 0:
            self.graphitization_power -= 0.3
        if not self.in_air:
            self.graphitization_power -= self.jump_height
            self.in_air = True

    def repeat(self, screan, camera_x, camera_y, key: ScancodeWrapper, player, second_objects) -> None:
        self.draw(screan, camera_x, camera_y)
        previous_x = self.x
        self.graphitization_index.update_position(self.x, self.y)

        self.move(key)
        self.y = self.graphitization(self.y)

        for every_object in second_objects:
            self.collision(player, every_object, previous_x, self.graphitization_index)
            if not self.in_air:
                break


class GraphitizationIndex:
    def __init__(self, player_width, player_height):
        self.x = 0
        self.y = 0
        self.height = 1
        self.width = player_width
        self.player_height = player_height

    def update_position(self, player_x, player_y):
        self.x = player_x
        self.y = player_y + self.player_height + 1

    @property
    def hitbox(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
