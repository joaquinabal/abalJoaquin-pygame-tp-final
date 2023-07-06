import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from auxiliar import Auxiliar
from gui_label import Label
from sql import Sql

class FormMenuScoreBoard(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.music_path = r"music/title_theme.wav"



        self.title = Label(master=self,x=500,y=100,w=400,text="SCOREBOARD",color_border=None,font="Verdana",font_size=50,font_color=C_YELLOW_2)
        self.puesto_1 = Label(master=self,x=500,y=200,w=400,text=f"1- XXX - XXX",color_border=None,font="Verdana",font_size=30,font_color=C_WHITE)
        self.puesto_2 = Label(master=self,x=500,y=250,w=400,text=f"2- XXX - XXX",color_border=None,font="Verdana",font_size=30,font_color=C_WHITE)
        self.puesto_3 = Label(master=self,x=500,y=300,w=400,text=f"3- XXX - XXX",color_border=None,font="Verdana",font_size=30,font_color=C_WHITE)
        self.puesto_4 = Label(master=self,x=500,y=350,w=400,text=f"4- XXX - XXX",color_border=None,font="Verdana",font_size=30,font_color=C_WHITE)
        self.puesto_5 = Label(master=self,x=500,y=400,w=400,text=f"5- XXX - XXX",color_border=None,font="Verdana",font_size=30,font_color=C_WHITE)
           
        self.boton_back = Button(master=self,x=200,y=600,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Data_Border/Buttons/Button_M_06.png",on_click=self.on_click_boton3,on_click_param="form_menu_principal",text="BACK",font="Verdana",font_size=30,font_color=C_WHITE)                                
   
           
            
        self.lista_widget = [self.puesto_1,self.puesto_2,self.puesto_3,self.puesto_4,self.puesto_5,self.title,self.boton_back]
    
    def on_click_boton3(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos,keys,delta_ms,event):
        lista_scoreboard = Sql.devolver_puntaje()
        self.probar_scoreboard(lista_scoreboard,self.puesto_1,1,0)
        self.probar_scoreboard(lista_scoreboard,self.puesto_2,2,1)
        self.probar_scoreboard(lista_scoreboard,self.puesto_3,3,2)
        self.probar_scoreboard(lista_scoreboard,self.puesto_4,4,3)
        self.probar_scoreboard(lista_scoreboard,self.puesto_5,5,4)

        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def probar_scoreboard(self,lista_sb,label,order,posicion_array,):    
        try:
            label._text = f"{order}- {lista_sb[posicion_array][0]} - {int(lista_sb[posicion_array][1])}"
        except:
            pass
            
        
    def draw(self): 
        super().draw()
        

        
        for aux_widget in self.lista_widget:    
            aux_widget.draw()