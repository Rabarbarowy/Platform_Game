import pygame
from pygame import Rect

from src.sprite import Sprite


class Drawable(Sprite):
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('src/assets/images/brak_grafiki.png')

    def cut_image_part(self, image, x_frame_pos: int, y_frame_pos: int, frame_width: int, frame_height: int):
        cropped_image = image.subsurface((x_frame_pos, y_frame_pos, frame_width, frame_height))
        return cropped_image

    def draw(self, screan, camera_x: int, camera_y: int,) -> None:
        screan.blit(self.image, (self.x - camera_x, self.y - camera_y))

    @property
    def width(self) -> int:
        return self.image.get_width()

    @property
    def height(self) -> int:
        return self.image.get_height()

    @property
    def hitbox(self) -> Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)
