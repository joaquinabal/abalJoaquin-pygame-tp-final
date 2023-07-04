import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from auxiliar import Auxiliar
from gui_label import Label

class FormMenuLvl(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.music_path = r"music/title_theme.wav"



        self.title = Label(master=self,x=500,y=100,w=400,text="NIVELES",color_border=None,font="Verdana",font_size=50,font_color=C_ORANGE)
        self.boton_lvl1 = Button(master=self,x=600,y=300,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Data_Border/Buttons/Button_M_06.png",on_click=self.on_click_boton3,on_click_param="form_game_L1",text="LVL1",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton_lvl2 = Button(master=self,x=600,y=400,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Data_Border/Buttons/Button_M_06.png",on_click=self.on_click_boton3,on_click_param="form_game_L2",text="LVL2",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton_lvl3 = Button(master=self,x=600,y=500,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Data_Border/Buttons/Button_M_06.png",on_click=self.on_click_boton3,on_click_param="form_game_L3",text="LVL 3",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton_back = Button(master=self,x=200,y=600,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Data_Border/Buttons/Button_M_06.png",on_click=self.on_click_boton3,on_click_param="form_menu_principal",text="BACK",font="Verdana",font_size=30,font_color=C_WHITE)                                
     
        self.lista_widget = [self.boton_lvl1,self.boton_lvl2,self.boton_lvl3,self.title,self.boton_back]

    def on_click_boton1(self, parametro):
        self.pb1.value += 1
 
    def on_click_boton2(self, parametro):
        self.pb1.value -= 1
    
    def on_click_boton3(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos,keys,delta_ms,event):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

        
    def draw(self): 
        super().draw()
        

        
        for aux_widget in self.lista_widget:    
            aux_widget.draw()