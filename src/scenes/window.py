import pygame
from pygame.key import ScancodeWrapper

from src.constants import WINDOW_WIDTH, WINDOW_HEIGHT
from src.objects.objects import Button
from src.objects.player import Player
from src.sprite import Sprite


class Scene:
    def __init__(self) -> None:
        self.width = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT

        self.landscape_image = pygame.image.load('src/assets/images/background.png')
        self.castle_interior_image = pygame.image.load('src/assets/images/castle_background.png')
        self.background = Background(self.landscape_image)
        self.change_background_index = 110

        self.background_color = (234, 212, 252)
        self.background_image = self.background.img
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.what_background = 'landscape'
        self.old_view = ''
        self.view = 'menu'
        # self.view = 'level15'

        self.draw_player = True
        self.objects_to_draw = []
        self.special_objects = []
        self.teleporters = []
        self.checkpoints = []
        self.buttons = []
        self.pause_buttons = [
            Button(430, 200, pygame.image.load('src/assets/images/buttons/resume.png'), 'resume'),
            Button(430, 400, pygame.image.load('src/assets/images/buttons/back.png'), 'menu'),
        ]

        self.pause_index = False
        self.choose_mode = False
        self.hardcore_mode = False
        self.choose_level = False

        self.button_cooldown = 0

    def show(self, direction_index: int, camera_x: int, camera_y: int) -> None:
        self.screen.fill(self.background_color)
        if direction_index + 250 + WINDOW_WIDTH >= self.background.width:
            self.screen.blit(self.background_image.convert(), (-self.background.width + WINDOW_WIDTH, 0))
        elif direction_index + 250 <= 0:
            self.screen.blit(self.background_image.convert(), (0, 0))
        else:
            self.screen.blit(self.background_image.convert(), (-direction_index - 250, 0))

        for element in self.objects_to_draw:
            element.draw(self.screen, camera_x, camera_y, False)
        for element in self.special_objects:
            element.draw(self.screen, camera_x, camera_y, False)
        for element in self.teleporters:
            element.draw(self.screen, camera_x, camera_y, False)
        for element in self.checkpoints:
            element.draw(self.screen, camera_x, camera_y, False)

    def darken(self, dimensions: tuple, coordinates: tuple) -> None:
        obfuscate = pygame.Surface(dimensions)
        obfuscate.set_alpha(150)
        self.screen.blit(obfuscate, coordinates)

    def repeat(self, player: Player, clicked: bool, key: ScancodeWrapper) -> None:
        # print(self.view, self.old_view)
        for element in self.special_objects:
            element.action(player)
        for element in self.teleporters:
            changed_level = element.action(player, key)
            if changed_level != '':
                self.view = element.next_level
        for element in self.checkpoints:
            element.action(player)

        if player.died:
            for element in self.special_objects:
                if element.need_to_active:
                    element.active = True
                    element.cooldown = 0
            player.died = False

        for button in self.buttons:
            button.check_action(clicked)
            if button.hovered:
                self.darken((button.width, button.height), (button.x, button.y))
            if button.pressed and self.button_cooldown == 0:
                self.button_cooldown = 10
                if button.name == 'play':
                    self.choose_mode = True
                elif button.name == 'exit':
                    raise SystemExit
                elif button.name == 'yes_to_hardcore':
                    self.choose_mode = False
                    self.hardcore_mode = True
                    self.choose_level = True
                elif button.name == 'no_to_hardcore':
                    self.choose_mode = False
                    self.hardcore_mode = False
                    self.choose_level = True
                elif button.name == 'level1':
                    self.view = 'level1'
                    self.choose_level = False
                elif button.name == 'level2':
                    self.view = 'level2'
                    self.choose_level = False
                elif button.name == 'level3':
                    self.view = 'level3'
                    self.choose_level = False
                elif button.name == 'level4':
                    self.view = 'level4'
                    self.choose_level = False
                elif button.name == 'level5':
                    self.view = 'level5'
                    self.choose_level = False
                elif button.name == 'level6':
                    self.view = 'level6'
                    self.choose_level = False
                elif button.name == 'level7':
                    self.view = 'level7'
                    self.choose_level = False
                elif button.name == 'level8':
                    self.view = 'level8'
                    self.choose_level = False
                elif button.name == 'level9':
                    self.view = 'level9'
                    self.choose_level = False
                elif button.name == 'level10':
                    self.view = 'level10'
                    self.choose_level = False
                elif button.name == 'level11':
                    self.view = 'level11'
                    self.choose_level = False
                elif button.name == 'level12':
                    self.view = 'level12'
                    self.choose_level = False
                elif button.name == 'level13':
                    self.view = 'level13'
                    self.choose_level = False
                elif button.name == 'level14':
                    self.view = 'level14'
                    self.choose_level = False
                elif button.name == 'level15':
                    self.view = 'level15'
                    self.choose_level = False

        if not self.button_cooldown == 0:
            self.button_cooldown -= 1
        self.change_background()

    def draw_buttons(self) -> None:
        for button in self.buttons:
            button.draw(self.screen, button.x, button.y, True)
            if button.hovered:
                self.darken((button.width, button.height), (button.x, button.y))

    def pause_menu(self, clicked: bool) -> None:
        self.pause_index = False
        self.darken((self.width, self.height), (0, 0))
        for button in self.pause_buttons:
            button.draw(self.screen, button.x, button.y, True)
            button.check_action(clicked)
            if button.hovered:
                self.darken((button.width, button.height), (button.x, button.y))
            if button.pressed:
                if button.name == 'menu':
                    self.view = 'menu'
                elif button.name == 'resume':
                    self.pause_index = True
                button.pressed = False

    def change_background(self) -> None:
        # print(self.view, self.old_view)
        if len(self.view) == 7:
            if self.old_view == 'menu':
                self.background = Background(self.castle_interior_image)
                self.background_image = self.background.img
                self.change_background_index = 110
                self.what_background = 'castle'
            if self.change_background_index == 0:
                self.background = Background(self.castle_interior_image)
                self.background_image = self.background.img
                self.change_background_index = 110
                self.what_background = 'castle'
            elif self.what_background == 'landscape':
                self.change_background_index -= 1
        else:
            self.what_background = 'landscape'
            self.background = Background(self.landscape_image)
            self.background_image = self.background.img


class Background(Sprite):
    def __init__(self, back_img) -> None:
        self.img = self.transform_size(back_img, 4)
        self.width = self.img.get_width()
