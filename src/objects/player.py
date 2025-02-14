from xml.etree.ElementPath import xpath_tokenizer

import pygame
from pygame.key import ScancodeWrapper

from src.animation import AnimateSprite
from src.constants import FPS, INITIAL_COORDINATES
from src.display import Drawable
from src.objects.objects import VisibleObject, Heart
from src.physic import Physic
from src.sounds import SoundManager


class Player(Physic, Drawable, SoundManager):
    def __init__(self, initial_coordinates: list, camera_y: int) -> None:
        super().__init__()
        AnimateSprite.__init__(self)
        SoundManager.__init__(self)
        # Images
        self.source_image = self.transform_size(pygame.image.load('src/assets/images/player/rabarbarowy.png'), 3)
        self.run_image = self.transform_size(pygame.image.load('src/assets/images/player/rabarbarowy_run.png'), 3)
        self.jumping_image = self.transform_size(pygame.image.load('src/assets/images/player/rabarbarowy_jumping.png'), 3)
        self.falling_image = self.transform_size(pygame.image.load('src/assets/images/player/rabarbarowy_falling.png'), 3)
        self.dash_image = self.transform_size(pygame.image.load('src/assets/images/player/rabarbarowy_dash.png'), 3)
        self.hanging_image = self.transform_size(pygame.image.load('src/assets/images/player/rabarbarowy_hanging.png'), 3)
        self.entering_gate_image = self.transform_size(pygame.image.load('src/assets/images/player/rabarbarowy_entering_gate.png'), 3)
        self.image = self.source_image
        self.life_element = pygame.image.load('src/assets/images/life_element.png')

        # Sounds
        self.run_sound = pygame.mixer.Sound('src/assets/sounds/moving.mp3')
        self.jump_sound = pygame.mixer.Sound('src/assets/sounds/jump.mp3')
        self.dash_sound = pygame.mixer.Sound('src/assets/sounds/jump.mp3')

        # Coordinates Properties
        self.start_x, self.start_y = initial_coordinates
        self.x = self.start_x
        self.y = self.start_y
        self.previous_x = self.x
        self.previous_y = self.y

        # Hitbox Properties
        self.left_hitbox_reduction = 20
        self.right_hitbox_reduction = 40

        # Statistics Property
        self.speed = 6
        self.dash_speed = self.speed * 1.5
        self.jump_height = 8
        self.invisible_time = 0

        # Action Status
        self.jumping = False
        self.falling = False
        self.double_jump = False
        self.running_right = False
        self.running_left = False
        self.attacked = False
        self.invisible = False
        self.dashing = False
        self.hanging = False
        self.can_move = True
        self.frozen = False
        self.impacted = False
        self.died = False
        self.entering_gate = False
        self.have_key = False
        self.finish_last_level = False

        self.dash_index = 0
        self.cooldown = 25
        self.cooldown_index = self.cooldown

        # Direction
        self.direction = 'right'
        self.direction_index = self.x - self.start_x

        self.gravitation_index = GravitationIndex(self.width, self.height, self.right_hitbox_reduction, self.left_hitbox_reduction)

        # HP Properties
        self.max_hp = 4
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

        if key[pygame.K_LSHIFT]:
            if self.cooldown_index == self.cooldown:
                self.dashing = True

        if self.dashing:
            self.dash()
            self.image = self.dash_image
        elif not self.running_right and not self.running_left and not self.jumping and not self.falling:
            self.image = self.source_image
        elif self.jumping:
            self.image = self.jumping_image
        elif self.falling:
            if self.hanging:
                self.image = self.hanging_image
            else:
                self.image = self.falling_image

        self.direction_of_player()
        self.direction_index = (self.x - self.start_x) / 8
        self.player_sound_play()

    def player_sound_play(self) -> None:
        if self.sound_index != 0:
            self.sound_index -= 1
        if not self.frozen:
            if self.running_left or self.running_right and not self.in_air:
                self.play_sound(self.run_sound, FPS)
            elif self.dashing:
                self.play_sound(self.dash_sound, FPS)
            else:
                self.sound_index = 0
                self.run_sound.stop()
                self.dash_sound.stop()
        else:
            self.sound_index = 0
            self.run_sound.stop()

    def jump(self) -> None:
        if not self.gravitation_power >= 0:
            self.gravitation_power -= 0.3
        if not self.in_air or self.hanging:
            self.gravitation_power -= self.jump_height
            self.in_air = True
            self.jumping = True
            self.hanging = False
            self.jump_sound.play()
        elif self.double_jump:
            self.jumping = True
            self.gravitation_power = 0
            self.gravitation_power -= self.jump_height + 3
            self.double_jump = False
            self.jump_sound.play()

    def dash(self) -> None:
        if self.dash_index != 10:
            if self.direction == 'right':
                self.x += self.dash_speed
            elif self.direction == 'left':
                self.x -= self.dash_speed
            self.dash_index += 1
        else:
            self.dashing = False
            self.dash_index = 0
            self.cooldown_index = 0

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
                self.double_jump = False

        if on_something:
            self.in_air = False

    def show_hp(self, screen, paused: bool) -> None:
        index = 0
        if not paused:
            self.life_bar[0].heart_beating(self.hp)
        for element in self.life_bar:
            element.draw(screen, element.x, element.y, True)
            index += 1
            if index == self.hp:
                break

    def immortal(self) -> None:
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

    def die(self) -> None:
        if self.hp <= 0:
            self.hp = self.max_hp
            self.x = self.start_x
            self.y = self.start_y
            self.in_air = True
            self.died = True

        if self.y >= 1800:
            self.hp = 0
            # self.y = self.start_y
            # self.x = self.start_x
            # self.gravitation_power = 1
            # self.attacked = True

    def reset_statistic(self) -> None:
        self.start_x, self.start_y = INITIAL_COORDINATES
        self.x = self.start_x
        self.y = self.start_y
        self.hp = self.max_hp
        self.in_air = True
        self.attacked = False
        self.gravitation_power = 1
        self.immortal_time = 0
        self.invisible_time = 0
        self.direction = 'right'
        self.have_key = False

    def froze(self) -> None:
        self.speed = 0
        self.jump_height = 0
        self.dash_speed = 0
        self.frozen = True

    def frostbite(self) -> None:
        self.speed = 6
        self.jump_height = 8
        self.dash_speed = self.speed * 1.5
        self.frozen = False

    def show_player(self, screen, camera_x: int, camera_y: int, paused: bool) -> None:
        if not self.invisible:
            self.draw(screen, camera_x, camera_y, False)
        self.show_hp(screen, paused)

    def hang(self) -> None:
        if self.falling and self.collided:
            if self.y - self.y_of_object >= -5 and self.y - self.y_of_object <= 10:
                self.gravitation_power = 0
                self.hanging = True
        else:
            self.hanging = False

    def repeat(self, key: ScancodeWrapper, player, second_objects) -> None:
        self.immortal()
        previous_x = self.x
        self.previous_x = previous_x
        self.gravitation_index.update_position(self.x, self.y)
        self.move(key)

        if self.frozen:
            self.image = self.source_image
        if self.entering_gate:
            self.image = self.entering_gate_image
        self.image = self.animation(self.image, [66, self.height])

        self.y = self.gravitation(self.y)

        self.check_collision(player, second_objects, previous_x)
        self.die()
        if self.cooldown != self.cooldown_index:
            self.cooldown_index += 1

        self.hang()
        self.collided = False


class GravitationIndex:
    def __init__(self, player_width: int, player_height: int, right_hitbox_reduction: int, left_hitbox_reduction: int) -> None:
        self.x = 0
        self.y = 0
        self.left_hitbox_reduction = left_hitbox_reduction
        self.right_hitbox_reduction = right_hitbox_reduction
        self.height = 1
        self.width = player_width - self.right_hitbox_reduction
        self.player_height = player_height

    def update_position(self, player_x: int, player_y: int) -> None:
        self.x = player_x + self.left_hitbox_reduction
        self.y = player_y + self.player_height + 1

    @property
    def hitbox(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
