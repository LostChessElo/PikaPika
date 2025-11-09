import pygame 
import random
import os

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, screen_width, screen_height, floor):
        super().__init__()
        self.x, self.y = x, y
        self.w, self.h = 95, 105 
        self.screen_w, self.screen_h = screen_width, screen_height
        self.image = pygame.image.load(os.path.join("images", "player.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.w,self.h))
        self.rect = self.image.get_rect(center = (x, y))
        self.speed = 7.25
        self.v = 0 # pygame takes down as positive
        self.jump_strength = - 17 
        self.jumped = False
        self.gravity = 9.8 / 13
        self.floor = floor
        self.rect.bottom = self.floor.rect.top

        
    def key_logic(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > self.speed:
            self.rect.x -= self.speed

        if keys[pygame.K_d] and self.rect.x < self.screen_w - self.w - self.speed:
            self.rect.x += self.speed
 
        on_ground = self.rect.bottom >= self.floor.rect.top
        if keys[pygame.K_SPACE] and on_ground:
            self.jumped = True
            self.v = self.jump_strength

        if self.jumped:
            self.rect.y += self.v
            self.v += self.gravity

            if self.rect.bottom >= self.floor.rect.top:
                self.rect.bottom = self.floor.rect.top
                self.jumped = False
                self.v = 0 


    def update(self):
        self.key_logic()

class Food(pygame.sprite.Sprite):

    MAX_FALL_RATE = 35
    fall_rate = 2.5

    def __init__(self, screen_width: int, screen_height:int, floor):
        super().__init__()
        self.screen_w, self.screen_h = screen_width, screen_height
        self.x, self.y = random.uniform(80.0, float(screen_width - 80)), 0
        self.w, self.h = 50, 50
        self.image = pygame.image.load(os.path.join('images', "red_berry.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.fall_rate = Food.fall_rate
        self.floor = floor
        
    def fall(self):
        if self.rect.bottom < self.floor.rect.top:
            self.rect.y += self.fall_rate
        else:
            self.rect.y = 0
            self.rect.x = random.uniform(80.0, float(self.screen_w - 80))         
            Food.fall_rate = min(Food.fall_rate * 1.1, Food.MAX_FALL_RATE)
     
    def update(self):
        self.fall()


class Enemy(pygame.sprite.Sprite):
    
    fall_rate = 2
    MAX_FALL_RATE = 15

    def __init__(self, screen_width, screen_height, floor):
        super().__init__()
        self.screen_w, self.screen_h = screen_width, screen_height
        self.x, self.y = random.randint(80, screen_width - 80), 0
        self.w, self.h = 60, 67
        self.image = pygame.image.load(os.path.join('images', "black_berry.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.floor = floor

    def fall(self):
        if self.rect.bottom < self.floor.rect.top:
            self.rect.y += self.fall_rate

        else:
            self.rect.y = 0
            self.rect.x =  random.uniform(80.0, float(self.screen_w - 80))  
            if Enemy.fall_rate <= Enemy.MAX_FALL_RATE:
                Enemy.fall_rate = min(Enemy.fall_rate * 1.1, Enemy.MAX_FALL_RATE)
    
    def update(self):
        self.fall()

class Menu:
    pass
    # imporrt buttons  and impliment them into a pause menu
    # eg:
    # ------ Puase -------
    # Resume
    # Options
    # quit 

class Floor:
    def __init__(self, screen_w: int, screen_h: int):
        self.x, self.y = 0, screen_h - 50
        self.w, self.h = screen_w, 50
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

