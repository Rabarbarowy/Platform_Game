import pygame
# from pygame.locals import *
#
# pygame.init()
#
#
# class Game:
#     def __init__(self):
#         self.moving_sound = pygame.mixer.Sound('/home/krzysztof/dev/Platform_Game/src/assets/sounds/moving.mp3')
#         self.DISPLAYSURF = pygame.display.set_mode((400, 300), RESIZABLE)
#         self.mainLoop = True
#         self.stop = False
#         self.index = 0
#
#     def play_sound(self):
#         self.moving_sound.play()
#
#         if self.stop:
#             self.moving_sound.stop()
#
#     def elo(self):
#         if self.index == 1000:
#             self.stop = True
#
#         self.index += 1
#
#     def run(self):
#         while self.mainLoop:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     self.mainLoop = False
#
#             self.elo()
#             self.play_sound()
#             pygame.display.update()
#
#         pygame.quit()
#
#
# Game().run()
import pygame.mixer
from pygame.time import Clock

pygame.init()


def elo():
    clock = Clock()
    a = 0
    elo = pygame.mixer.Sound('/home/krzysztof/dev/Platform_Game/src/assets/sounds/teleport_aura.mp3')
    siema = pygame.mixer.Sound('/home/krzysztof/dev/Platform_Game/src/assets/sounds/teleport.mp3')
    siema.set_volume(0.3)
    channel1 = pygame.mixer.Channel(1)
    channel2 = pygame.mixer.Channel(2)
    while True:
        clock.tick(1)
        a += 1
        print(a)
        if a == 1:
            channel1.play(siema)
        if a >= 2:
            elo.play()
        if a >= 6:
            pygame.mixer.pause()
        if a >= 8:
            pygame.mixer.unpause()

elo()
