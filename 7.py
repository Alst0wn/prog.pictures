import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((350, 600))
screen.fill([102, 102, 102])

rect(screen, (0, 0, 0), (0, 240, 350, 360))
rect(screen, (26, 26, 26), (145, 65, 5, 40))
circle(screen, (230, 230, 230), (305, 50), 35)
polygon(screen, (0, 0, 0), [(0, 110), (50, 90),
                               (190, 90), (240, 110)])
rect(screen, (26, 26, 26), (72, 65, 5, 30))                               
ellipse(screen, (26, 26, 26), (185, 112, 185, 30))
ellipse(screen, (51, 51, 51), (60, 60, 220, 20))
ellipse(screen, (77, 77, 77), (165, 45, 185, 25))
ellipse(screen, (77, 77, 77), (240, 75, 185, 30))
rect(screen, (26, 26, 26), (185, 70, 5, 30))
rect(screen, (26, 26, 26), (80, 55, 10, 45))
rect(screen, (40, 34, 11), (30, 240, 180, 200))
rect(screen, (43, 34, 0), (30, 110, 180, 130))
rect(screen, (26, 26, 26), (0, 240, 240, 30))
rect(screen, (26, 26, 26), (14, 210, 6, 30))
rect(screen, (26, 26, 26), (220, 210, 6, 30))

color = [(43, 17, 0), (43, 17, 0), (212, 170, 0)]
x1 = 45
for i in range(3):
    rect(screen, color[i], (x1, 340, 40, 50))
    x1 += 55
x2 = 50
for i in range(4):
    rect(screen, (72, 62, 55), (x2, 110, 20, 130))
    x2 += 40

x3 = 50
for i in range(5):
    rect(screen, (26, 26, 26), (x3, 210, 12, 30))
    x3 += 32
rect(screen, (26, 26, 26), (20, 195, 200, 15))

#призрак

colour = (179, 179, 179)
colour2 = (135, 205, 222)
colour3 = (0, 0, 0)
colour4 = (255, 255, 255)
circle(screen, colour, (280, 440), 20)
polygon(screen, colour, ((280, 440), (270, 445), (250, 465), (225, 480),
    (210, 510), (236, 495), (248, 500), (265, 525), (280, 530), (310, 500),
    (325, 505), (335, 480), (350, 465), (330, 455), (315, 450), (280, 440)))
circle(screen, colour2, (271, 432), 5)
circle(screen, colour2, (289, 434), 5)
circle(screen, colour3, (269, 432), 1)
circle(screen, colour3, (287, 433), 1)
circle(screen, colour4, (270, 430), 1)
circle(screen, colour4, (288, 431), 1)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()