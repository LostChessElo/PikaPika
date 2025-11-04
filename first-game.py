import pygame 
import sys

# initialize pygame 
pygame.init()

W, H = 500, 500
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("First game")
box_x, box_y = 20, 20 
velocity = 10

running = True
while running:
    pygame.time.delay(100)
    clock = pygame.time.Clock()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and box_x > velocity:
        box_x -= velocity
    if keys[pygame.K_RIGHT] and box_x < W - 20 - velocity:
        box_x += velocity
    if keys[pygame.K_UP] and box_y > velocity:
        box_y -= velocity
    if keys[pygame.K_DOWN] and box_y < H - 20 - velocity:
        box_y += velocity

    screen.fill((0,0,0))
    box = pygame.draw.rect(screen, (255,0,0), (box_x, box_y, 20, 20))
    pygame.display.update()
    clock.tick(120)
pygame.quit
