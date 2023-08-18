import pygame


class Sprite:
    def transform_size(self, source_image, custom_width: int, custom_height: int):
        image = pygame.transform.scale(source_image, (custom_width, custom_height))
        return image
