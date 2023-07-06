import pygame
from pygame.locals import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from constantes import *

import sqlite3

class Sql():

    def actualizar_tabla(nombre, score):
        with sqlite3.connect("db/db_score.db") as conexion:
            try:
                conexion.execute("insert into scoreboard (nombre,score) values (?,?)", (nombre, score))
                conexion.commit()# Actualiza los datos realmente en la tabla
            except:
                print("Error")
    
    def crear_tabla():
        
        with sqlite3.connect("db/db_score.db") as conexion:
            try:
                sentencia = ''' create  table scoreboard
                                (
                                        id integer primary key autoincrement,
                                        nombre text,
                                        score real
                                )
                            '''
                conexion.execute(sentencia)
                print("Se creo la tabla highscore")                       
            except sqlite3.OperationalError:
                print("La tabla ya existe")

    def devolver_puntaje():
        lista_scoreboard = []
        with sqlite3.connect("db/db_score.db") as conexion:
            cursor=conexion.execute("SELECT nombre, score FROM scoreboard ORDER BY score DESC LIMIT 5")
            
            for fila in cursor:
                lista_scoreboard.append(fila)
        #print(lista_scoreboard)
        return lista_scoreboard

        
    # def update(self, lista_eventos,keys,delta_ms,event):
    #     for aux_widget in self.lista_widget:
    #         aux_widget.update(lista_eventos)

    # def draw(self): 
    #     super().draw()
    #     for aux_widget in self.lista_widget:    
    #         aux_widget.draw()