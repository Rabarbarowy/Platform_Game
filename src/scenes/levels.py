import pygame

from src.objects.objects import VisibleObject, Spike
from src.scenes.window import Scene


platform = pygame.image.load('src/assets/images/platform.png')
platform2 = pygame.image.load('src/assets/images/platform2.png')
spike = pygame.image.load('src/assets/images/spikes.png')


class FirstLevel(Scene):
    def __init__(self):
        super().__init__()
        
        self.objects_to_draw = [
            VisibleObject(290, 300, platform, 3, True),
            VisibleObject(-300, 500, platform, 3, True),
            VisibleObject(-100, 400, platform, 3, True),
            VisibleObject(400, 400, platform, 3, True),
            VisibleObject(640, 500, platform, 3, True),
            VisibleObject(1000, 400, platform, 3, True),
            VisibleObject(1200, 350, platform2, 3, True),

            Spike(640, 479, spike, 3),
        ]
