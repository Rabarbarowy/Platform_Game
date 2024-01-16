import pygame

from src.display import Drawable


class VisibleObject(Drawable):
    def __init__(self, x: int, y: int, image, size_index: int) -> None:
        super().__init__()
        self.source_image = self.transform_size(image, size_index)
        self.image = self.source_image
        self.x = x
        self.y = y
        self.frame_position = 0


class Heart(VisibleObject):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x=x, y=y, image=pygame.image.load('src/assets/images/heart.png'), size_index=2)
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
        super().__init__(x=x, y=y, image=image, size_index=size_index)
        self.dmg = 1

    def attacking(self, enemy):
        if enemy.hitbox.colliderect(self.hitbox):
            if not enemy.attacked:
                enemy.attacked = True
                enemy.hp -= self.dmg
