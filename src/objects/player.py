import pygame
from pygame.key import ScancodeWrapper

from src.animation import AnimateSprite
from src.display import Drawable
from src.physic import Physic


class Player(Physic, Drawable, AnimateSprite):
    def __init__(self) -> None:
        super().__init__()
        AnimateSprite.__init__(self)
        self.source_image = self.transform_size(pygame.image.load('src/assets/images/rabarbarowy.png'), 3)
        self.run_image = self.transform_size(pygame.image.load('src/assets/images/rabarbarowy_run.png'), 3)
        self.jumping_image = self.transform_size(pygame.image.load('src/assets/images/rabarbarowy_jumping.png'), 3)
        self.falling_iamge = self.transform_size(pygame.image.load('src/assets/images/rabarbarowy_falling.png'), 3)
        self.image = self.source_image

        self.x = 350
        self.y = 0
        self.speed = 6
        self.jump_height = 9

        self.jumping = False
        self.falling = False
        self.running_right = False
        self.running_left = False

        self.direction = 'right'

        self.gravitation_index = GravitationIndex(self.width, self.height)

    def move(self, key) -> None:
        if key[pygame.K_d]:
            self.direction = 'right'
            self.running_right = True
            self.x += self.speed
            if not self.in_air:
                self.image = self.run_image
            else:
                self.running_right = False
        else:
            self.running_right = False

        if key[pygame.K_a]:
            self.direction = 'left'
            self.running_left = True
            self.x -= self.speed
            if not self.in_air:
                self.image = self.run_image
            else:
                self.running_left = False
        else:
            self.running_left = False

        if key[pygame.K_SPACE]:
            self.jump()

        if self.gravitation_power >= 0:
            self.jumping = False
            if self.in_air:
                self.falling = True
            else:
                self.falling = False

        if not self.running_right and not self.running_left and not self.jumping and not self.falling:
            self.image = self.source_image
        elif self.jumping:
            self.image = self.jumping_image
        elif self.falling:
            self.image = self.falling_iamge

        self.direction_of_player()

    def jump(self) -> None:
        if not self.gravitation_power >= 0:
            self.gravitation_power -= 0.3
        if not self.in_air:
            self.gravitation_power -= self.jump_height
            self.in_air = True
            self.jumping = True

    def direction_of_player(self):
        if self.direction == 'right':
            self.image = pygame.transform.flip(self.image, False, False)
        elif self.direction == 'left':
            self.image = pygame.transform.flip(self.image, True, False)

    def repeat(self, screan, camera_x, camera_y, key: ScancodeWrapper, player, second_objects) -> None:

        self.draw(screan, camera_x, camera_y)

        previous_x = self.x
        self.gravitation_index.update_position(self.x, self.y)

        self.move(key)
        self.image = self.animation(self.image, [96, 96])
        self.y = self.gravitation(self.y)
        for every_object in second_objects:
            self.collision(player, every_object, previous_x, self.gravitation_index, self.jumping)
            if not self.in_air:
                break


class GravitationIndex:
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
