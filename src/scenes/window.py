import pygame

from src.constants import WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND_IMAGE
from src.objects.objects import Button
from src.sprite import Sprite


class Scene:
    def __init__(self) -> None:
        self.width = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT

        self.background = Background(BACKGROUND_IMAGE)

        self.background_color = (234, 212, 252)
        self.background_image = self.background.img
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.old_view = 'menu'
        self.view = self.old_view

        self.draw_player = True
        self.objects_to_draw = []
        self.hostile_objects = []
        self.buttons = []
        self.pause_buttons = [
            # Button(430, 200, pygame.image.load('src/assets/images/play.png'), 'resume'),
            Button(430, 400, pygame.image.load('src/assets/images/exit.png'), 'menu'),
        ]

        self.obfuscate = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.obfuscate.set_alpha(150)
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
        for element in self.hostile_objects:
            element.draw(self.screen, camera_x, camera_y, False)

    def repeat(self, player, clicked) -> None:
        for element in self.hostile_objects:
            element.action(player)

        self.old_view = self.view
        for button in self.buttons:
            button.draw(self.screen, button.x, button.y, True)
            button.press(clicked)
            if button.pressed:
                if button.name == 'play':
                    self.view = 'level1'
                elif button.name == 'exit':
                    raise SystemExit

    def pause_menu(self, clicked):
        self.screen.blit(self.obfuscate, (0, 0))
        for button in self.pause_buttons:
            button.draw(self.screen, button.x, button.y, True)
            button.press(clicked)
            if button.pressed:
                if button.name == 'menu':
                    self.view = 'menu'
                if button.name == 'resume':
                    self.pause_index = True


class Background(Sprite):
    def __init__(self, back_img) -> None:
        self.img = self.transform_size(back_img, 4)
        self.width = self.img.get_width()
