import pygame 
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, screen_width, screen_height):
        super().__init__()
        self.x, self.y = x, y
        self.w, self.h = 100, 100 
        self.screen_w, self.screen_h = screen_width, screen_height
        self.image = pygame.image.load("player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.w,self.h))
        self.rect = self.image.get_rect(center = (x, y))
        self.speed = 10


        
    def key_logic(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > self.speed:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < self.screen_w - self.w - self.speed:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.y > self.speed:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < self.screen_h - self.h - self.speed:
            self.rect.y += self.speed


    def update(self):
        self.key_logic()

class Enemy(pygame.sprite.Sprite):
    MAX_FALL_RATE = 25

    def __init__(self, screen_width: int, screen_height:int, level: int):
        super().__init__()
        self.screen_w, self.screen_h = screen_width, screen_height
        self.x, self.y = random.randint(0, screen_width), 0
        self.w, self.h = 25, 15
        self.image = pygame.Surface((self.w, self.h))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.fall_rate = 10
        self.level = 1

    def fall(self):
        if self.rect.y < self.screen_h:
            self.rect.y += self.fall_rate
        else:
            self.rect.y = 0
            self.rect.x = random.randint(80, self.screen_w - 80)
    
            
            

    def update(self):
        self.fall()
      