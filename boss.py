from player import *
from constantes import *
from auxiliar import Auxiliar
from enemigo import Enemy


class Boss():
    
    def __init__(self,x,y,frame_rate_ms,move_rate_ms) -> None:
        self.walk =  Auxiliar.getSurfaceFromSpriteSheet("images/enemies/boss/boss_walk.png",6,1,scale=4)
        self.stay =  Auxiliar.getSurfaceFromSpriteSheet("images/enemies/boss/boss_stay.png",6,1,scale=4)
        self.attack = Auxiliar.getSurfaceFromSpriteSheet("images/enemies/boss/boss_attack.png",17,1,scale=4)
        self.dmg = Auxiliar.getSurfaceFromSpriteSheet("images/enemies/boss/boss_dmg.png",4,1,scale=4)
        self.spawn = Auxiliar.getSurfaceFromSpriteSheet("images/enemies/boss/boss_spawn.png",11,1,scale=4) 
        self.death = Auxiliar.getSurfaceFromSpriteSheet("images/enemies/boss/boss_death.png",5,1,scale=4)  
        self.stay_death = Auxiliar.getSurfaceFromSpriteSheet("images/enemies/boss/boss_stay_death.png",2,1,scale=4)  
        self.frame = 0
        self.lives = 5
        self.score = 0
        
        self.flag_spawn = True
        self.flag_still_alive = True
        
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
    
    def update(self,delta_ms,player,enemies_list):
        self.do_animation(delta_ms) 
        self.animate_spawn()
        self.do_attack(player,enemies_list)
        self.stop_suffering_dmg()
        self.animate_death()
        
    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,255,0),rect=self.rect) 
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        
    def receive_shoot(self):
        self.lives -= 1
        
    def do_attack(self,player,enemies_list):
        if self.calculate_delta_time(7000) and self.animation == self.stay:
            print("entro al ataque")
            self.animation = self.attack

            self.tiempo_inicial = pygame.time.get_ticks()
        if self.animation == self.attack and self.frame == len(self.animation) - 1:
            if player.rect.y > 575:
                player.lives -= 1
                print(player.lives)
            self.generate_enemy(enemies_list,player)
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
        self.frame = 0
        self.animation = self.dmg
        self.lives -= 1
        print(self.lives)
        
    def stop_suffering_dmg(self):
        if self.animation == self.dmg and self.frame == len(self.animation) - 1:
            print("entra a stay")
            self.frame = 0
            self.animate_stay()
            
    def animate_death(self):
        if self.flag_still_alive:
            if self.lives < 1:
                self.animation = self.death
                self.flag_still_alive = False
        if self.animation == self.death and self.frame == len(self.animation) - 1 and not self.flag_still_alive:
            print("entra al death")
            print(self.frame)
            self.frame = 0
            self.animation = self.stay_death
            
    def generate_enemy(self,enemies_list,player):
        enemies_list.append(Enemy(x=player.rect.x,y=0,speed_walk=4,speed_run=8,gravity=20,jump_power=10,frame_rate_ms=80,move_rate_ms=80,jump_height=100,x_length=50,x_moving=1,p_scale=1,interval_time_jump=100,enemy_type=0))
        
                
        
    
        
        