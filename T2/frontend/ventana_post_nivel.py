from PyQt5 import uic
from PyQt5.QtCore import QObject, QRect, pyqtSignal, QEvent, QTimer
from PyQt5.QtGui import QIcon, QPixmap, QFont, QTransform

import random

import parametros as p


window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_POST)

class VenPost(window_name, base_class):
    senal_enviar_datos = pyqtSignal(dict)
    senal_siguiente_ronda = pyqtSignal(dict)
    senal_volver_menu = pyqtSignal()
    senal_detener_post = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
        self.ganador = False
        self.data = None
    def init_gui(self):
        self.setWindowIcon(QIcon(p.RUTA_ICONO))

        self.siguiente_nivel.clicked.connect(self.siguiente_ronda)
        self.puntaje_count.setText('0')

        self.Salir.clicked.connect(self.salir_menu_inicio)
        
        self.label_10.setPixmap(QPixmap(p.RUTA_MONEDA))
        self.label_10.setScaledContents(True)
        self.label_9.setPixmap(QPixmap(p.RUTA_VIDA))
        self.label_9.setScaledContents(True)

        self.rana_bailando_anima()

    def salir_menu_inicio(self):
        self.senal_volver_menu.emit()
        self.hide()


    def siguiente_ronda(self):
        self.senal_siguiente_ronda.emit(self.data)
        self.hide()
    
    def rana_bailando_anima(self):
        self.foto_1 = QPixmap(p.RUTA_SKIN_RANA_DOWN_1)
        self.foto_2 = QPixmap(p.RUTA_SKIN_RANA_DOWN_3)
        self.fotos = [self.foto_1,self.foto_2]

        self.timer_rana = QTimer()
        self.timer_rana.setInterval(1000 * 0.5)
        self.timer_rana.timeout.connect(self.timer_animacion_tick)
        self.timer_animacion_tick()

    def timer_animacion_tick(self):
        
        self.rana_bailando.setPixmap(self.fotos[0])
        self.rana_bailando.setScaledContents(True)

        self.fotos.append(self.fotos.pop(0))

    def mostrar(self):
        self.timer_rana.start()
        self.show()
        
    def ocultar(self):
        self.timer_rana.stop()
        self.siguiente_nivel.show()
        self.hide()
    
    def datos(self, event):
        
        self.ganador = event['isGanador']
        self.data = event

        if event['isGanador'] == True:
            self.w_n_w.setText('COMPLETASTE LA RONDA PUEDES SEGUIR JUGANDO')
            self.w_n_w.setStyleSheet(
                '''
border-style: dashed;
background-color: #85ffde;
width: 20px;
border: 5px  solid #488c7a;
border-style:  groove ;
color: black;
'''
            )
            self.siguiente_nivel.show()
        else:
            self.w_n_w.setText(
                '                                        GAME OVER'
                )
            self.w_n_w.setStyleSheet(
                '''
border-style: dashed;
background-color: #e82b0e;
width: 20px;
border: 5px  solid #a61c07;
border-style:  groove ;
color: black;
'''
            )
            self.siguiente_nivel.hide()
        
        self.label_4.setText(event['usuario'])
        self.nivel_count.setText(str(event['ronda']))
        self.label_5.setText(str(event['jugador'].monedas))
        self.label_6.setText(str(event['jugador'].vidas if event['jugador'].vidas >= 0 else 0))
        self.label_7.setText(str(event['jugador'].puntaje))
        self.calcular_puntaje(event)

        self.mostrar()

    def calcular_puntaje(self, data):
        self.jugador = data['jugador']
        self.tiempo = data['tiempo']
        self.ronda = data['ronda']
        self.monedas_ronda = data['monedas_ronda']
        self.puntaje_nivel = data['puntaje_ronda']
        self.tiempo_ronda = data['tiempo']
        self.animacion_tiempo()
    
    def animacion_tiempo(self):
        self.timer_tiempo = QTimer()
        self.timer_tiempo.setInterval( 1000 * 0.005 )
        self.timer_tiempo.timeout.connect(self.timer_animacion_tiempo_tick)
        self.sub_tiempo = -1
        self.timer_tiempo.start()
        
    def timer_animacion_tiempo_tick(self):
        self.sub_tiempo += 1
        self.tiempo_count.setText(str(self.sub_tiempo))
        if str(self.sub_tiempo) == str(self.tiempo_ronda):
            self.timer_tiempo.stop()
            self.animacion_monedas()

    def animacion_monedas(self):
        self.timer_monedas = QTimer()
        self.timer_monedas.setInterval( 1000 * 0.05)
        self.timer_monedas.timeout.connect(self.timer_animacion_monedas_tick)
        self.sub_monedas = -1
        self.timer_monedas.start()
        
    def timer_animacion_monedas_tick(self):
        self.sub_monedas += 1
        self.monedas_count.setText(str(self.sub_monedas))
        if str(self.sub_monedas) == str(self.monedas_ronda):
            self.timer_monedas.stop()
            self.animacion_puntaje()
    
    def animacion_puntaje(self):
        self.timer_puntaje = QTimer()
        self.timer_puntaje.setInterval( 1000 * 0.0002)
        self.timer_puntaje.timeout.connect(self.timer_animacion_puntaje_tick)
        self.sub_puntos = -1
        self.timer_puntaje.start()

    def timer_animacion_puntaje_tick(self):
        self.sub_puntos += 1
        self.puntaje_count.setText(str(self.sub_puntos))
        if self.sub_puntos == self.puntaje_nivel:
            self.timer_puntaje.stop()
            
            

