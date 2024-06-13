import pygame
from src.objects.objects import VisibleObject, Spike, SpecialBall, Teleporter, Button
from src.scenes.window import Scene


platform = pygame.image.load('src/assets/images/platforms/platform.png')
platform2 = pygame.image.load('src/assets/images/platforms/platform2.png')
platform3 = pygame.image.load('src/assets/images/platforms/platform3.png')
spike = pygame.image.load('src/assets/images/obstacles/spikes.png')
spike2 = pygame.image.load('src/assets/images/obstacles/spikes2.png')
red_ball = pygame.image.load('src/assets/images/red_ball.png')
blue_ball = pygame.image.load('src/assets/images/blue_ball.png')
green_ball = pygame.image.load('src/assets/images/green_ball.png')


class LevelChanger(Scene):
    def __init__(self):
        super().__init__()

    def menu(self):
        self.draw_player = False
        self.buttons = [
            Button(430, 200, pygame.image.load('src/assets/images/buttons/play.png'), 'play'),
            Button(430, 500, pygame.image.load('src/assets/images/buttons/exit.png'), 'exit'),
        ]
        self.objects_to_draw = []
        self.special_objects = []
        self.teleporters = []

    def level1(self):
        self.draw_player = True
        self.objects_to_draw = [
            VisibleObject(290, -1000, platform, 3, True),
            VisibleObject(290, 300, platform, 3, True),
            VisibleObject(482, 300, platform, 3, True),
            VisibleObject(674, 300, platform, 3, True),
            VisibleObject(1000, 300, platform, 3, True),
            VisibleObject(1000, 300, platform, 3, True),
            VisibleObject(1300, 250, platform, 3, True),
            VisibleObject(1600, 200, platform, 3, True),
            VisibleObject(1792, 200, platform, 3, True),
            VisibleObject(1984, 200, platform, 3, True),
            VisibleObject(2350, 200, platform3, 3, True),
            VisibleObject(2500, 000, platform2, 3, True),
            VisibleObject(3000, 300, platform, 3, True),
            VisibleObject(3192, 300, platform, 3, True),
        ]
        self.special_objects = [
            Spike(1996, 179, spike, 3),
            Spike(3080, 279, spike2, 3),
        ]
        self.teleporters = [
            Teleporter(3220, 156, 'level2'),
        ]
        self.buttons = []

    def level2(self):
        self.draw_player = True
        self.objects_to_draw = [
            VisibleObject(290, 300, platform, 3, True),
            VisibleObject(482, 300, platform, 3, True),
            VisibleObject(674, 300, platform, 3, True),
            VisibleObject(1000, 500, platform3, 3, True),
            VisibleObject(1150, 400, platform3, 3, True),
            VisibleObject(1400, 500, platform3, 3, True),
            VisibleObject(1550, 500, platform3, 3, True),
            VisibleObject(1700, 450, platform2, 3, True),
            VisibleObject(1800, 500, platform, 3, True),
            VisibleObject(2300, 700, platform, 3, True),
            VisibleObject(2500, 900, platform, 3, True),
            VisibleObject(2800, 900, platform, 3, True),
            VisibleObject(3000, 850, platform, 3, True),
            VisibleObject(3300, 780, platform2, 3, True),
            VisibleObject(3300, 460, platform2, 3, True),
            VisibleObject(3500, 850, platform, 3, True),
            VisibleObject(3800, 700, platform3, 3, True),
            VisibleObject(2700, 550, platform, 3, True),
            VisibleObject(3348, 460, platform, 3, True),
            VisibleObject(3540, 460, platform, 3, True),
            VisibleObject(3732, 460, platform, 3, True),
            VisibleObject(3924, 460, platform, 3, True),
            VisibleObject(3924, 721, platform3, 3, True),
            VisibleObject(4200, 700, platform3, 3, True),
            VisibleObject(4000, 700, platform3, 3, True),

            VisibleObject(3300, 1300, platform, 3, True),
            VisibleObject(3492, 1300, platform, 3, True),
            VisibleObject(3684, 1300, platform, 3, True),
            VisibleObject(3876, 1300, platform, 3, True),
            VisibleObject(4066, 1300, platform, 3, True),

            VisibleObject(4500, 750, platform, 3, True),
        ]
        self.special_objects = [
            Spike(686, 279, spike, 3),
            Spike(1403, 479, spike2, 3),
            Spike(1703, 429, spike2, 3),
            Spike(2447, 679, spike2, 3),
            Spike(2812, 879, spike, 3),
            Spike(3303, 759, spike2, 3),
            Spike(3360, 439, spike, 3),
            Spike(3744, 439, spike, 3),
            Spike(3927, 700, spike2, 3),

            Spike(3312, 1279, spike, 3),
            Spike(3504, 1279, spike, 3),
            Spike(3696, 1279, spike, 3),
            Spike(3888, 1279, spike, 3),
            Spike(4078, 1279, spike, 3),
        ]
        self.teleporters = [
            Teleporter(4530, 606, 'level2'),
        ]
        self.buttons = []
