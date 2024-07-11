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

    def action(self, enemy) -> None:
        if enemy.hitbox.colliderect(self.hitbox):
            if not enemy.attacked:
                enemy.attacked = True
                enemy.hp -= self.dmg


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

    def action(self, player) -> None:
        self.check_active()
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

    def green_action(self, player) -> None:
        if self.cooldown == 0:
            player.double_jump = True
            self.active = False

    def check_active(self) -> None:
        if self.active:
            self.image = self.source_image
        else:
            self.image = self.inactive_ball


class Teleporter(VisibleObject):
    def __init__(self, x: int, y: int, next_level) -> None:
        super().__init__(x=x, y=y, image=pygame.image.load('src/assets/images/teleporter.png'), size_index=3, collision=True)
        self.working_teleporter = self.transform_size(pygame.image.load('src/assets/images/working_teleporter.png'), 3)
        self.next_level = next_level

    def action(self, player, key: ScancodeWrapper) -> None:
        next = ''
        if player.hitbox.colliderect(self.hitbox):
            self.image = self.working_teleporter
            if key[pygame.K_e]:
                next = self.next_level
        else:
            self.image = self.source_image
            next = ''

        self.image = self.animation(self.image, (144, 144))
        return next


class Laser(VisibleObject):
    def __init__(self) -> None:
        super().__init__(x=0, y=0, image=pygame.image.load('src/assets/images/teleport_laser.png'), size_index=3, collision=False)
        self.time_index = 100
        self.laser_index = self.time_index

    def laser_animation(self, screen, player_x) -> None:
        self.image = self.animation(self.image, (48 * 3, 104 * 3))
        self.draw(screen, player_x, 0, True)
