import pygame

pygame.init()  # Initialize Pygame first

screen = pygame.display.set_mode((640, 360))
pygame.display.set_caption('Game')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 106, 78))  # Fill the screen with bangladesh green
    pygame.draw.circle(screen, (200, 0, 0), (300, 200), 50)  # Draw the circle
    pygame.display.update()  # Update the display

pygame.quit()