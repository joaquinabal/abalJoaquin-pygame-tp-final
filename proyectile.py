from player import *
from constantes import *
from auxiliar import Auxiliar
import math
from botin import Loot

class Proyectile:
    def __init__(self,speed,x,y,direction,player_shoot=True) -> None:
        self.sprite_left = Auxiliar.getSurfaceFromSpriteSheet(r"images\caracters\adventurer\arrow_l.png",1,1,scale=2)[0]
        self.sprite_right = Auxiliar.getSurfaceFromSpriteSheet(r"images\caracters\adventurer\arrow_r.png",1,1,scale=2)[0]
        self.image = self.sprite_right
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.direction = direction
        self.tiempo_transcurrido = 0
        self.tiempo_objetivo = 500
        self.player_shoot = player_shoot

    def draw(self,screen):
        #if(DEBUG): 
            #pygame.draw.rect(screen,RED, self.rect)     
            #pygame.draw.rect(screen,GREEN, self.rect_ground_col)
        if self.direction == DIRECTION_L:
                self.image = self.sprite_left
        screen.blit(self.image,self.rect)

    def update(self,delta_ms,enemy_list,platform_list,proyectile_list, proyectile,player,loot_list,boss):
        if self.direction == DIRECTION_L:
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        self.collide(delta_ms,enemy_list,platform_list,proyectile_list, proyectile, player,loot_list,boss)

    def collide(self,delta_ms,enemy_list, platform_list,proyectile_list, proyectile, player,loot_list,boss):
        if self.player_shoot:
            for enemy in enemy_list:
                if self.rect.colliderect(enemy.rect):
                    enemy_list.remove(enemy)
                    player.score += 100
                    loot = Loot(enemy.rect.x, enemy.rect.bottom,15)
                    loot_list.append(loot) 
                    proyectile_list.remove(proyectile)
            try:
                if self.rect.colliderect(boss.rect):
                    proyectile_list.remove(proyectile)
                    boss.suffer_damage()
            except:
                pass
        else:
            if self.rect.colliderect(player.rect):
                player.lives -= 1
                proyectile_list.remove(proyectile)
                
        for platform in platform_list:
            try:
                if self.rect.colliderect(platform.rect_right_side_col) or self.rect.colliderect(platform.rect_left_side_col):
                    proyectile_list.remove(proyectile)
            except:
                pass        
                 
                 
    def timer(self):
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.tiempo_transcurrido >= self.tiempo_objetivo:
                return True
            else:
                return False
