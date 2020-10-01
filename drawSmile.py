import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill([128, 128, 128])

circle(screen, (255, 255, 0), (200, 200), 150)
circle(screen, (0, 0, 0), (200, 200), 150, 3)
polygon(screen, (0, 0, 0), [(70,80), (180,120),
                               (174,130), (64,90)])
polygon(screen, (0, 0, 0), [(220,120), (330,90),
                               (337,100), (227,130)])
rect(screen, (0, 0, 0), (125, 280, 150, 30))
circle(screen, (255, 0, 0), (125, 140), 25)
circle(screen, (0, 0, 0), (125, 140), 25, 1)
circle(screen, (0, 0, 0), (125, 140), 10)
circle(screen, (255, 0, 0), (275, 138), 20)
circle(screen, (0, 0, 0), (275, 138), 20, 1)
circle(screen, (0, 0, 0), (275, 138), 7)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()