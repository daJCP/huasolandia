from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout,
)
from PyQt5 import uic

import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_RANKING)

class VentanaRanking(window_name, base_class):

    senal_volver = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
        with open('ranking.txt', 'a') as file:
            pass

    def init_gui(self):
            
        self.setWindowIcon(QIcon(p.RUTA_ICONO))
        
        self.rana_logo.setPixmap(QPixmap(p.RUTA_LOGO))
        self.rana_logo.setScaledContents(True)

        self.Salir.clicked.connect(self.volver)

    def volver(self):
        self.senal_volver.emit()
        self.hide()

    def top5(self):
        with open('ranking.txt', 'r') as file:
            lista = []
            for line in file:
                lista.append(line.strip().split(','))
            lista = sorted(lista, key=lambda x: int(x[1]), reverse=True)
            return lista

    def revisar_top5(self):
        self.lista = self.top5()
        num = 0
        self.labels = []
        self.labels.append((self.top_1, self.pts_1))
        self.labels.append((self.top_2, self.pts_2))
        self.labels.append((self.top_3, self.pts_3))
        self.labels.append((self.top_4, self.pts_4))
        self.labels.append((self.top_5, self.pts_5))

        for x in self.labels:
            for y in x:
                y.hide()

        for top in self.lista:
            if num <= 4:
                self.labels[num][0].setText(top[0].strip())
                self.labels[num][1].setText(top[1].strip())
                num += 1
        for label in self.labels[:num]:
            for l in label:
                l.show()
        

    def mostrar(self):
        self.revisar_top5()
        self.show()
