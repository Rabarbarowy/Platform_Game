# import pygame
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

a = 'elo ściero'
b = 'elo kolego'


def siema(string1, string2):
    if 'elo' in string1 and 'elo' in string2:
        print(string1, string2)


siema(a, b)
