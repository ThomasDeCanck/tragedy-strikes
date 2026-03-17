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

acceleration = 0.5
friction = 0.98  # closer to 1 = less friction

running = True
while running:
    dt = clock.tick(120) / 1000  # delta time (seconds)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ✅ Continuous key input (hold keys)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        vx += acceleration
    if keys[pygame.K_LEFT]:
        vx -= acceleration
    if keys[pygame.K_UP]:
        vy -= acceleration
    if keys[pygame.K_DOWN]:
        vy += acceleration

    # ✅ Apply friction
    vx *= friction
    vy *= friction

    # Move
    x += vx
    y += vy

    # Bounce
    if x + radius >= 1280 or x - radius <= 0:
        vx = -vx
    if y + radius >= 720 or y - radius <= 0:
        vy = -vy

    screen.fill((0, 106, 78))
    pygame.draw.circle(screen, (205, 2, 3), (int(x), int(y)), radius)
    pygame.display.update()

pygame.quit()