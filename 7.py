import pygame
from pygame.draw import *

pygame.init()

resolution = 800
FPS = 30
screen = pygame.display.set_mode((resolution, resolution))
screen.fill([102, 102, 102])

rect(screen, (0, 0, 0), (0, 350*resolution//800, resolution, 550*resolution//800))

def body(surface, color, outline, x, y, r, flipbool, resolution):
    '''
    function draws ghost's body
    arguments: (surface, color, ouline, x, y, r, flipbool, resolution)
    surface - surface on which the body is drawn - pygame.surface
    color - color of ghost's body in rgb with transparency
    outline - color of ghost's outline in rgb with transparency
    x, y - coordinates of centre of the head - 2 integers
    r - radius of ghost's head (whole ghost is scaled accordingly)
    flipbool - True if the ghost is looking right, False if left - bool
    resolution - screen resolution - integer
    '''
    bodysurf = pygame.Surface((resolution,resolution), pygame.SRCALPHA)
    k = r / 20
    kx = k * (1 - 2 * int(flipbool))
    polygon(bodysurf, color, ((x, y), (int(x - kx * 10) , int(y + k * 5)), (int(x - kx * 30), int(y + k * 25)),
     (int(x - kx * 55), int(y + k * 40)), (int(x - kx * 70), int(y + k * 70)), (int(x - kx * 44), int(y + k * 55)),
     (int(x - kx * 32), int(y + k * 60)), (int(x - kx * 15), int(y + k * 85)), (x, int(y + k * 90)),
     (int(x + kx * 30), int(y + k * 60)), (int(x + kx * 45), int(y + k * 65)), (int(x + kx * 55), int(y + k * 40)),
     (int(x + kx * 70), int(y + k * 25)), (int(x + kx * 50), int(y + k * 15)), (int(x + kx * 35), int(y + k * 10)), (x, y)))
    aalines(bodysurf, outline, True, ((x, y), (int(x - kx * 10) , int(y + k * 5)),
     (int(x - kx * 30), int(y + k * 25)), (int(x - kx * 55), int(y + k * 40)),
     (int(x - kx * 70), int(y + k * 70)), (int(x - kx * 44), int(y + k * 55)),
     (int(x - kx * 32), int(y + k * 60)), (int(x - kx * 15), int(y + k * 85)),
     (x, int(y + k * 90)), (int(x + kx * 30), int(y + k * 60)), (int(x + kx * 45), int(y + k * 65)),
     (int(x + kx * 55), int(y + k * 40)), (int(x + kx * 70), int(y + k * 25)),
     (int(x + kx * 50), int(y + k * 15)), (int(x + kx * 35), int(y + k * 10)), (x, y)), 1)
    circle(bodysurf, color, (x, y + r), r)
    circle(bodysurf, color, (x, y), r)
    circle(bodysurf, outline, (x, y), r, 1)
    surface.blit(bodysurf, (0,0))

def eyes(surface, color, iris_color, highlight_color, x, y, r, flipbool, resolution):
    '''
    function draws ghost's eyes
    arguments: (surface, color, iris_color, highlight_color, x, y, r, flipbool, resolution)
    surface - surface on which the eyes are drawn - pygame.surface
    color - color of ghost's eyes in rgb with transparency
    iris_color - color of ghost's irises in rgb with transparency
    highlight_color - color of little highlights in the eyes
    x, y - coordinates of centre of the head - 2 integers
    r - radius of ghost's head (whole ghost is scaled accordingly)
    flipbool - True if the ghost is looking right, False if left - bool
    resolution - screen resolution - integer
    '''
    eyesurf = pygame.Surface((resolution,resolution), pygame.SRCALPHA)   
    if flipbool:
        circle(eyesurf, color, (x - r // 2, y - r // 2 + 3), r // 4 + 1)
        circle(eyesurf, color, (x + r // 2, y - r // 2 + 1), r // 4 + 1)
        circle(eyesurf, iris_color, (x - r // 2, y - r // 2 + 3), r // 20 + 1)
        circle(eyesurf, iris_color, (x + r // 2, y - r // 2 + 1), r // 20 + 1)
        circle(eyesurf, highlight_color, (x - r // 2 - 1, y - r // 2 + 1), r // 20 + 1)
        circle(eyesurf, highlight_color, (x + r // 2 - 1, y - r // 2 - 1), r // 20 + 1)
    else:
        circle(eyesurf, color, (x - r // 2, y - r // 2 + 1), r // 4 + 1)
        circle(eyesurf, color, (x + r // 2, y - r // 2 + 3), r // 4 + 1)
        circle(eyesurf, iris_color, (x - r // 2 - 1, y - r // 2 + 1), r // 20 + 1)
        circle(eyesurf, iris_color, (x + r // 2 - 1, y - r // 2 + 3), r // 20 + 1)
        circle(eyesurf, highlight_color, (x - r // 2, y - r // 2 - 1), r // 20 + 1)
        circle(eyesurf, highlight_color, (x + r // 2, y - r // 2 + 1), r // 20 + 1)
    surface.blit(eyesurf, (0,0))

def ghost(surface, body_color, eye_color, x, y, r, flipbool, transparency, resolution):
    '''
    function draws a ghost
    arguments: (surface, body_color, eye_color, x, y, r, flipbool, transparency, resolution)
    surface - surface on which the ghost is drawn - pygame.surface
    body_color - color of ghost's body in rgb
    eye_color - color of ghost's eyes in rgb
    x, y - coordinates of centre of the head - 2 integers
    r - radius of ghost's head (whole ghost is scaled accordingly)
    flipbool - True if the ghost is looking right, False if left - bool
    transparency - ghost's transparency - integer from 0 to 255
    resolution - screen resolution - integer
    '''
    ghostsurf = pygame.Surface((resolution,resolution), pygame.SRCALPHA)
    outline_color = (0, 0, 0, transparency)
    highlight_color = (255, 255, 255, transparency)
    red, g, b = body_color
    body_color_t = (red, g, b, transparency)
    red, g, b = eye_color
    eye_color_t = (red, g, b, transparency)
    body(ghostsurf, body_color_t, outline_color, x, y, r, flipbool, resolution)
    eyes(ghostsurf, eye_color_t, outline_color, highlight_color, x, y, r, flipbool, resolution)
    surface.blit (ghostsurf, (0, 0))

def house(surface, x, y, h, w, transparency, resolution):
    '''
    function draws a house
    arguments: (surface, x, y, h, w, transparency, resolution)
    surface - surface on which the house is drawn - pygame.surface
    x, y - coordinates of the top left corner of the wall (below the roof)- 2 integers
    h, w - height and width of the house - 2 integers
    transparency - house's transparency - integer from 0 to 255
    resolution - screen resolution - integer
    '''
    housesurf = pygame.Surface((resolution,resolution), pygame.SRCALPHA)
    colour = (26, 26, 26, transparency)
    roof(housesurf, (0, 0, 0, transparency), colour, x, y, h, w, resolution)
    rect(housesurf, (40, 34, 11, transparency), (x, y + h - 6 * h // 10, w, 6 * h // 10))
    rect(housesurf, (43, 34, 0, transparency), (x, y, w, h - 6 * h // 10))
    x2 = x + w // 9
    for i in range(4):
        rect(housesurf, (72, 62, 55, transparency), (x2, y, w // 9, h - 6 * h // 10))
        x2 += 2 * w // 9
    color = [(43, 17, 0, transparency), (43, 17, 0, transparency), (212, 170, 0, transparency)]
    x1 = x + w // 7
    for i in range(3):
        rect(housesurf, color[i], (x1, y + 6 * h // 10, w // 7, 2 * h // 10))
        x1 += 2 * w // 7
    railings(housesurf, colour, x, y, h, w, resolution)
    surface.blit(housesurf, (0, 0))

def railings(surface, colour, x, y, h, w, resolution):
    '''
    function draws railings
    arguments: (surface, colour, x, y, h, w, transparency, resolution)
    surface - surface on which the house is drawn - pygame.surface
    colour - colour of the railings rgb with transparency
    x, y - coordinates of the top left corner of the wall of the house (railings placed accordingly)- 2 integers
    h, w - height and width of the house (railings scaled accordingly) - 2 integers
    resolution - screen resolution - integer
    '''
    railsurf = pygame.Surface((resolution,resolution), pygame.SRCALPHA)
    rect(railsurf, colour, (x - w // 6, y + h - 7 * h // 10, w + 2 * w // 6, h // 10))
    rect(railsurf, colour, (x - 16, y + h - 8 * h // 10, 6, h // 10))
    rect(railsurf, colour, (x + w + 10, y + h - 8 * h // 10, 6, h // 10))
    rect(railsurf, colour, (x - 10, y + h - 8 * h // 10 - h // 20, w + 20, h // 20))
    x3 = x - 10 + (w + 20) // 11
    for i in range(5):
        rect(railsurf, colour, (x3, y + 2 * h // 10, (w + 20) // 11, h // 10))
        x3 += 2 * (w + 20) // 11
    surface.blit(railsurf, (0, 0))

def roof(surface, roofcolour, pipecolour, x, y, h, w, resolution):
    '''
    function draws a roof with pipes
    arguments: (surface, roofcolour, pipecolour, x, y, h, w, resolution)
    surface - surface on which the house is drawn - pygame.surface
    roofcolour - colour of the roof rgb with transparency
    pipecolour - colour of the chimneys/pipes rgb with transparency
    x, y - coordinates of the top left corner of the wall of the house (roof placed accordingly)- 2 integers
    h, w - height and width of the house (roof scaled accordingly) - 2 integers
    resolution - screen resolution - integer
    '''
    roofsurf = pygame.Surface((resolution,resolution), pygame.SRCALPHA)
    rect(roofsurf, pipecolour, (x + w // 2 + w // 12,y - 18 * h // 80 , w // 30, h // 5))
    polygon(roofsurf, roofcolour, [(x - w // 6, y), (x, y - h // 10),
                               (x + w, y - h // 10), (x + w + w // 6, y)])
    rect(roofsurf, pipecolour, (x + 7 * w // 8, y - h // 8, w // 30, h // 12))
    rect(roofsurf, pipecolour, (x + w // 3, y - 2 * h // 10 - 10, w // 30, h // 5))
    rect(roofsurf, pipecolour, (x + w // 2, y - 2 * h // 10, w // 15, h // 8))
    surface.blit(roofsurf, (0, 0))
 
def cloud(surface, color, rect, resolution):
    '''
    function draws a cloud
    arguments: (surface, color, rect, resolution)
    surface - surface on which the cloud is drawn - pygame.surface
    color - color of the cloud in rgb with transparency
    rect - rectangle into which cloud is inscribed - pygame.rect
    resolution - screen resolution - integer
    '''
    cloudsurf = pygame.Surface((resolution, resolution), pygame.SRCALPHA)
    ellipse(cloudsurf, color, rect)
    surface.blit(cloudsurf, (0,0))


circle(screen, (230, 230, 230), (650*resolution//800, 
        50*resolution//800), 55*resolution//800)
cloud(screen, (77, 77, 77, 150), (400*resolution//800, 200*resolution//800,
        475*resolution//800, 70*resolution//800), resolution)
cloud(screen, (26, 26, 26, 150), (175*resolution//800, 70*resolution//800,
        510*resolution//800, 60*resolution//800), resolution)
cloud(screen, (77, 77, 77, 150), (280*resolution//800, 25*resolution//800,
        475*resolution//800, 65*resolution//800), resolution)
cloud(screen, (51, 51, 51, 150), (355*resolution//800, 115*resolution//800,
        475*resolution//800, 70*resolution//800), resolution)
cloud(screen, (51, 51, 51, 150), (60*resolution//800, 200*resolution//800,
        346*resolution//800, 50*resolution//800), resolution)

house(screen, 650*resolution//800, 200*resolution//800,
        210*resolution//800, 120*resolution//800, 255, resolution)
house(screen, 50*resolution//800, 330*resolution//800,
        300*resolution//800, 180*resolution//800, 255, resolution)
house(screen, 350*resolution//800, 240*resolution//800,
        240*resolution//800, 150*resolution//800, 255, resolution)

ghost_color = (179, 179, 179)
eye_color = (135, 205, 222)

ghost(screen, ghost_color, eye_color, 680*resolution//800,
        500*resolution//800, 25*resolution//800, False, 100, resolution)
ghost(screen, ghost_color, eye_color, 730*resolution//800,
        540*resolution//800, 15*resolution//800, False, 100, resolution)
ghost(screen, ghost_color, eye_color, 650*resolution//800,
        600*resolution//800, 30*resolution//800, False, 100, resolution)
ghost(screen, ghost_color, eye_color, 580*resolution//800,
        640*resolution//800, 20*resolution//800, False, 100, resolution)
ghost(screen, ghost_color, eye_color, 300*resolution//800,
        540*resolution//800, 25*resolution//800, True, 100, resolution)
ghost(screen, ghost_color, eye_color, 320*resolution//800,
        620*resolution//800, 15*resolution//800, True, 100, resolution)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
