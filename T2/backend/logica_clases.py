from PyQt5.QtCore import QObject, QPoint, QTimer, Qt, pyqtSignal, QRect
import random

import parametros as p


class Jugador:
    def __init__(self, usuario):
        self.usuario = usuario
        self.monedas = None
        self.puntaje = None
        self.vidas = p.VIDAS_INICIO
    def seterar_monedad(self, monedas):
        self.monedas = monedas
    def setear_puntaje(self, puntaje):
        self.puntaje = puntaje



    

