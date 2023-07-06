import pygame
from constantes import *
from auxiliar import Auxiliar


class Consumable:
    def __init__(self,x,y) -> None:
        self.sprite = Auxiliar.getSurfaceFromSpriteSheet(r"images\consumable\bad_heart.png",1,1,scale=2)[0]
        self.image = self.sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def draw(self,screen):
        if(DEBUG): 
            pygame.draw.rect(screen,C_RED, self.rect)     
            #pygame.draw.rect(screen,GREEN, self.rect_ground_col)
        screen.blit(self.image,self.rect)

    def collide(self,player, consumable_list, consumable):
        if self.rect.colliderect(player.rect):
            player.discount_live()
            consumable_list.remove(consumable)  
            

    def update(self, player, consumable_list, consumable):
        self.collide(player, consumable_list, consumable)
    

