import pygame
from pygame.key import ScancodeWrapper

from src.animation import AnimateSprite
from src.display import Drawable
from src.objects.objects import VisibleObject, Heart
from src.physic import Physic


class Player(Physic, Drawable):
    def __init__(self, initial_coordinates: list, camera_y: int) -> None:
        super().__init__()
        AnimateSprite.__init__(self)
        # Images
        self.source_image = self.transform_size(pygame.image.load('src/assets/images/rabarbarowy.png'), 3)
        self.run_image = self.transform_size(pygame.image.load('src/assets/images/rabarbarowy_run.png'), 3)
        self.jumping_image = self.transform_size(pygame.image.load('src/assets/images/rabarbarowy_jumping.png'), 3)
        self.falling_iamge = self.transform_size(pygame.image.load('src/assets/images/rabarbarowy_falling.png'), 3)
        self.image = self.source_image

        self.life_element = pygame.image.load('src/assets/images/life_element.png')

        # Coordinates Properties
        self.start_x, self.start_y = initial_coordinates
        self.x = self.start_x
        self.y = self.start_y

        # Statistics Property
        self.speed = 6
        self.jump_height = 8
        self.invisible_time = 0

        # Action Status
        self.jumping = False
        self.falling = False
        self.running_right = False
        self.running_left = False
        self.attacked = False
        self.invisible = False

        # Direction
        self.direction = 'right'
        self.direction_index = self.x - self.start_x

        self.gravitation_index = GravitationIndex(self.width, self.height)

        # HP Properties
        self.max_hp = 3
        self.hp = self.max_hp
        self.immortal_time = 0
        self.life_bar = [
            Heart(self.x - 300, camera_y - self.y + 20)
        ]
        self.life_bar[0].heart_beating(len(self.life_bar))
        for i in range(self.max_hp):
            self.life_bar.append(VisibleObject(self.life_bar[-1].x + self.life_bar[-1].width, camera_y - self.y + 20, self.life_element, 2, collision=False))

    def move(self, key: ScancodeWrapper) -> None:
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
        self.direction_index = (self.x - self.start_x) / 8

    def jump(self) -> None:
        if not self.gravitation_power >= 0:
            self.gravitation_power -= 0.3
        if not self.in_air:
            self.gravitation_power -= self.jump_height
            self.in_air = True
            self.jumping = True

    def direction_of_player(self) -> None:
        if self.direction == 'right':
            self.image = pygame.transform.flip(self.image, False, False)
        elif self.direction == 'left':
            self.image = pygame.transform.flip(self.image, True, False)

    def check_collision(self, player, second_objects, previous_x: int) -> None:
        on_something = False
        for every_object in second_objects:
            if every_object.collision:
                self.collision(player, every_object, previous_x, self.gravitation_index, self.jumping)
            if not self.in_air:
                on_something = True

        if on_something:
            self.in_air = False

    def show_hp(self, screen, paused):
        index = 0
        if not paused:
            self.life_bar[0].heart_beating(self.hp)
        for element in self.life_bar:
            element.draw(screen, element.x, element.y, True)
            index += 1
            if index == self.hp:
                break

    def immortal(self):
        if self.attacked:
            self.immortal_time += 1
            self.invisible_time += 1
            if self.invisible_time == 5:
                self.invisible = True
            if self.invisible_time == 10:
                self.invisible = False
                self.invisible_time = 0
            if self.immortal_time == 80:
                self.immortal_time = 0
                self.attacked = False

    def die(self):
        if self.hp == 0:
            self.hp = self.max_hp
            self.x = self.start_x
            self.y = self.start_y
            self.in_air = True

        if self.y >= 1000:
            self.hp -= 1
            self.y = self.start_y
            self.gravitation_power = 1
            self.attacked = True

    def reset_statistic(self) -> None:
        self.x = self.start_x
        self.y = self.start_y
        self.hp = self.max_hp
        self.in_air = True
        self.invisible = False
        self.attacked = False
        self.gravitation_power = 1
        self.immortal_time = 0
        self.direction = 'right'

    def repeat(self, key: ScancodeWrapper, player, second_objects) -> None:
        self.immortal()
        previous_x = self.x
        self.gravitation_index.update_position(self.x, self.y)

        self.move(key)
        self.image = self.animation(self.image, [96, 96])
        self.y = self.gravitation(self.y)

        self.check_collision(player, second_objects, previous_x)
        self.die()

    def show_player(self, screen, camera_x: int, camera_y: int, paused: bool) -> None:
        if not self.invisible:
            self.draw(screen, camera_x, camera_y, False)
        self.show_hp(screen, paused)


class GravitationIndex:
    def __init__(self, player_width: int, player_height: int) -> None:
        self.x = 0
        self.y = 0
        self.height = 1
        self.width = player_width
        self.player_height = player_height

    def update_position(self, player_x: int, player_y: int) -> None:
        self.x = player_x
        self.y = player_y + self.player_height + 1

    @property
    def hitbox(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
