import pygame
from constantes import *
from auxiliar import Auxiliar
from proyectile import Proyectile
import time
class Player:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100) -> None:
        '''
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/walk.png",15,1,scale=p_scale)[:12]
        '''

        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_walk_r.png",6,1,scale=3)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_walk_l.png",6,1,scale=3)  
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_stay_r.png",3,1,scale=3)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_stay_l.png",3,1,scale=3)  
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_jump_r.png",15,1,scale=3)  
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_jump_l.png",15,1,scale=3)  
        self.atk_stance_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_atk_stance_r.png",5,1,scale=3)  
        self.atk_stance_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_atk_stance_l.png",5,1,scale=3) 
        self.charge_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_charge_r.png",1,1,scale=3)  
        self.charge_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_charge_l.png",1,1,scale=3)   
        self.atk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_atk_r.png",2,1,scale=3)  
        self.atk_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_atk_l.png",2,1,scale=3)    
        self.hurt_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_hurt_r.png",3,1,scale=3)  
        self.hurt_l = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/adventurer/adv_hurt_l.png",3,1,scale=3)

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
        
        self.tiempo_objetivo = 500
        self.atk_stance_flag = False
        self.tiempo_transcurrido = 0
        
        self.previous_time = time.time()
                
        self.font_score = pygame.font.Font(None, 32)

    def walk(self,direction):
        if(self.is_jump == False and self.is_fall == False):
            if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
                self.frame = 0
                self.direction = direction
                if(direction == DIRECTION_R):
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                else:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l

    def shoot(self,on_off = True):
        self.is_shoot = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):

            if(self.animation != self.shoot_r and self.animation != self.shoot_l):
                self.frame = 0
                self.is_shoot = True
                if(self.direction == DIRECTION_R):
                    self.animation = self.shoot_r
                else:
                    self.animation = self.shoot_l       

    def receive_shoot(self):
        self.lives -= 1

    def knife(self,on_off = True):
        self.is_knife = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.knife_r and self.animation != self.knife_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.knife_r
                else:
                    self.animation = self.knife_l      

    def jump(self,platform_list,on_off = True):
        if(on_off and self.is_jump == False and self.is_fall == False):
            self.y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R):
                self.move_x = int(self.move_x / 1.5)
                self.move_y = -self.jump_power
                self.animation = self.jump_r
            else:
                self.move_x = int(self.move_x / 1.5)
                self.move_y = -self.jump_power
                self.animation = self.jump_l
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()

    def stay(self):
        if(self.is_knife or self.is_shoot):
            return

        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

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

            if(abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0
          
            self.change_x(self.move_x)
            self.change_y(self.move_y)

            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                if (self.is_jump): 
                    self.jump(plataform_list,False)
                self.is_fall = False            
            if self.collide_platform_sides(plataform_list):
                self.move_x = 0
            if  self.collide_platform_bottom(plataform_list):
                print("colision bottom")
                self.move_y = 0
                
            

    def show_score(self):
        score_count = self.font_score.render('SCORE: {0}'.format(self.score), True, C_WHITE, None)
        return score_count

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
 
    def update(self,delta_ms,plataform_list,enemy_list):
        self.do_movement(delta_ms,plataform_list)
        self.do_animation(delta_ms)
        self.colllide_enemy(enemy_list)
        
    
    def draw(self,screen):
        
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        
        try:
            self.imagen = self.animation[self.frame]
        except IndexError:
            print("IndexError")
        screen.blit(self.imagen, self.rect)
        screen.blit(self.show_score(), SCORE_POSITION)
        

    def events(self,delta_ms,keys,event,proyectile_list,platform_list):
        self.tiempo_transcurrido += delta_ms


        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_L)

        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_R)

        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()
        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()  

        if(keys[pygame.K_SPACE]):
            if((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                self.jump(platform_list,True)
                self.tiempo_last_jump = self.tiempo_transcurrido

        if keys[pygame.K_q]:
            self.atk_stance()
            global unpressed_flag
            unpressed_flag = True
            if self.timer(1000):
                unpressed_flag = False
                self.charge_attack() 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:   
                #print("q")
               # print(self.atk_stance_flag)       
                if not unpressed_flag:   
                    self.attack()
                    if self.direction == DIRECTION_R:
                        self.create_proyectile(proyectile_list,self.rect.right,self.rect.centery)
                    else:
                        self.create_proyectile(proyectile_list,self.rect.left,self.rect.centery)    
                    unpressed_flag = True
                self.atk_stance_flag = False
                    
    def create_proyectile(self, proyectile_list,x,y):
        proyectile = Proyectile(5,x,y,self.direction) 
        proyectile_list.append(proyectile)
                
    def timer(self, tiempo_obj):
            if self.atk_stance_flag == False:
                self.tiempo_trans = pygame.time.get_ticks()
                self.atk_stance_flag = True
            print(self.atk_stance_flag)
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.tiempo_trans >= tiempo_obj:
                return True
            else:
                return False
            

    def calculate_delta_time(self,ms_threshold, time):
        current_time = time.time()
        delta_time = current_time - previous_time
        previous_time = current_time

        if delta_time * time >= ms_threshold:
            return True
        else:
            return False  
   
    def charge_attack(self):
        if self.direction == DIRECTION_R:
            self.animation = self.charge_r
        else:
            self.animation = self.charge_l        

    def attack(self):
        if self.direction == DIRECTION_R:
            self.animation = self.atk_r
        else:
            self.animation = self.atk_l
            
    def atk_stance(self):
        #print("atk stance")
        if self.direction == DIRECTION_R:
            self.animation = self.atk_stance_r
        else:
            self.animation = self.atk_stance_l
            
    def colllide_enemy(self, enemy_list):
        collision_detected = False  # Bandera para indicar si se detectó una colisión con algún enemigo   
        for enemy in enemy_list:
            if self.rect.colliderect(enemy.rect):
                collision_detected = True
                break  # Si hay una colisión, no es necesario verificar los otros enemigos
        if collision_detected:
            if not self.colliding_enemy_flag:  # Verifica si ya estás colisionando con un enemigo
                self.be_hurted()
                self.lives -= 1
                print(self.lives)
                self.colliding_enemy_flag = True  # Establece la bandera para indicar que estás colisionando con un enemigo
        else:
            self.colliding_enemy_flag = False
            
    def collide_platform_sides(self, platform_list): 
        retorno = False
        for platform in platform_list:
            try:
                if self.rect.colliderect(platform.rect_right_side_col) or self.rect.colliderect(platform.rect_left_side_col):
                    retorno = True
                    break
            except:
                pass
        return retorno        
    
    def collide_platform_bottom(self, platform_list): 
        retorno = False
        for platform in platform_list:
            try:
                if self.rect.colliderect(platform.rect_bottom_col):
                    retorno = True
                    break
            except:
                pass        
        return retorno 
    
    
    def be_hurted(self):
        pass
    '''CHEQUEAR 
    if self.direction == DIRECTION_R:
        self.animation = self.hurt_r
    else:
        self.animation = self.hurt_l'''