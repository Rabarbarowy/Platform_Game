from gzip import GzipFile
from symtable import Class

import pygame
from pygame.key import ScancodeWrapper

from src.display import Drawable


class VisibleObject(Drawable):
    def __init__(self, x: int, y: int, image, size_index: int, collision: bool) -> None:
        super().__init__()
        self.source_image = self.transform_size(image, size_index)
        self.image = self.source_image
        self.x = x
        self.y = y
        self.collision = collision
        self.frame_position = 0
        self.need_to_active = False


class Heart(VisibleObject):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x=x, y=y, image=pygame.image.load('src/assets/images/heart.png'), size_index=2, collision=False)
        self.beating_index = 0

    def heart_beating(self, number_of_life_bars):
        self.beating_index += 1
        if number_of_life_bars == 1:
            self.image = self.animation(self.source_image, [64, 64])

        elif self.beating_index <= 36:
            self.image = self.animation(self.source_image, [64, 64])
        if self.beating_index > 70:
            self.beating_index = 0


class Spike(VisibleObject):
    def __init__(self, x: int, y: int, image, size_index: int) -> None:
        super().__init__(x=x, y=y, image=image, size_index=size_index, collision=False)
        self.dmg = 1
        self.giving_damage_sound = pygame.mixer.Sound('src/assets/sounds/punch.mp3')

    def action(self, enemy) -> None:
        if enemy.hitbox.colliderect(self.hitbox):
            if not enemy.attacked:
                enemy.attacked = True
                enemy.hp -= self.dmg
                self.giving_damage_sound.play()


class Button(VisibleObject):
    def __init__(self, x: int, y: int, img, name_of_function: str) -> None:
        super().__init__(x=x, y=y, image=img, size_index=3, collision=False)
        self.name = name_of_function
        self.pressed = False
        self.hovered = False

    def check_action(self, clicked) -> None:
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            self.hovered = True
            if clicked:
                self.pressed = True
            else:
                self.pressed = False
        else:
            self.hovered = False


class SpecialBall(VisibleObject):
    def __init__(self, x: int, y: int, image, color: str) -> None:
        super().__init__(x=x, y=y, image=image, size_index=3, collision=True)
        self.color = color
        self.active = True
        self.cooldown = 0
        self.inactive_ball = self.transform_size(pygame.image.load('src/assets/images/grey_ball.png'), 3)
        self.image_to_draw = self.source_image
        self.need_to_active = True

    def action(self, player) -> None:
        self.check_active()
        self.image = self.animation(self.image_to_draw, (16*3, 16*3))
        if player.hitbox.colliderect(self.hitbox):
            if self.active:
                if self.color == 'red':
                    self.red_action(player)
                elif self.color == 'blue':
                    self.blue_action(player)
                elif self.color == 'green':
                    self.green_action(player)

    def red_action(self, player) -> None:
        if player.hp < player.max_hp:
            player.hp += 1
            self.active = False

    def blue_action(self, player) -> None:
        player.dash_index = 0
        player.cooldown_index = player.cooldown

    def green_action(self, player) -> None:
        if self.cooldown == 0:
            player.double_jump = True
            self.active = False
            self.cooldown = 300

    def check_active(self) -> None:
        if self.active:
            self.image_to_draw = self.source_image
        else:
            self.image_to_draw = self.inactive_ball
            self.cooldown -= 1
            if self.cooldown == 0:
                self.active = True


class Teleporter(VisibleObject):
    def __init__(self, x: int, y: int, next_level: str, sound) -> None:
        super().__init__(x=x, y=y, image=pygame.image.load('src/assets/images/teleporter.png'), size_index=3, collision=False)
        self.working_teleporter = self.transform_size(pygame.image.load('src/assets/images/working_teleporter.png'), 3)
        self.aura_sound = sound
        self.aura_sound.set_volume(0.5)
        self.next_level = next_level

    def action(self, player, key: ScancodeWrapper):
        next = ''
        if player.hitbox.colliderect(self.hitbox):
            self.aura_sound.play()
            self.image = self.working_teleporter
            if key[pygame.K_e]:
                self.aura_sound.stop()
                next = self.next_level
        else:
            self.aura_sound.stop()
            self.image = self.source_image
            next = ''

        self.image = self.animation(self.image, (144, 144))
        return next


