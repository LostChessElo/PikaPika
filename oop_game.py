import pygame 
import random
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, screen_width, screen_height):
        super().__init__()
        self.x, self.y = x, y
        self.w, self.h = 75, 75 
        self.screen_w, self.screen_h = screen_width, screen_height
        self.image = pygame.image.load(os.path.join("images", "player.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.w,self.h))
        self.rect = self.image.get_rect(center = (x, y))
        self.speed = 10


        
    def key_logic(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > self.speed:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.x < self.screen_w - self.w - self.speed:
            self.rect.x += self.speed
        if keys[pygame.K_w] and self.rect.y > self.speed:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < self.screen_h - self.h - self.speed:
            self.rect.y += self.speed


    def update(self):
        self.key_logic()

class Food(pygame.sprite.Sprite):
    MAX_FALL_RATE = 35
    fall_rate = 2.5

    def __init__(self, screen_width: int, screen_height:int, collision_status: bool):
        super().__init__()
        self.screen_w, self.screen_h = screen_width, screen_height
        self.x, self.y = random.uniform(80.0, float(screen_width - 80)), 0
        self.w, self.h = 50, 50
        self.image = pygame.image.load(os.path.join('images', "red_berry.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.fall_rate = Food.fall_rate
        # self.level = 1

    def fall(self):
        if self.rect.y < self.screen_h:
            self.rect.y += self.fall_rate
        else:
            self.rect.y = 0
            self.rect.x = random.uniform(80.0, float(self.screen_w - 80))            # Food.fall_rate = min(Food.fall_rate * 1.5, Food.MAX_FALL_RATE)
            Food.fall_rate = min (Food.fall_rate * 1.1, Food.MAX_FALL_RATE)

    
            
    def update(self):
        self.fall()


class Enemy(pygame.sprite.Sprite):
    fall_rate = 2
    MAX_FALL_RATE = 35

    def __init__(self, screen_width, screen_height, collision_status):
        super().__init__()
        self.screen_w, self.screen_h = screen_width, screen_height
        self.x, self.y = random.randint(80, screen_width - 80), 0
        self.w, self.h = 60, 67
        self.image = pygame.image.load(os.path.join('images', "black_berry.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.rect = self.image.get_rect(center = (self.x, self.y))
        # self.fall_rate = 2

    def fall(self):
        if self.rect.y < self.screen_h:
            self.rect.y += self.fall_rate

        else:
            self.rect.y = 0
            self.rect.x = random.randint(self.screen_w // 2, self.screen_w - 80)
            Enemy.fall_rate = min(Enemy.fall_rate * 1.1, Enemy.MAX_FALL_RATE)
    
                
    def update(self):
        self.fall()