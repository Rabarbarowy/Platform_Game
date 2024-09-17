import pygame
from src.objects.objects import VisibleObject, Spike, SpecialBall, Teleporter, Button, Laser
from src.scenes.window import Scene


platform = pygame.image.load('src/assets/images/platforms/platform.png')
platform2 = pygame.image.load('src/assets/images/platforms/platform2.png')
platform3 = pygame.image.load('src/assets/images/platforms/platform3.png')
spike = pygame.image.load('src/assets/images/obstacles/spikes.png')
spike2 = pygame.image.load('src/assets/images/obstacles/spikes2.png')
red_ball = pygame.image.load('src/assets/images/red_ball.png')
blue_ball = pygame.image.load('src/assets/images/blue_ball.png')
green_ball = pygame.image.load('src/assets/images/green_ball.png')

aura_sound = pygame.mixer.Sound('src/assets/sounds/teleport_aura.mp3')


class LevelChanger(Scene):
    def __init__(self) -> None:
        super().__init__()
        self.time_index = 160
        self.change_level_animation_index = self.time_index
        self.x_for_laser = 0
        self.invisible_index = 52

        self.laser_to_draw = []

        self.reset_player_stats = False
        self.animation_started = False
        self.level_changed = False
        self.frozen_player = False
        self.invisible_player = True

    def draw_laser(self, camera_x: int, camera_y: int) -> None:
        for element in self.laser_to_draw:
            element.draw(self.screen, camera_x, camera_y, False)

    def change_level_animation(self, player_x: int) -> None:
        if self.change_level_animation_index != 0:
            self.change_level_animation_index -= 1
            if not self.animation_started:
                self.laser_to_draw.append(Laser(player_x - 35, self.x_for_laser))
                self.laser_to_draw[0].laser_animation()
                self.animation_started = True
            else:
                self.laser_to_draw[0].laser_animation()
        else:
            self.change_level_animation_index = self.time_index
            self.laser_to_draw.pop(0)
            self.animation_started = False

    def change_level(self, player_x: int) -> None:
        if self.old_view != self.view:
            self.frozen_player = True
            self.reset_player_stats = False
            if 'level' in self.old_view and 'level' in self.view:
                self.x_for_laser = self.teleporters[0].y - 456
                self.change_level_animation(player_x)
            if self.change_level_animation_index == self.invisible_index + 10:
                self.invisible_player = True
            if self.change_level_animation_index == self.time_index:
                if self.view == 'menu':
                    self.menu()
                if self.view == 'level1':
                    self.level1()
                if self.view == 'level2':
                    self.level2()
                    self.view = 'level1'
                self.reset_player_stats = True
                self.level_changed = True
                self.old_view = self.view

    def show_up_in_new_level(self, player_x: int, player_y: int) -> None:
        if self.level_changed:
            if 'level' in self.old_view and 'level' in self.view:
                self.x_for_laser = player_y - 300
                self.change_level_animation(player_x)
            else:
                self.invisible_player = True
            if self.change_level_animation_index == self.invisible_index:
                self.invisible_player = False
            if self.change_level_animation_index == self.time_index:
                self.level_changed = False
                self.frozen_player = False

    def menu(self) -> None:
        self.draw_player = False
        self.buttons = [
            Button(430, 200, pygame.image.load('src/assets/images/buttons/play.png'), 'play'),
            Button(430, 500, pygame.image.load('src/assets/images/buttons/exit.png'), 'exit'),
        ]
        self.objects_to_draw = []
        self.special_objects = []
        self.teleporters = []

    def level1(self) -> None:
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
            VisibleObject(3384, 300, platform, 3, True),
        ]
        self.special_objects = [
            Spike(1996, 179, spike, 3),
            Spike(3080, 279, spike2, 3),
        ]
        self.teleporters = [
            Teleporter(3220, 156, 'level2', aura_sound),
        ]
        self.buttons = []

    def level2(self) -> None:
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
            VisibleObject(4692, 750, platform, 3, True),
            VisibleObject(4882, 750, platform, 3, True),
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
            Teleporter(4720, 606, 'level2', aura_sound),
        ]
        self.buttons = []
