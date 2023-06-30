from player import *
from constantes import *
from auxiliar import Auxiliar
import time


class Boss():
    
    def __init__(self,x,y,frame_rate_ms,move_rate_ms) -> None:
        self.walk =  Auxiliar.getSurfaceFromSpriteSheet("images/enemies/boss/boss_walk.png",6,1,scale=4)
        self.stay =  Auxiliar.getSurfaceFromSpriteSheet("images/enemies/boss/boss_stay.png",6,1,scale=4)
        self.attack = Auxiliar.getSurfaceFromSpriteSheet("images/enemies/boss/boss_attack.png",10,1,scale=4)
        self.dmg = Auxiliar.getSurfaceFromSpriteSheet("images/enemies/boss/boss_dmg.png",4,1,scale=4)
        self.spawn = Auxiliar.getSurfaceFromSpriteSheet("images/enemies/boss/boss_spawn.png",11,1,scale=4) 
        self.death = Auxiliar.getSurfaceFromSpriteSheet("images/enemies/boss/boss_death.png",5,1,scale=4)  
        
        self.frame = 0
        self.lives = 5
        self.score = 0
        
        self.flag_spawn = True
        
        self.animation = self.spawn
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y  
        
        self.tiempo_inicial = pygame.time.get_ticks()

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms  
        
    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
    
    def update(self,delta_ms,player):
        self.do_animation(delta_ms) 
        self.animate_spawn()
        self.do_attack(player)
        
    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,255,0),rect=self.rect) 
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        
    def receive_shoot(self):
        self.lives -= 1
        
    def do_attack(self,player):
        if self.calculate_delta_time(7000) and self.animation == self.stay:
            print("entro al ataque")
            self.animation = self.attack
            if player.rect.y > 575:
                player.lives -= 1
                print(player.lives)
            self.tiempo_inicial = pygame.time.get_ticks()
        if self.animation == self.attack and self.frame == len(self.animation) - 1:
            print("entra a stay")
            self.frame = 0
            self.animate_stay()

    def calculate_delta_time(self,tiempo_objetivo):
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = tiempo_actual - self.tiempo_inicial
        if tiempo_transcurrido >= tiempo_objetivo:
            return True
        else:
            return False
        
    def animate_spawn(self):
        if self.flag_spawn:
            self.animation = self.spawn
        if self.animation == self.spawn and self.frame == len(self.animation) - 1:
            self.frame = 0
            self.animate_stay()
            self.flag_spawn = False
          
    def animate_stay(self):
        self.animation = self.stay
        
    def suffer_damage(self):
        self.animation = self.dmg
        if self.animation == self.dmg and self.frame == len(self.animation) - 1:
            print("entra a stay")
            self.frame = 0
            self.animate_stay()
    
        
        