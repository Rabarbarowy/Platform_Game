import pygame

from src.sprite import Sprite


class AnimateSprite(Sprite):
    def animate_frame(self, image_of_activity, size_index: int):
        image = self.transform_size(image_of_activity, size_index)
        surf = pygame.Surface((96, 0))
        surf.blit(image, ())
        return 'something'
