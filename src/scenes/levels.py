import pygame

from src.objects.objects import VisibleObject, Spike
from src.scenes.window import Scene


platform = pygame.image.load('src/assets/images/platforms/platform.png')
platform2 = pygame.image.load('src/assets/images/platforms/platform2.png')
spike = pygame.image.load('src/assets/images/obstacles/spikes.png')


class FirstLevel(Scene):
    def __init__(self):
        super().__init__()
        self.view = 'level1'
        self.objects_to_draw = [
            VisibleObject(290, 300, platform, 3, True),
            VisibleObject(98, 300, platform, 3, True),
            VisibleObject(-94, 300, platform, 3, True),
            VisibleObject(-286, 300, platform, 3, True),
            VisibleObject(-300, 500, platform, 3, True),
            VisibleObject(-100, 400, platform, 3, True),
            VisibleObject(400, 400, platform, 3, True),
            VisibleObject(640, 500, platform, 3, True),
            VisibleObject(840, 550, platform, 3, True),
            VisibleObject(1000, 400, platform, 3, True),
            VisibleObject(1200, 350, platform2, 3, True),
            VisibleObject(1200, 550, platform2, 3, True),
            VisibleObject(1200, 750, platform2, 3, True),
        ]
        # self.hostile_objects = [
        #     Spike(640, 479, spike, 3),
        # ]


class SecondLevel(Scene):
    def __init__(self):
        super().__init__()
        self.view = 'level2'
        self.objects_to_draw = [
            VisibleObject(290, 300, platform, 3, True),
        ]
