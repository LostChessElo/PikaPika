import pygame 
import sys
from oop_game import Player, Enemy

pygame.init()

W, H = 650, 900
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("First game")
player = Player(W // 2, H // 2, W, H)
level = 1
enemy = Enemy(W, H, level)
sprite_groups = pygame.sprite.Group(player, enemy)
clock = pygame.time.Clock()


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    sprite_groups.update()
    for thing in sprite_groups:
        if isinstance(thing, Enemy):
            if thing.y > H:
                level += 1
        else:
            continue

    print(level)
    screen.fill((0,0,0))
    sprite_groups.draw(screen)
    pygame.display.flip()
    clock.tick(60)

    
pygame.quit
