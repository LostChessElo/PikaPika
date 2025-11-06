import pygame 
import sys
from oop_game import Player, Food, Enemy

pygame.init()
pygame.font.init()

W, H = 650, 900
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("First game")
player = Player(W // 2, H // 2, W, H)
score = 0
collision = False
food = Food(W, H, collision)
enemy = Enemy(W, H, collision)
sprite_groups = pygame.sprite.Group(player)
food_group = pygame.sprite.Group(food) 
enemies = pygame.sprite.Group(enemy)     
clock = pygame.time.Clock()
font = pygame.font.SysFont("Ariel", 36)

run = True
while run:
    # pygame.time.delay(550)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    collision = False
    sprite_groups.update()
    food_group.update()
    enemies.update()


    screen.fill((0,0,0))
    sprite_groups.draw(screen)
    food_group.draw(screen)
    enemies.draw(screen)

    screen_txt = font.render(f"Score: {score}",True, (255,255,255))
    screen.blit(screen_txt, (10,10))
    food_collision = pygame.sprite.spritecollide(player, food_group, True)
    enemy_collision = pygame.sprite.spritecollide(enemy, sprite_groups, True)
    
    if food_collision:
        collision = True

        new_food = Food(W, H, collision)
        new_food.fall_rate = food.fall_rate 
        food_group.add(new_food)
        score += 1
    elif enemy_collision:
        lost = font.render(f"YOU DIED!! Final score {score}", True, (255,255,255))
        lost_rect = lost.get_rect(center = (W // 2, H // 2))
        screen.blit(lost, lost_rect)
        # pygame.display.update()
        # pygame.time.delay(2000)
        run = False




    pygame.display.flip()
    clock.tick(120)

pygame.time.delay(2000)   
pygame.quit
