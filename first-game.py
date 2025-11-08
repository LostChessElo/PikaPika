import pygame 
import os
from Game_objects import Player, Food, Enemy
import time

#initialize pygame
pygame.init()
pygame.font.init()

# create window 
W, H = 900, 650
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("First game")
backgroung_img = pygame.image.load(os.path.join('images', 'background.jpg')).convert()
backgroung_img = pygame.transform.scale(backgroung_img, (W, H))

# clock for fps and font init
clock = pygame.time.Clock()
font = pygame.font.SysFont("comic sans", 36)


    
def objects():

    player = Player(W // 2, H // 2, W, H)
    food = Food(W, H)
    enemy = Enemy(W, H)
    sprite_groups = pygame.sprite.Group(player)
    food_group = pygame.sprite.Group(food) 
    enemies = pygame.sprite.Group(enemy)     

    return player, food, enemy, sprite_groups, food_group, enemies


def game_loop(player: object, food: object , enemy: object, sprite_groups: object , food_group: object , enemies: object):

    pygame.time.delay(200)
    score = 0
    run, died = True, False

    # main game loop
    while run:

        clock.tick(120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

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

            new_food = Food(W, H)
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
 
    pygame.time.delay(2000)   
    pygame.quit


def main():
    player, food, enemy, sprite_groups, food_group, enemies = objects()
    game_loop(player, food, enemy, sprite_groups, food_group, enemies)


if __name__ == '__main__':
    main()