class Laser(VisibleObject):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x=x, y=y, image=pygame.image.load('src/assets/images/teleport_laser.png'), size_index=3, collision=False)
        self.laser_sound = pygame.mixer.Sound('src/assets/sounds/teleport.mp3')

    def laser_animation(self) -> None:
        self.image = self.animation(self.source_image, (48 * 3, 200 * 3))
        self.laser_sound.play()
        self.laser_sound.set_volume(0.3)


class Saw(VisibleObject):
    def __init__(self, x: int, y: int, size_index: int, speed: int, direction: str) -> None:
        super().__init__(x=x, y=y, image=pygame.image.load('src/assets/images/obstacles/saw.png'), size_index=size_index, collision=False)
        self.source_speed = speed
        self.speed = self.source_speed
        self.direction = direction
        self.dmg = 2
        self.giving_damage_sound = pygame.mixer.Sound('src/assets/sounds/punch.mp3')
        self.size_index = size_index

    def action(self, enemy) -> None:
        self.image = self.animation(self.source_image, [22 * self.size_index, 22 * self.size_index])
        if self.direction == 'right':
            self.x += self.speed
            if self.speed <= 0:
                self.speed = self.source_speed
                self.direction = 'left'
        elif self.direction == 'left':
            self.x -= self.speed
            if self.speed <= 0:
                self.speed = self.source_speed
                self.direction = 'right'
        elif self.direction == 'top':
            self.y -= self.speed
            if self.speed <= 0:
                self.speed = self.source_speed
                self.direction = 'down'
        elif self.direction == 'down':
            self.y += self.speed
            if self.speed <= 0:
                self.speed = self.source_speed
                self.direction = 'top'
        self.speed -= 0.5

        if enemy.hitbox.colliderect(self.hitbox):
            if not enemy.attacked:
                enemy.attacked = True
                enemy.hp -= self.dmg
                self.giving_damage_sound.play()


class Castle(VisibleObject):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x=x, y=y, image=pygame.image.load('src/assets/images/castle/castle.png'), size_index=3, collision=False)

    def action(self, player) -> None:
        if player.hitbox.colliderect(self.hitbox):
            player.walking = True
        else:
            player.walking = False


class Gate(VisibleObject):
    def __init__(self, x: int, y: int, next_level: str) -> None:
        super().__init__(x=x, y=y, image=pygame.image.load('src/assets/images/castle/gate.png'), size_index=3, collision=False)
        self.opening_gate = self.transform_size(pygame.image.load('src/assets/images/castle/opening_gate.png'), 3)
        self.open_gate_image = self.transform_size(pygame.image.load('src/assets/images/castle/open_gate.png'), 3)
        self.next_level = next_level
        self.gate_animation_index = 0
        self.enter_gate = False

    def gate_animation(self) -> None:
        if self.gate_animation_index <= 45:
            self.gate_animation_index += 1
            self.image = self.animation(self.opening_gate, (36 * 3, 50 * 3))
        else:
            self.image = self.open_gate_image

    def action(self, player, key: ScancodeWrapper):
        next = ''
        if player.hitbox.colliderect(self.hitbox) and self.x - player.x <= 4 and self.x - player.x >= -19:
            if key[pygame.K_e]:
                self.enter_gate = True
                next = self.next_level

        if self.enter_gate:
            self.gate_animation()
            if self.gate_animation_index >= 50:
                self.enter_gate = False

        return next

class Flag(VisibleObject):
    def __init__(self, x: int, y: int):
        super().__init__(x=x, y=y, image=pygame.image.load('src/assets/images/castle/flag.png'), size_index=3, collision=False)

    def action(self, player) -> None:
        self.image = self.animation(self.source_image, (63, 84))
