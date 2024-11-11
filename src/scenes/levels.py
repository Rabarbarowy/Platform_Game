import pygame
from src.objects.objects import VisibleObject, Spike, SpecialBall, Teleporter, Button, Laser, Saw
from src.scenes.window import Scene


platform = pygame.image.load('src/assets/images/platforms/platform.png')
platform2 = pygame.image.load('src/assets/images/platforms/platform2.png')
platform3 = pygame.image.load('src/assets/images/platforms/platform3.png')
spike = pygame.image.load('src/assets/images/obstacles/spikes.png')
spike2 = pygame.image.load('src/assets/images/obstacles/spikes2.png')
spike3 = pygame.image.load('src/assets/images/obstacles/spikes3.png')
red_ball = pygame.image.load('src/assets/images/red_ball.png')
blue_ball = pygame.image.load('src/assets/images/blue_ball.png')
green_ball = pygame.image.load('src/assets/images/green_ball.png')

dash_text = pygame.image.load('src/assets/images/guide_texts/dash_text.png')
hang_text = pygame.image.load('src/assets/images/guide_texts/hang_text.png')
interact_text = pygame.image.load('src/assets/images/guide_texts/interact_text.png')
jump_higher_text = pygame.image.load('src/assets/images/guide_texts/jump_higher_text.png')
jump_text = pygame.image.load('src/assets/images/guide_texts/jump_text.png')
move_text = pygame.image.load('src/assets/images/guide_texts/move_text.png')
pause_text = pygame.image.load('src/assets/images/guide_texts/pause_text.png')
be_careful_text = pygame.image.load('src/assets/images/guide_texts/be_careful_text.png')
good_luck_text = pygame.image.load('src/assets/images/guide_texts/good_luck_text.png')
double_jump_text = pygame.image.load('src/assets/images/guide_texts/double_jump_text.png')
double_dash_text = pygame.image.load('src/assets/images/guide_texts/double_dash_text.png')
healing_text = pygame.image.load('src/assets/images/guide_texts/healing_text.png')
XD = pygame.image.load('src/assets/images/guide_texts/XD.png')

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
                if self.view == 'level3':
                    self.level3()
                if self.view == 'level4':
                    self.level4()
                if self.view == 'level5':
                    self.level5()
                if self.view == 'level6':
                    self.level6()
                if self.view == 'level7':
                    self.level7()
                if self.view == 'level8':
                    self.level8()
                if self.view == 'level9':
                    self.level9()
                if self.view == 'level10':
                    self.level10()
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
            VisibleObject(866, 300, platform, 3, True),
            VisibleObject(1058, 300, platform, 3, True),
            VisibleObject(1400, 300, platform, 3, True),
            VisibleObject(1800, 250, platform3, 3, True),
            VisibleObject(2100, 200, platform3, 3, True),
            VisibleObject(2400, 200, platform, 3, False),
            VisibleObject(2500, 600, platform, 3, True),
            VisibleObject(2800, 530, platform, 3, True),
            VisibleObject(3100, 450, platform, 3, True),
            VisibleObject(3650, 450, platform, 3, True),
            VisibleObject(4000, 350, platform3, 3, True),
            VisibleObject(4200, 300, platform3, 3, True),
            VisibleObject(4400, 300, platform3, 3, True),
            VisibleObject(4600, 300, platform3, 3, True),
            VisibleObject(4800, 100, platform2, 3, True),
            VisibleObject(5200, 300, platform, 3, True),
            VisibleObject(5392, 300, platform, 3, True),
            VisibleObject(5584, 300, platform, 3, True),

            VisibleObject(400, 30, move_text, 3, False),
            VisibleObject(1100, 30, jump_text, 3, False),
            VisibleObject(1700, -20, jump_higher_text, 3, False),
            VisibleObject(2450, 700, be_careful_text, 3, False),
            VisibleObject(3300, 170, dash_text, 3, False),
            VisibleObject(4500, -50, hang_text, 3, False),
            VisibleObject(5450, 0, interact_text, 3, False),
        ]
        self.special_objects = [
            Spike(2512, 579, spike, 3),
            Spike(4403, 279, spike2, 3),
        ]
        self.teleporters = [
            Teleporter(5420, 156, 'level2', aura_sound),
        ]
        self.buttons = []

    def level2(self) -> None:
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

            VisibleObject(400, 50, pause_text, 3, False),
            VisibleObject(900, 0, good_luck_text, 3, False),
        ]
        self.special_objects = [
            Spike(1996, 179, spike, 3),
            Spike(3080, 279, spike2, 3),
        ]
        self.teleporters = [
            Teleporter(3220, 156, 'level3', aura_sound),
        ]
        self.buttons = []

    def level3(self) -> None:
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
            Teleporter(4720, 606, 'level4', aura_sound),
        ]
        self.buttons = []

    def level4(self) -> None:
        self.draw_player = True
        self.objects_to_draw = [
            VisibleObject(290, -1000, platform, 3, True),
            VisibleObject(290, 300, platform, 3, True),
            VisibleObject(700, 200, platform, 3, True),
            VisibleObject(1000, 400, platform3, 3, True),
            VisibleObject(1210, 350, platform, 3, True),
            VisibleObject(1390, 350, platform3, 3, True),
            VisibleObject(1600, 100, platform3, 3, True),
            VisibleObject(1900, 100, platform3, 3, True),
            VisibleObject(2200, 400, platform, 3, True),
            VisibleObject(2650, 400, platform3, 3, False),
            VisibleObject(2900, 300, platform, 3, True),
            VisibleObject(2700, 1200, platform, 3, True),
            VisibleObject(2892, 1200, platform, 3, True),
            VisibleObject(3200, 1100, platform, 3, True),
            VisibleObject(3500, 1000, platform3, 3, True),
            VisibleObject(3700, 800, platform2, 3, True),
            VisibleObject(4000, 800, platform3, 3, True),
            VisibleObject(4350, 620, platform, 3, True),
            VisibleObject(4670, 620, platform, 3, True),
            VisibleObject(4950, 620, platform3, 3, True),
            VisibleObject(5350, 470, platform, 3, True),
            VisibleObject(5700, 360, platform, 3, True),
            VisibleObject(5892, 360, platform, 3, True),
            VisibleObject(6084, 228, platform2, 3, True),
            VisibleObject(6084, 36, platform2, 3, True),
            VisibleObject(5892, 36, platform, 3, True),

            VisibleObject(5200, 800, platform, 3, True),
            VisibleObject(5600, 1100, platform, 3, True),
            VisibleObject(5792, 1100, platform, 3, True),
            VisibleObject(5984, 1100, platform, 3, True),

            VisibleObject(1200, 0, double_jump_text, 3, False),
            VisibleObject(2900, 850, healing_text, 3, False),
        ]
        self.special_objects = [
            Spike(1222, 329, spike2, 3),
            Spike(1390, 329, spike2, 3),
            SpecialBall(1450, 130, green_ball, 'green'),
            Saw(1750, -200, 3, 20, 'down'),
            Spike(2212, 379, spike2, 3),
            Spike(2712, 1179, spike, 3),
            SpecialBall(3100, 1000, red_ball, 'red'),
            Saw(3850, 1300, 3, 30, 'top'),
            Saw(3850, 400, 3, 30, 'down'),
            Spike(4682, 599, spike, 3),
            Saw(5000, 700, 3, 20, 'right'),
        ]
        self.teleporters = [
            Teleporter(5820, 956, 'level5', aura_sound),
        ]
        self.buttons = []

    def level5(self) -> None:
        self.draw_player = True
        self.objects_to_draw = [
            VisibleObject(290, -10000, platform, 3, True),
            VisibleObject(290, 300, platform, 3, True),
            VisibleObject(800, 250, platform3, 3, True),
            VisibleObject(1200, 200, platform, 3, True),
            VisibleObject(2600, -100, platform, 3, True),
            VisibleObject(2900, -310, platform2, 3, True),
            VisibleObject(1500, -680, platform, 3, True),
            VisibleObject(2100, -770, platform, 3, True),
            VisibleObject(2292, -770, platform, 3, True),
            VisibleObject(2484, -770, platform, 3, True),
            VisibleObject(2676, -770, platform, 3, True),
            VisibleObject(2868, -770, platform, 3, True),
            VisibleObject(3900, 300, platform, 3, True),
            VisibleObject(4092, 300, platform, 3, True),
            VisibleObject(4284, 300, platform, 3, True),

            VisibleObject(2410, -1100, double_dash_text, 3, False),
        ]
        self.special_objects = [
            SpecialBall(1700, 100, green_ball, 'green'),
            SpecialBall(2000, 50, green_ball, 'green'),
            SpecialBall(2300, 0, green_ball, 'green'),
            SpecialBall(2500, -400, green_ball, 'green'),
            SpecialBall(2200, -450, green_ball, 'green'),
            SpecialBall(1900, -500, green_ball, 'green'),
            SpecialBall(2500, -840, blue_ball, 'blue'),
            SpecialBall(3300, -700, blue_ball, 'blue'),
            SpecialBall(3450, -600, blue_ball, 'blue'),
            SpecialBall(3600, -500, blue_ball, 'blue'),
            SpecialBall(3700, -380, blue_ball, 'blue'),
            SpecialBall(3800, -250, blue_ball, 'blue'),
            SpecialBall(3850, -130, blue_ball, 'blue'),
            SpecialBall(3900, -50, blue_ball, 'blue'),
        ]
        self.teleporters = [
            Teleporter(4120, 156, 'level6', aura_sound),
        ]
        self.buttons = []

    def level6(self) -> None:
        self.draw_player = True
        self.objects_to_draw = [
            VisibleObject(290, -10000, platform, 3, True),
            VisibleObject(290, 300, platform, 3, True),
            VisibleObject(482, 300, platform, 3, True),
            VisibleObject(674, 300, platform, 3, True),
            VisibleObject(900, 250, platform2, 3, True),
            VisibleObject(900, -90, platform2, 3, True),
            VisibleObject(1000, 300, platform, 3, True),
            VisibleObject(1300, 250, platform3, 3, True),
            VisibleObject(1450, 250, platform, 3, True),
            VisibleObject(1900, 300, platform, 3, True),
            VisibleObject(2200, 200, platform, 3, True),
            VisibleObject(2500, 100, platform, 3, True),
            VisibleObject(2692, 100, platform, 3, True),
            VisibleObject(3300, 200, platform3, 3, True),
            VisibleObject(3348, 200, platform, 3, True),
            VisibleObject(3540, 200, platform3, 3, True),
            VisibleObject(3588, 200, platform, 3, True),
            VisibleObject(3780, 200, platform3, 3, True),
            VisibleObject(4400, 200, platform, 3, True),
            VisibleObject(5200, 200, platform, 3, True),

            VisibleObject(-392, 1000, platform, 3, True),
            VisibleObject(-200, 1000, platform, 3, True),
            VisibleObject(-8, 1000, platform, 3, True),

            VisibleObject(5500, -100, XD, 3, False),
        ]
        self.special_objects = [
            Spike(903, 229, spike2, 3),
            Spike(1303, 229, spike2, 3),
            Saw(1650, 420, 3, 27, 'top'),
            Saw(1800, -120, 3, 27, 'down'),
            Spike(2044, 279, spike2, 3),
            Spike(2344, 179, spike2, 3),
            SpecialBall(2580, -150, green_ball, 'green'),
            SpecialBall(2580, -250, red_ball, 'red'),
            Saw(2850, -270, 3, 25, 'left'),
            Spike(3360, 179, spike, 3),
            Spike(3600, 179, spike, 3),
            SpecialBall(4000, 50, blue_ball, 'blue'),
            SpecialBall(4250, 50, blue_ball, 'blue'),
            SpecialBall(4700, 50, blue_ball, 'blue'),
            SpecialBall(4950, 50, blue_ball, 'blue'),
            SpecialBall(5350, 50, red_ball, 'red'),
        ]
        self.teleporters = [
            Teleporter(-170, 856, 'level7', aura_sound),
        ]
        self.buttons = []

    def level7(self) -> None:
        self.draw_player = True
        self.objects_to_draw = [
            VisibleObject(290, -10000, platform, 3, True),
            VisibleObject(290, 300, platform, 3, True),
            VisibleObject(600, -50, platform3, 3, True),
            VisibleObject(290, -200, platform3, 3, True),
            VisibleObject(500, -300, platform, 3, True),
            VisibleObject(1100, -300, platform, 3, True),
            VisibleObject(1100, -700, platform3, 3, True),
            VisibleObject(1400, -800, platform3, 3, True),
            VisibleObject(1300, -1000, platform3, 3, True),
            VisibleObject(200, -1100, platform, 3, True),
            VisibleObject(8, -1100, platform, 3, False),
            VisibleObject(-184, -1100, platform, 3, True),
            VisibleObject(-184, -1310, platform2, 3, True),
            VisibleObject(0, -1400, platform3, 3, True),
            VisibleObject(100, -1450, platform, 3, True),
            VisibleObject(700, -1550, platform2, 3, True),
            VisibleObject(700, -1650, platform3, 3, True),
            VisibleObject(700, -1850, platform2, 3, True),
            VisibleObject(550, -1745, platform3, 3, True),
            VisibleObject(550, -1950, platform2, 3, True),
            VisibleObject(700, -2050, platform2, 3, True),
            VisibleObject(550, -2150, platform2, 3, True),
            VisibleObject(700, -2250, platform2, 3, True),
            VisibleObject(550, -2350, platform2, 3, True),
            VisibleObject(700, -2450, platform2, 3, True),
            VisibleObject(200, -2400, platform, 3, True),
            VisibleObject(1400, -2300, platform, 3, True),
            VisibleObject(1592, -2300, platform, 3, True),
            VisibleObject(1784, -2300, platform, 3, True),
        ]
        self.special_objects = [
            SpecialBall(450, 100, green_ball, 'green'),
            Saw(490, -320, 3, 25, 'right'),
            SpecialBall(750, -450, blue_ball, 'blue'),
            SpecialBall(1300, -550, green_ball, 'green'),
            SpecialBall(1100, -1150, blue_ball, 'blue'),
            SpecialBall(850, -1150, blue_ball, 'blue'),
            SpecialBall(550, -950, green_ball, 'green'),
            Saw(100, -1480, 3,  0, 'right'),
            SpecialBall(950, -2400, red_ball, 'red'),
            SpecialBall(950, -2200, green_ball, 'green'),
            Spike(553, -2371, spike2, 3),
            Spike(703, -2471, spike2, 3),
            SpecialBall(500, -2650, green_ball, 'green'),
        ]
        self.teleporters = [
            Teleporter(1620, -2444, 'level8', aura_sound),
        ]
        self.buttons = []

    def level8(self):
        self.draw_player = True
        self.objects_to_draw = [
            VisibleObject(290, -10000, platform, 3, True),
            VisibleObject(290, 300, platform, 3, True),
            VisibleObject(-290, 300, platform, 3, True),
            VisibleObject(-500, 100, platform3, 3, True),
            VisibleObject(-800, 150, platform3, 3, True),
            VisibleObject(-1100, 100, platform, 3, True),
            VisibleObject(-1300, -100, platform2, 3, True),
            VisibleObject(-1100, -210, platform3, 3, True),
            VisibleObject(-800, -300, platform3, 3, True),
            VisibleObject(-500, -200, platform, 3, True),
            VisibleObject(-250, -150, platform2, 3, True),
            VisibleObject(-200, 0, platform, 3, True),
            VisibleObject(-8, 0, platform, 3, True),
            VisibleObject(200, -100, platform3, 3, True),
            VisibleObject(300, -200, platform3, 3, True),
            VisibleObject(400, -300, platform3, 3, True),
            VisibleObject(500, -400, platform3, 3, True),
            VisibleObject(600, -500, platform3, 3, True),
            VisibleObject(700, -600, platform3, 3, True),
            VisibleObject(800, -700, platform3, 3, True),
            VisibleObject(900, -800, platform3, 3, False),
            VisibleObject(1000, -900, platform3, 3, False),
            VisibleObject(1100, -1000, platform3, 3, True),
            VisibleObject(1200, -1100, platform3, 3, True),

            VisibleObject(1250, -300, platform, 3, True),
            VisibleObject(1442, -300, platform, 3, True),
            VisibleObject(1634, -300, platform, 3, True),
            VisibleObject(1826, -300, platform, 3, True),
            VisibleObject(2018, -300, platform, 3, True),

            VisibleObject(1442, -550, platform, 3, True),
            VisibleObject(1634, -550, platform, 3, True),
            VisibleObject(1826, -550, platform, 3, True),
            VisibleObject(2018, -550, platform, 3, True),

            VisibleObject(2400, -350, platform, 3, True),
            VisibleObject(1300, -730, platform3, 3, True),
            VisibleObject(1600, -1200, platform3, 3, True),
            VisibleObject(2100, -1000, platform, 3, True),
            VisibleObject(2292, -1000, platform, 3, True),
            VisibleObject(2484, -1000, platform, 3, True),
        ]
        self.special_objects = [
            Saw(50, 450, 3, 25, 'top'),
            Spike(-985, 65, spike2, 5),
            Spike(-494, -228, spike2, 4),
            SpecialBall(-1500, -260, red_ball, 'red'),
            SpecialBall(-1700, -100, green_ball, 'green'),
            Spike(-247, -171, spike2, 3),
            Saw(1500, -250, 3, 20, 'top'),
            Saw(1700, -680, 3, 20, 'down'),
            Saw(1900, -250, 3, 20, 'top'),
            Saw(2100, -680, 3, 20, 'down'),
            SpecialBall(1300, -950, green_ball, 'green'),
        ]
        self.teleporters = [
            Teleporter(2320, -1144, 'level9', aura_sound),
        ]
        self.buttons = []

    def level9(self) -> None:
        self.draw_player = True
        self.objects_to_draw = [
            VisibleObject(290, -10000, platform, 3, True),
            VisibleObject(290, 300, platform, 3, True),
            VisibleObject(500, 100, platform2, 3, True),
            VisibleObject(500, -100, platform2, 3, True),
            VisibleObject(340, 550, platform, 3, True),
            VisibleObject(340, 550, platform, 3, True),
            VisibleObject(750, 150, platform3, 3, True),
            VisibleObject(1400, 150, platform, 3, True),
            VisibleObject(1650, -50, platform3, 3, True),
            VisibleObject(1650, -250, platform3, 3, True),
            VisibleObject(1650, -450, platform, 3, True),
            VisibleObject(1900, -700, platform, 3, True),
            VisibleObject(2100, -300, platform, 3, True),
            VisibleObject(2244, -500, platform3, 3, True),
            VisibleObject(2244, -700, platform3, 3, True),
            VisibleObject(1900, -900, platform3, 3, True),
            VisibleObject(1900, -1100, platform3, 3, True),
            VisibleObject(2280, -1280, platform2, 3, True),
            VisibleObject(2100, -1380, platform3, 3, True),
            VisibleObject(2280, -1480, platform2, 3, True),
            VisibleObject(2100, -1580, platform2, 3, True),
            VisibleObject(2280, -1680, platform2, 3, True),
            VisibleObject(2100, -1780, platform2, 3, True),
            VisibleObject(2280, -1880, platform2, 3, True),
            VisibleObject(2328, -1880, platform, 3, True),
            VisibleObject(2520, -1880, platform, 3, True),
            VisibleObject(2712, -1880, platform, 3, True),
        ]
        self.special_objects = [
            Spike(365, 348, spike3, 3),
            SpecialBall(630, 300, green_ball, 'green'),
            SpecialBall(630, -50, green_ball, 'green'),
            SpecialBall(650, -250, blue_ball, 'blue'),
            SpecialBall(850, -230, blue_ball, 'blue'),
            SpecialBall(1050, -200, blue_ball, 'blue'),
            SpecialBall(1250, -160, blue_ball, 'blue'),
            Spike(1730, -471, spike2, 3),
            Spike(1950, -655, spike3, 3),
            Spike(1912, -721, spike, 3),
            Spike(2103, -1801, spike2, 3),
        ]
        self.teleporters = [
            Teleporter(2550, -2024, 'level10', aura_sound),
        ]
        self.buttons = []

    def level10(self) -> None:
        self.draw_player = True
        self.objects_to_draw = [
            VisibleObject(290, -10000, platform, 3, True),
            VisibleObject(290, 300, platform, 3, True),
        ]
        self.special_objects = [

        ]
        self.teleporters = [

        ]
        self.buttons = []
