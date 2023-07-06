import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from auxiliar import Auxiliar
from gui_label import Label
from background import Background

class FormMenuInstructions(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.music_path = r"music/title_theme.wav"
        self.static_background = Background(x=70,y=50,width=w*0.9,height=h*0.9,path="images/menu/instructions.png")

        self.boton_back = Button(master=self,x=1050,y=700,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Data_Border/Buttons/Button_M_06.png",on_click=self.on_click_boton3,on_click_param="form_menu_principal",text="BACK",font="Verdana",font_size=30,font_color=C_WHITE)                                
     
        self.lista_widget = [self.boton_back]

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
        
        self.static_background.draw(self.surface)
        
        for aux_widget in self.lista_widget:    
            aux_widget.draw()