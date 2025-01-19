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
        # self.view = 'level10'

        self.draw_player = True
        self.objects_to_draw = []
        self.special_objects = []
        self.teleporters = []
        self.buttons = []
        self.pause_buttons = [
            Button(430, 200, pygame.image.load('src/assets/images/buttons/resume.png'), 'resume'),
            Button(430, 400, pygame.image.load('src/assets/images/buttons/back.png'), 'menu'),
        ]

        self.pause_index = False

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

    def darken(self, dimensions: tuple, coordinates: tuple) -> None:
        obfuscate = pygame.Surface(dimensions)
        obfuscate.set_alpha(150)
        self.screen.blit(obfuscate, coordinates)

    def repeat(self, player: Player, clicked: bool, key: ScancodeWrapper) -> None:
        for element in self.special_objects:
            element.action(player)
        for element in self.teleporters:
            changed_level = element.action(player, key)
            if changed_level != '':
                self.view = element.next_level

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
            if button.pressed:
                if button.name == 'play':
                    self.view = 'level1'
                elif button.name == 'exit':
                    raise SystemExit

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
        if len(self.view) > 6:
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

    #
    def elo(self, key):
        if key[pygame.K_1]:
            self.view = 'level9'
    #


class Background(Sprite):
    def __init__(self, back_img) -> None:
        self.img = self.transform_size(back_img, 4)
        self.width = self.img.get_width()
