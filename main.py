import pygame
from pygame.examples.eventlist import virtual_x

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Game')

clock = pygame.time.Clock()

x = 300
y = 200
radius = 50


vx = 3

running = True
while running:
    clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += vx
    if x + radius >= 1280:
        vx = -vx

    if x - radius <= 0:
        vx = -vx

    screen.fill((0, 106, 78))
    pygame.draw.circle(screen, (205, 2, 3), (x, y), 50)
    pygame.display.update()

pygame.quit()