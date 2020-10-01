import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))
screen.fill([102, 102, 102])

rect(screen, (0, 0, 0), (0, 350, 800, 550))

def prizrac(x, y, r, a):
    colour = (179, 179, 179)
    colour2 = (135, 205, 222)
    colour3 = (0, 0, 0)
    colour4 = (255, 255, 255)
    kx = r / 20
    k = r / 20
    if a < 0:
        kx *= -1
    polygon(screen, colour, ((x, y), (int(x - kx * 10) , int(y + k * 5)), (int(x - kx * 30), int(y + k * 25)), 
     (int(x - kx * 55), int(y + k * 40)), (int(x - kx * 70), int(y + k * 70)), (int(x - kx * 44), int(y + k * 55)), 
     (int(x - kx * 32), int(y + k * 60)), (int(x - kx * 15), int(y + k * 85)), (x, int(y + k * 90)),
     (int(x + kx * 30), int(y + k * 60)), (int(x + kx * 45), int(y + k * 65)), (int(x + kx * 55), int(y + k * 40)), 
     (int(x + kx * 70), int(y + k * 25)), (int(x + kx * 50), int(y + k * 15)), (int(x + kx * 35), int(y + k * 10)), (x, y)))
    aalines(screen, colour3, True, ((x, y), (int(x - kx * 10) , int(y + k * 5)), 
     (int(x - kx * 30), int(y + k * 25)), (int(x - kx * 55), int(y + k * 40)),
     (int(x - kx * 70), int(y + k * 70)), (int(x - kx * 44), int(y + k * 55)), 
     (int(x - kx * 32), int(y + k * 60)), (int(x - kx * 15), int(y + k * 85)), 
     (x, int(y + k * 90)), (int(x + kx * 30), int(y + k * 60)), (int(x + kx * 45), int(y + k * 65)), 
     (int(x + kx * 55), int(y + k * 40)), (int(x + kx * 70), int(y + k * 25)), 
     (int(x + kx * 50), int(y + k * 15)), (int(x + kx * 35), int(y + k * 10)), (x, y)), 1)
    circle(screen, colour, (x, y), r)
    circle(screen, colour3, (x, y), r, 1)
    circle(screen, colour, (x, y + r), r)
    circle(screen, colour2, (x - r // 2, y - r // 2 + 1), r // 4 + 1)
    circle(screen, colour2, (x + r // 2, y - r // 2 + 3), r // 4 + 1)
    if a > 0:
        circle(screen, colour2, (x - r // 2, y - r // 2 + 1), r // 4 + 1)
        circle(screen, colour2, (x + r // 2, y - r // 2 + 3), r // 4 + 1)
        circle(screen, colour3, (x - r // 2 - 1, y - r // 2 + 1), r // 20 + 1)
        circle(screen, colour3, (x + r // 2 - 1, y - r // 2 + 3), r // 20 + 1)
        circle(screen, colour4, (x - r // 2, y - r // 2 - 1), r // 20 + 1)
        circle(screen, colour4, (x + r // 2, y - r // 2 + 1), r // 20 + 1)
    else:
        circle(screen, colour2, (x - r // 2, y - r // 2 + 3), r // 4 + 1)
        circle(screen, colour2, (x + r // 2, y - r // 2 + 1), r // 4 + 1)
        circle(screen, colour3, (x - r // 2, y - r // 2 + 3), r // 20 + 1)
        circle(screen, colour3, (x + r // 2, y - r // 2 + 1), r // 20 + 1)
        circle(screen, colour4, (x - r // 2 - 1, y - r // 2 + 1), r // 20 + 1)
        circle(screen, colour4, (x + r // 2 - 1, y - r // 2 - 1), r // 20 + 1)
    

def dom(x, y, h, w):
    colour = (26, 26, 26)
    rect(screen, colour, (x + w // 2 + w // 12,y - 18 * h // 80 , w // 30, h // 5))#труба
    polygon(screen, (0, 0, 0), [(x - w // 6, y), (x, y - h // 10),
                               (x + w, y - h // 10), (x + w + w // 6, y)])
    rect(screen, colour, (x + 7 * w // 8, y - h // 8, w // 30, h // 12))#труба                               
    rect(screen, colour, (x + w // 3, y - 2 * h // 10 - 10, w // 30, h // 5))#труба
    rect(screen, colour, (x + w // 2, y - 2 * h // 10, w // 15, h // 8))#труба
    rect(screen, (40, 34, 11), (x, y + h - 6 * h // 10, w, 6 * h // 10))
    rect(screen, (43, 34, 0), (x, y, w, h - 6 * h // 10))
    x2 = x + w // 9
    for i in range(4):
        rect(screen, (72, 62, 55), (x2, y, w // 9, h - 6 * h // 10))
        x2 += 2 * w // 9
    rect(screen, colour, (x - w // 6, y + h - 7 * h // 10, w + 2 * w // 6, h // 10))
    rect(screen, colour, (x - 16, y + h - 8 * h // 10, 6, h // 10))#крайнее звено
    rect(screen, colour, (x + w + 10, y + h - 8 * h // 10, 6, h // 10))#крайнее звено
    rect(screen, (26, 26, 26), (x - 10, y + h - 8 * h // 10 - h // 20, w + 20, h // 20))#перила сверху

    color = [(43, 17, 0), (43, 17, 0), (212, 170, 0)]
    x1 = x + w // 7
    for i in range(3):
        rect(screen, color[i], (x1, y + 6 * h // 10, w // 7, 2 * h // 10))
        x1 += 2 * w // 7
    
    x3 = x - 10 + (w + 20) // 11
    for i in range(5):
        rect(screen, (26, 26, 26), (x3, y + 2 * h // 10, (w + 20) // 11, h // 10))
        x3 += 2 * (w + 20) // 11


#surf = pygame.Surface((475, 70), pygame.SRCALPHA)
#surf.fill([102, 102, 102])
#surf.set_alpha(100) не получилось(((((((((((((
circle(screen, (230, 230, 230), (650, 50), 55)
ellipse(screen, (77, 77, 77, 255), (400, 200, 475, 70))
ellipse(screen, (26, 26, 26), (175, 70, 510, 60))
ellipse(screen, (77, 77, 77), (280, 25, 475, 65))
ellipse(screen, (51, 51, 51), (355, 115, 475, 70))
ellipse(screen, (51, 51, 51), (60, 200, 346, 50))
#screen.blit(surf, (400, 200))

dom(650, 200, 210, 120)
dom(50, 330, 300, 180)
dom(350, 240, 240, 150)
prizrac(680, 500, 25, 1)
prizrac(730, 540, 15, 1)
prizrac(650, 600, 30, 1)
prizrac(580, 640, 20, 1)
prizrac(300, 540, 25, -1)
prizrac(320, 620, 15, -1)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()