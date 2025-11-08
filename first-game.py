import pygame 
import os
from oop_game import Player, Food, Enemy
import time

pygame.init()
pygame.font.init()

W, H = 900, 650
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("First game")
backgroung_img = pygame.image.load(os.path.join('images', 'background.jpg')).convert()
backgroung_img = pygame.transform.scale(backgroung_img, (W, H))
player = Player(W // 2, H // 2, W, H)
score = 0
collision = False
food = Food(W, H, collision)
enemy = Enemy(W, H, collision)
sprite_groups = pygame.sprite.Group(player)
food_group = pygame.sprite.Group(food) 
enemies = pygame.sprite.Group(enemy)     
clock = pygame.time.Clock()
font = pygame.font.SysFont("comic sans", 36)
died = False

pygame.time.delay(25)
run = True
while run:
    # pygame.time.delay(550)

    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    collision = False
    sprite_groups.update()
    food_group.update()
    enemies.update()


    screen.blit(backgroung_img, (0,0))
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
    elif player not in sprite_groups:
        lost = font.render(f"YOU DIED!! Final score {score}", True, (255,0,0))
        lost_rect = lost.get_rect(center = (W // 2, H // 2))
        screen.blit(lost, lost_rect)
        died = True
        run = False




    pygame.display.flip()
    # clock.tick(120)

pygame.time.delay(2000)   
pygame.quit
