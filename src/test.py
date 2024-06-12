import pygame
from pygame.locals import *

pygame.init()


class Game:
    def __init__(self):
        self.moving_sound = pygame.mixer.Sound('/home/krzysztof/dev/Platform_Game/src/assets/sounds/kroki.mp3')
        self.DISPLAYSURF = pygame.display.set_mode((400, 300), RESIZABLE)
        self.mainLoop = True

    def run(self):
        while self.mainLoop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.mainLoop = False
            self.moving_sound.play()
            pygame.display.update()

        pygame.quit()


Game().run()
