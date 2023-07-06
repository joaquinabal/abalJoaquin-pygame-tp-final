import pygame
import sys
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from auxiliar import Auxiliar
from gui_label import Label


class FormMenuPrincipal(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.music_path = r"music/title_theme.wav"
        self.music = True
        Auxiliar.generar_musica(self.music_path,0.1)

        self.title = Label(master=self,x=500,y=100,w=400,text="PYGAME SOULS",color_border=None,font="Verdana",font_size=50,font_color=C_ORANGE)
        self.boton_jugar = Button(master=self,x=600,y=300,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Data_Border/Buttons/Button_M_06.png",on_click=self.on_click_boton3,on_click_param="form_game_L1",text="Jugar",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton_niveles = Button(master=self,x=600,y=400,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Data_Border/Buttons/Button_M_06.png",on_click=self.on_click_boton3,on_click_param="form_menu_niveles",text="Niveles",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton_instrucciones = Button(master=self,x=600,y=500,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Data_Border/Buttons/Button_M_06.png",on_click=self.on_click_boton3,on_click_param="form_menu_instructions",text="Instrucciones",font="Verdana",font_size=20,font_color=C_WHITE) 
        self.boton_scoreboard = Button(master=self,x=600,y=700,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Data_Border/Buttons/Button_M_06.png",on_click=self.on_click_boton3,on_click_param="form_menu_scoreboard",text="SCOREBOARD",font="Verdana",font_size=20,font_color=C_WHITE)
       
        self.boton_salir = Button(master=self,x=600,y=600,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Data_Border/Buttons/Button_M_06.png",on_click=self.on_click_boton2,on_click_param="form_game_L3",text="Salir",font="Verdana",font_size=30,font_color=C_WHITE)
                                
        self.lista_widget = [self.boton_jugar,self.boton_niveles,self.boton_instrucciones,self.boton_salir,self.title,self.boton_scoreboard]

    def on_click_boton1(self, parametro):
        self.pb1.value += 1
 
    def on_click_boton2(self, parametro):
        pygame.quit()
        sys.exit()
    
    def on_click_boton3(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos,keys,delta_ms,event):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)
        
    def draw(self): 
        super().draw()
        
        for aux_widget in self.lista_widget:    
            aux_widget.draw()