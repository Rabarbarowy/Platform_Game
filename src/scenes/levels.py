import pygame

from src.objects.objects import VisibleObject, Spike, SpecialBall
from src.scenes.window import Scene


platform = pygame.image.load('src/assets/images/platforms/platform.png')
platform2 = pygame.image.load('src/assets/images/platforms/platform2.png')
platform3 = pygame.image.load('src/assets/images/platforms/platform3.png')
spike = pygame.image.load('src/assets/images/obstacles/spikes.png')
spike2 = pygame.image.load('src/assets/images/obstacles/spikes2.png')
red_ball = pygame.image.load('src/assets/images/red_ball.png')
blue_ball = pygame.image.load('src/assets/images/blue_ball.png')
green_ball = pygame.image.load('src/assets/images/green_ball.png')


class FirstLevel(Scene):
    def __init__(self):
        super().__init__()
        self.view = 'level1'
        self.objects_to_draw = [
            VisibleObject(290, 300, platform, 3, True),
            VisibleObject(482, 300, platform, 3, True),
            VisibleObject(674, 300, platform, 3, True),
            VisibleObject(1000, 500, platform3, 3, True),
            VisibleObject(1150, 400, platform3, 3, True),
            VisibleObject(1450, 500, platform3, 3, True),
            VisibleObject(1550, 500, platform3, 3, True),
            VisibleObject(1700, 450, platform2, 3, True),
            VisibleObject(1800, 500, platform, 3, True),
            VisibleObject(2300, 700, platform, 3, True),
            VisibleObject(2500, 900, platform, 3, True),
            VisibleObject(2800, 900, platform, 3, True),
            VisibleObject(3000, 850, platform, 3, True),
        ]

        self.special_objects = [
            Spike(674, 279, spike, 3),
            Spike(1450, 479, spike2, 3),
            Spike(1700, 429, spike2, 3),
            Spike(2444, 679, spike2, 3),
            Spike(2800, 879, spike, 3),
        ]


class SecondLevel(Scene):
    def __init__(self):
        super().__init__()
        self.view = 'level2'
        self.objects_to_draw = [
            VisibleObject(290, 300, platform, 3, True),
        ]
