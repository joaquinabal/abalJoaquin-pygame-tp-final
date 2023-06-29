import pygame
from constantes import *
from auxiliar import Auxiliar


class Loot:
    def __init__(self,x,y,y_length) -> None:
        self.sprite = Auxiliar.getSurfaceFromSpriteSheet("images/bullet01_l.png",1,1)[0]
        self.image = self.sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.y_length = y_length
        self.initial_y = y
        self.speed = 1
        self.movement_up = True
       # self.gravity = gravity

    def draw(self,screen):
        if(DEBUG): 
            pygame.draw.rect(screen,C_RED, self.rect)     
            #pygame.draw.rect(screen,GREEN, self.rect_ground_col)
        screen.blit(self.image,self.rect)

    def collide(self,player, loot_list, loot):
        if self.rect.colliderect(player.rect):
            player.score += 300
            loot_list.remove(loot)  

    def update(self, player, loot_list, loot,platform_list):
        self.move(platform_list)
        self.collide(player, loot_list, loot)
    
    def increment_y(self,delta_y):
        self.rect.y += delta_y
        
    def move(self,platform_list):
        for platform in platform_list:
            if self.rect.y < GROUND_LEVEL and not self.rect.colliderect(platform.ground_collition_rect):
                self.increment_y(self.speed)
        if self.movement_up:
            self.increment_y(self.speed)
            if self.rect.y > self.initial_y + self.y_length:
                self.movement_up = False
        else:
            self.increment_y(-self.speed)
            if self.rect.y < self.initial_y - self.y_length:
                self.movement_up = True