import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_progressbar import ProgressBar
from player import Player
from enemigo import Enemy
from plataforma import Plataform
from background import Background
from gui_label import Label
from boss import Boss
from auxiliar import Auxiliar
from consumable import Consumable

class FormGameLevel3(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,config_json,lvl2):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.levels = config_json
        self.player_1 = self.generate_player()
        self.music_path = r"music/boss_music.wav" 
        self.music_menu = r"music/title_theme.wav"    
        self.tiempo_inicial = pygame.time.get_ticks()
        self.music = True
        self.cronometro = 120
        self.lvl_anterior = lvl2
        self.score_total = 0
        self.pausado = False
        self.font = pygame.font.SysFont("Verdana",50)


        
        # --- GUI WIDGET --- 
        
        self.text_lvl = Label(master=self,x=75,y=30,w=200,h=50,color_background=None,color_border=None,image_background=None,
                                  text="LEVEL 3",font='Arial',font_size=30,font_color=C_WHITE)
        
        self.text_required_score = Label(master=self,x=90,y=75,w=300,h=50,color_background=None,color_border=None,image_background=None,
                                  text=f'DERROTA AL REY ESQUELETO',font='Arial',font_size=20,font_color=C_WHITE)

        
        self.button_menu = Button(master=self,x=1275,y=725,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Data_Border/Buttons/Button_M_06.png",on_click=self.on_click_boton1,on_click_param="form_menu_principal",text="MENU",font="Verdana",font_size=30,font_color=C_WHITE)
         
        self.text_score = Label(master=self,x=1200,y=30,w=200,h=50,color_background=None,color_border=None,image_background=None,
                                  text=f'SCORE: {str(self.player_1.score)}',font='Arial',font_size=30,font_color=C_WHITE)
        
        self.text_time = Label(master=self,x=1200,y=80,w=200,h=50,color_background=None,color_border=None,image_background=None,
                                  text=f'TIME: {str(self.cronometro)}',font='Arial',font_size=30,font_color=C_WHITE)
        
        self.pb_lives = ProgressBar(master=self,x=1000,y=50,w=150,h=30,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Data_Border/Bars/Bar_Background01.png",image_progress="images/gui/set_gui_01/Data_Border/Bars/Bar_Segment05.png",value = self.player_1.lives, value_max=5)
        
        self.widget_list = [self.text_lvl,self.text_required_score,self.button_menu,self.text_score,self.text_time,self.pb_lives]

        # --- GAME ELEMNTS --- 
        self.static_background = Background(x=0,y=0,width=w,height=h,path="images/locations/forest/forest.png")

        self.boss = self.generate_boss()

        self.enemies_list = []
        self.generate_enemies()
        
        self.platform_list = []
        self.generate_platform()

        self.consumable_list = []
        self.generate_consumables()

        self.proyectile_list = []
        self.proyectile_enemy_list = []
        self.loot_list = []


    def generate_player(self):
        data_player = self.levels[2]["player"]
        player = Player(x=data_player["x"],y=data_player["y"],speed_walk=data_player["speed_walk"],speed_run=data_player["speed_run"],
                        gravity=data_player["gravity"],jump_power=data_player["jump_power"],frame_rate_ms=data_player["frame_rate_ms"],
                        move_rate_ms=data_player["move_rate_ms"],jump_height=data_player["jump_height"],
                        p_scale=data_player["p_scale"],interval_time_jump=data_player["interval_time_jump"])
        return player

    def generate_enemies(self):
        data_enemies = self.levels[2]["enemies"]
        for enemy in data_enemies:
            self.enemies_list.append(Enemy(x=enemy["x"],y=enemy["y"],speed_walk=enemy["speed_walk"],
                            gravity=enemy["gravity"],frame_rate_ms=enemy["frame_rate_ms"],
                            move_rate_ms=enemy["move_rate_ms"],
                            p_scale=enemy["p_scale"],interval_time_jump=enemy["interval_time_jump"],
                            enemy_type=enemy["enemy_type"],x_length=enemy["x_length"],x_moving=enemy["x_moving"]))
        
    
    def generate_platform(self):
        data_platforms = self.levels[2]["platforms"]
        for platform in data_platforms:
            self.platform_list.append(Plataform(x=platform["x"],y=platform["y"],height=platform["height"],width=platform["width"],
                            image=platform["image"],column=platform["column"]))
            
    def generate_boss(self):
        data_boss = self.levels[2]["boss"]
        boss = Boss(x=data_boss["x"], y=data_boss["y"], frame_rate_ms=data_boss["frame_rate_ms"], move_rate_ms=data_boss["move_rate_ms"])
        return boss

    def generate_consumables(self):
        data_consumables = self.levels[2]["consumable"]
        for consumable in data_consumables:
            self.consumable_list.append(Consumable(x=consumable["x"],y=consumable["y"]))

    def update(self, lista_eventos,keys,delta_ms,event,evento_1000ms):
        
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    self.pausado = not self.pausado
        
        if self.pausado:
        
            pausa_texto = self.font.render("JUEGO EN PAUSA", True, (255, 255, 255))
            self.surface.blit(pausa_texto, (self.w/2 - pausa_texto.get_width()/2, self.h/2 - pausa_texto.get_height()/2))
        
        else:
        
            if self.music:
                Auxiliar.generar_musica(self.music_path,0.1)
                self.music = False
            
            for aux_widget in self.widget_list:
                aux_widget.update(lista_eventos)

            for proyectile_element in self.proyectile_list:
                proyectile_element.update(delta_ms,self.enemies_list,self.platform_list,self.proyectile_list,proyectile_element,self.player_1,self.loot_list,self.boss)
                
            for proyectile_enemy_element in self.proyectile_enemy_list:
                proyectile_enemy_element.update(delta_ms,self.enemies_list,self.platform_list,self.proyectile_enemy_list,proyectile_enemy_element,self.player_1,self.loot_list,self.boss)

            for enemy_element in self.enemies_list:
                enemy_element.update(delta_ms,self.platform_list,self.player_1,self.proyectile_enemy_list)
                
            for loot_element in self.loot_list:
                loot_element.update(self.player_1, self.loot_list, loot_element,self.platform_list)

            for consumable_element in self.consumable_list:
                consumable_element.update(self.player_1, self.consumable_list, consumable_element)

            self.descontar_tiempo(lista_eventos,evento_1000ms)

            self.text_score._text = f'SCORE: {str(self.player_1.score)}'
            self.text_time._text = f'TIME: {str(self.cronometro)}'
            self.player_1.events(delta_ms,keys,event,self.proyectile_list,self.platform_list)
            self.player_1.update(delta_ms,self.platform_list,self.enemies_list)
            
            self.boss.update(delta_ms,self.player_1,self.enemies_list)

            self.pb_lives.value = self.player_1.lives 

            if self.boss.flag_death:
                self.score_total = self.lvl_anterior.score_total
                self.score_total += self.player_1.score
                print(self.score_total)
                self.reiniciar_nivel()
                self.reproducir_musica(self.music_menu)
                self.music = True
                self.set_active("form_game_win")
                    
            if self.player_1.lives < 1 or self.cronometro < 1:
                self.score_total = 0
                self.reiniciar_nivel()
                self.reproducir_musica(self.music_menu)
                self.set_active("form_game_lose")
                
            self.daño_background()    
            
            
    def on_click_boton1(self, parametro):
        self.reiniciar_nivel()
        self.reproducir_musica(self.music_menu)
        self.music = True
        self.set_active("form_menu_principal") 
           
    def descontar_tiempo(self,lista_eventos,evento_1000ms):
        for event in lista_eventos:
            if event.type == evento_1000ms:
                self.cronometro -= 1             
           
    def reproducir_musica(self,music_path):
        if self.music:
            Auxiliar.generar_musica(music_path,0.1)
            self.music = False
        
    def reiniciar_nivel(self):
        self.cronometro = 120
        self.music = True
        self.player_1 = self.generate_player()
        self.boss = self.generate_boss()
        self.platform_list = []
        self.enemies_list = []
        self.proyectile_list = []
        self.proyectile_enemy_list = []   
        self.loot_list = []
        self.consumable_list = []
        self.consumable_list = []
        self.generate_consumables()
        self.generate_enemies()
        self.generate_platform()

    def daño_background(self):
        if self.player_1.flag_hurted:
            self.static_background = Background(x=0,y=0,width=self.w,height=self.h,path="images/locations/forest/forest_dmg.png")
            
        if self.calculate_delta_time(TIME_DAMAGE):
            self.player_1.flag_hurted = False
            self.static_background = Background(x=0,y=0,width=self.w,height=self.h,path="images/locations/forest/forest.png")
            self.tiempo_inicial = pygame.time.get_ticks()
                
    def calculate_delta_time(self,tiempo_objetivo):
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = tiempo_actual - self.tiempo_inicial
        if tiempo_transcurrido >= tiempo_objetivo:
            return True
        else:
            return False

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
        
        self.boss.draw(self.surface)
        
        for proyectile_element in self.proyectile_list:
            proyectile_element.draw(self.surface)
            
        for proyectile_element in self.proyectile_enemy_list:
            proyectile_element.draw(self.surface)
            
        for loot_element in self.loot_list:
            loot_element.draw(self.surface)
            
        for consumable_element in self.consumable_list:
            consumable_element.draw(self.surface)