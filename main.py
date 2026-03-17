import pygame

pygame.init()

screen = pygame.display.set_mode((640, 360))
pygame.display.set_caption('Game')

clock = pygame.time.Clock()  # ✅ create clock here

x = 300
y = 200

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += 1

    screen.fill((0, 106, 78))
    pygame.draw.circle(screen, (205, 2, 3), (x, y), 50)
    pygame.display.update()

pygame.quit()