import pygame


class Sprite:
    def transform_size(self, source_image, size_index: int):
        width = source_image.get_width()
        height = source_image.get_height()
        image = pygame.transform.scale(source_image, (width * size_index, height * size_index))
        return image
