import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from player import Player
from enemigo import Enemy
from plataforma import Plataform
from background import Background
from bullet import Bullet

class FormGameLevel1(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,config_json):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.levels = config_json
        
        # --- GUI WIDGET --- 
        self.boton1 = Button(master=self,x=0,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="BACK",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=200,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="PAUSE",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton_shoot = Button(master=self,x=400,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_shoot,on_click_param="form_menu_B",text="SHOOT",font="Verdana",font_size=30,font_color=C_WHITE)
       
        self.pb_lives = ProgressBar(master=self,x=500,y=50,w=240,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Bars/Bar_Background01.png",image_progress="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",value = 5, value_max=5)
        self.widget_list = [self.boton1,self.boton2,self.pb_lives,self.boton_shoot]

        # --- GAME ELEMNTS --- 
        self.static_background = Background(x=0,y=0,width=w,height=h,path="images/locations/forest/forest.png")

        self.player_1 = self.generate_player()

        self.enemies_list = []
        self.generate_enemies()
        
        self.platform_list = []
        self.generate_platform()

        self.proyectile_list = []
        self.bullet_list = []
        self.proyectile_enemy_list = []
        self.loot_list = []


    def generate_player(self):
        data_player = self.levels[0]["player"]
        player = Player(x=data_player["x"],y=data_player["y"],speed_walk=data_player["speed_walk"],speed_run=data_player["speed_run"],
                        gravity=data_player["gravity"],jump_power=data_player["jump_power"],frame_rate_ms=data_player["frame_rate_ms"],
                        move_rate_ms=data_player["move_rate_ms"],jump_height=data_player["jump_height"],
                        p_scale=data_player["p_scale"],interval_time_jump=data_player["interval_time_jump"])
        return player

    def generate_enemies(self):
        data_enemies = self.levels[0]["enemies"]
        for enemy in data_enemies:
            self.enemies_list.append(Enemy(x=enemy["x"],y=enemy["y"],speed_walk=enemy["speed_walk"],speed_run=enemy["speed_run"],
                            gravity=enemy["gravity"],jump_power=enemy["jump_power"],frame_rate_ms=enemy["frame_rate_ms"],
                            move_rate_ms=enemy["move_rate_ms"],jump_height=enemy["jump_height"],
                            p_scale=enemy["p_scale"],interval_time_jump=enemy["interval_time_jump"],
                            enemy_type=enemy["enemy_type"],x_length=enemy["x_length"],x_moving=enemy["x_moving"]))
        
    
    def generate_platform(self):
        data_platforms = self.levels[0]["platforms"]
        for platform in data_platforms:
            self.platform_list.append(Plataform(x=platform["x"],y=platform["y"],height=platform["height"],width=platform["width"],
                            image=platform["image"]))



    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def on_click_shoot(self, parametro):
        for enemy_element in self.enemies_list:
            self.bullet_list.append(Bullet(enemy_element,enemy_element.rect.centerx,enemy_element.rect.centery,self.Enemy_1.rect.centerx,self.Enemy_1.rect.centery,20,path="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",frame_rate_ms=100,move_rate_ms=20,width=5,height=5))    

    def update(self, lista_eventos,keys,delta_ms,event):
        for aux_widget in self.widget_list:
            aux_widget.update(lista_eventos)

        for bullet_element in self.bullet_list:
            bullet_element.update(delta_ms,self.enemies_list,self.platform_list,self.bullet_list,bullet_element,self.player_1,self.loot_list)
            
        for proyectile_enemy_element in self.proyectile_enemy_list:
            proyectile_enemy_element.update(delta_ms,self.enemies_list,self.platform_list,self.proyectile_enemy_list,proyectile_enemy_element,self.player_1,self.loot_list)

        for enemy_element in self.enemies_list:
            enemy_element.update(delta_ms,self.platform_list,self.player_1,self.proyectile_enemy_list)
            
        for loot_element in self.loot_list:
            loot_element.update(self.player_1, self.loot_list, loot_element,self.platform_list)
            


        self.player_1.events(delta_ms,keys,event,self.bullet_list)
        self.player_1.update(delta_ms,self.platform_list)

        self.pb_lives.value = self.player_1.lives 


    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)

        for aux_widget in self.widget_list:    
            aux_widget.draw()

        for plataforma in self.platform_list:
            plataforma.draw(self.surface)

        for enemy_element in self.enemies_list:
            enemy_element.draw(self.surface)
        
        self.player_1.draw(self.surface)

        for bullet_element in self.bullet_list:
            bullet_element.draw(self.surface)
            
        for bullet_element in self.proyectile_enemy_list:
            bullet_element.draw(self.surface)
            
        for loot_element in self.loot_list:
            loot_element.draw(self.surface)