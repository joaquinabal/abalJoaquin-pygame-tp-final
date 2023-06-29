from player import *
from constantes import *
from auxiliar import Auxiliar

class Enemy():
    
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,x_length,x_moving,
                 p_scale=1,interval_time_jump=100,enemy_type=0) -> None:
        '''self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/WALK/WALK_00{0}.png",0,7,scale=p_scale)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/WALK/WALK_00{0}.png",0,7,flip=True,scale=p_scale)
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/IDLE/IDLE_00{0}.png",0,7,scale=p_scale)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/enemies/ork_sword/IDLE/IDLE_00{0}.png",0,7,flip=True,scale=p_scale)
         '''
        self.enemy_type = enemy_type 
        if enemy_type == 0: #MUSHROOM
            self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/enemies/mushroom_walk_r.png",7,1,scale=DEFAULT_ENEMY_SIZE)
            self.walk_l =  Auxiliar.getSurfaceFromSpriteSheet("images/enemies/mushroom_walk_l.png",7,1,scale=DEFAULT_ENEMY_SIZE)
            self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("images/enemies/mushroom_walk_l.png",7,1,scale=DEFAULT_ENEMY_SIZE)
            self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("images/enemies/mushroom_walk_r.png",7,1,scale=DEFAULT_ENEMY_SIZE)
            
        elif enemy_type == 1: #ONEYE
            self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/enemies/oneye_walk_r.png",8,1,scale=DEFAULT_ENEMY_SIZE)
            self.walk_l =  Auxiliar.getSurfaceFromSpriteSheet("images/enemies/oneye_walk_l.png",8,1,scale=DEFAULT_ENEMY_SIZE)
            self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("images/enemies/oneye_walk_l.png",8,1,scale=DEFAULT_ENEMY_SIZE)
            self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("images/enemies/oneye_walk_r.png",8,1,scale=DEFAULT_ENEMY_SIZE)   
        self.contador = 0
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump
   
        self.x_moving = x_moving
        self.initial_y = y
        self.initial_x = x
        self.x_length = x_length
        self.movement_right = True
        self.flag_attack = True
        
        
    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self,delta_ms,plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if(not self.is_on_plataform(plataform_list)) and self.x_moving == 1:
                
                    if(self.move_y == 0):
                        self.is_fall = True
                        self.change_y(self.gravity)
            else:
                self.is_fall = False
                if self.x_moving == 1:
                    #print(")))")
                    if self.movement_right:
                        self.change_x(self.speed_walk)
                        self.animation = self.walk_r
                        if self.rect.x > self.initial_x + self.x_length:
                            self.movement_right = False
                    else:
                        self.change_x(-self.speed_walk)
                        self.animation = self.walk_l
                        if self.rect.x < self.initial_x - self.x_length:
                            self.movement_right = True
                else:
                    #print("==")
                    if self.movement_right:
                        self.change_y(self.speed_walk)
                        #self.animation = self.walk_r
                        if self.rect.y > self.initial_y + self.x_length:
                            self.movement_right = False
                        #print("pabajo")
                    else:
                        self.change_y(-self.speed_walk)
                        #self.animation = self.walk_l
                        if self.rect.y < self.initial_y - self.x_length:
                            self.movement_right = True
                        #print("parriba")
    
    def is_on_plataform(self,plataform_list):
        retorno = False
        
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    retorno = True
                    break       
        return retorno          

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
                #print(self.frame)
            else: 
                self.frame = 0

    def update(self,delta_ms,plataform_list,player,proyectile_list):
        self.do_movement(delta_ms,plataform_list)
        self.do_animation(delta_ms) 
        self.attack(player,proyectile_list)
        self.direct_animation(player)

    def draw(self,screen):
        
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

    def receive_shoot(self):
        self.lives -= 1
        
    def create_proyectile(self, proyectile_list,x,y):
        proyectile = Proyectile(5,x,y,self.direction,player_shoot=False) 
        proyectile_list.append(proyectile)
    
    def attack(self,player,proyectile_list):
        if self.x_moving == 0 and self.rect.y in range(player.rect.y-10,player.rect.y+10):
            if self.flag_attack:         
                print("asd")
                if self.direction == DIRECTION_R:
                    self.create_proyectile(proyectile_list,self.rect.right,self.rect.centery)
                else:
                    self.create_proyectile(proyectile_list,self.rect.left,self.rect.centery)    
                self.flag_attack = False
        else:
            self.flag_attack = True
        
    def direct_animation(self,player):
        if self.x_moving == 0:
            if player.rect.x < self.rect.x:
                self.direction = DIRECTION_L
                self.animation = self.walk_l
            else:
                self.direction = DIRECTION_R
                self.animation = self.walk_r
