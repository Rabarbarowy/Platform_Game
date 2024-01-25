import pygame
from pygame import QUIT

img = pygame.image.load('/home/krzysztof/dev/Platform_Game/src/assets/images/rabarbarowy_run.png')
cropped_img = img.subsurface((32, 0, img.get_width() - 32, 32))

screen = pygame.display.set_mode((800, 600))
color = (234, 212, 252)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            raise SystemExit

    screen.fill(color)
    screen.blit(img, (50, 50))
    screen.blit(cropped_img, (50, 100))

    pygame.display.update()
