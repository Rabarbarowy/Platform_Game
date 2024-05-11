# import pygame
# from pygame import QUIT
#
# img = pygame.image.load('/home/krzysztof/dev/Platform_Game/src/assets/images/rabarbarowy_run.png')
# cropped_img = img.subsurface((32, 0, img.get_width() - 32, 32))
#
# screen = pygame.display.set_mode((800, 600))
# color = (234, 212, 252)
#
#
# def fade(width, height):
#     fade = pygame.Surface((width, height))
#     alpha = 100
#     fade.set_alpha(alpha)
#     screen.blit(fade, (0, 0))
#
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             print('elo')
#         if event.type == QUIT:
#             raise SystemExit
#
#     screen.fill(color)
#     screen.blit(img, (50, 50))
#     screen.blit(cropped_img, (50, 100))
#     fade(800, 600)
#     screen.blit(img, (300, 50))
#
#     pygame.display.update()

import pygame, sys
from pydub import AudioSegment
from pygame.locals import *

pygame.init()

moving_sound = pygame.mixer.Sound('/home/krzysztof/dev/Platform_Game/src/assets/sounds/moving.mp3')


#Create a displace surface object
#Below line will let you toggle from maximize to the initial size
DISPLAYSURF = pygame.display.set_mode((400, 300), RESIZABLE)

mainLoop = True

while mainLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
    moving_sound.play()
    pygame.display.update()

pygame.quit()