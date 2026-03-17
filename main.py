import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Game')

clock = pygame.time.Clock()

x = 300
y = 200
radius = 50

vx = 0
vy = 0

running = True
while running:
    clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ✅ Key controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                vx += 1
            if event.key == pygame.K_LEFT:
                vx -= 1
            if event.key == pygame.K_UP:
                vy -= 1
            if event.key == pygame.K_DOWN:
                vy += 1
            if event.key == pygame.K_SPACE:
                vx = 3
                vy = 2

    x += vx
    y += vy

    if x + radius >= 1280 or x - radius <= 0:
        vx = -vx

    if y + radius >= 720 or y - radius <= 0:
        vy = -vy

    screen.fill((0, 106, 78))
    pygame.draw.circle(screen, (205, 2, 3), (x, y), radius)
    pygame.display.update()

pygame.quit()