import pygame
from pygame.locals import *
import sys
from constantes import *
from gui_form import Form
from gui_form_menu_principal import FormMenuPrincipal
from gui_form_menu_niveles import FormMenuLvl
from gui_form_menu_scoreboard import FormMenuScoreBoard
from gui_form_menu_game_l1 import FormGameLevel1
from gui_form_menu_game_l2 import FormGameLevel2
from gui_form_menu_game_l3 import FormGameLevel3
from gui_form_menu_ganador import FormMenuWin
from gui_form_menu_perdedor import FormMenuLose
from gui_form_menu_instructions import FormMenuInstructions
from auxiliar import Auxiliar 

flags = DOUBLEBUF 
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
music_path = r"music/title_theme.wav"


pygame.init()
pygame.mixer.init()

evento_1000ms = pygame.USEREVENT
pygame.time.set_timer(evento_1000ms, 1000)

clock = pygame.time.Clock()
config_json = Auxiliar.leer_archivo("levels.json")

form_menu_principal = FormMenuPrincipal(name="form_menu_principal",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=C_BLACK,color_border=None,active=True)
form_menu_niveles = FormMenuLvl(name="form_menu_niveles",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=C_BLACK,color_border=C_WHITE,active=False)
form_menu_instructions = FormMenuInstructions(name="form_menu_instructions",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=C_BLACK,color_border=None,active=False)
form_menu_scoreboard = FormMenuScoreBoard(name="form_menu_scoreboard",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=C_BLACK,color_border=C_WHITE,active=False)

form_game_L1 = FormGameLevel1(name="form_game_L1",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False,config_json=config_json)
form_game_L2 = FormGameLevel2(name="form_game_L2",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False,config_json=config_json,lvl1=form_game_L1)
form_game_L3 = FormGameLevel3(name="form_game_L3",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False,config_json=config_json,lvl2=form_game_L2)

form_game_win = FormMenuWin(name="form_game_win",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=C_BLACK,color_border=(255,0,255),active=False,lvl3=form_game_L3)
form_game_lose = FormMenuLose(name="form_game_lose",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=C_BLACK,color_border=(255,0,255),active=False)

while True:     
    lista_eventos = pygame.event.get()
    

    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)

    aux_form_active = Form.get_active()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    if(aux_form_active != None):
        try:
            aux_form_active.update(lista_eventos,keys,delta_ms,event,evento_1000ms)
        except:
            aux_form_active.update(lista_eventos,keys,delta_ms,event)
        aux_form_active.draw()
    pygame.display.flip()




    


  


