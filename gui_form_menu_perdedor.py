from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_label import Label


class FormMenuLose(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.music_path = r"music/title_theme.wav"

        self.title = Label(master=self,x=375,y=100,w=700,h=100,text="HAS PERDIDO",color_border=None,font="Verdana",font_size=100,font_color=C_RED)
        self.button_menu = Button(master=self,x=1275,y=725,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Data_Border/Buttons/Button_M_06.png",on_click=self.on_click_boton3,on_click_param="form_menu_principal",text="MENU",font="Verdana",font_size=30,font_color=C_WHITE)
     
        self.lista_widget = [self.title,self.button_menu]

    
    def on_click_boton3(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos,keys,delta_ms,event):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

        
    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()