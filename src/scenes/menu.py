import pygame

from src.objects.objects import Button
from src.scenes.window import Scene


class Menu(Scene):
    def __init__(self) -> None:
        super().__init__()
        self.draw_player = False

        self.buttons = [
            Button(430, 200, pygame.image.load('src/assets/images/play.png'), 'play'),
            Button(430, 500, pygame.image.load('src/assets/images/exit.png'), 'exit')
        ]

    def repeat(self) -> None:
        for button in self.buttons:
            button.draw(self.screen, button.x, button.y, True)
            button.click()
            if button.clicked:
                if button.name == 'play':
                    print('elo')
                elif button.name == 'exit':
                    raise SystemExit
