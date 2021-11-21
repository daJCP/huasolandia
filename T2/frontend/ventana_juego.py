from PyQt5 import uic
from PyQt5.QtCore import QObject, QRect, pyqtSignal, QEvent, QTimer
from PyQt5.QtGui import QIcon, QPixmap, QFont, QTransform
from PyQt5.QtWidgets import  QLabel, QStackedWidget,QVBoxLayout, QWidget

import random

import parametros as p

window_name, base_class = uic.loadUiType(p.RUTA_UI_VENTANA_JUEGO)

# COMPLETAR:
class VentanaJuego(window_name, base_class):

    senal_iniciar_juego = pyqtSignal()
    senal_tecla = pyqtSignal(str)
    senal_post_nivel = pyqtSignal(dict)
    senal_enviar_usuario = pyqtSignal(str)
    senal_pausa = pyqtSignal(int)
    senal_inicio_menu = pyqtSignal()
    detener_game = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.arenas = []
        # COMPLETAR
        self.setupUi(self)
        self.init_gui()
        self.ronda = 0
        self.num_auto = 0
        self.cheats = []

    def keyPressEvent(self, event):
        if event.text() in  [p.TECLA_ARRIBA,
         p.TECLA_ABAJO, p.TECLA_DERECHA, p.TECLA_IZQUIERDA, p.TECLA_SALTAR, p.TECLA_PAUSAR]:
            if event.text() == p.TECLA_ARRIBA:
                self.senal_tecla.emit('U')
            elif event.text() == p.TECLA_ABAJO:
                self.senal_tecla.emit('D')
            elif event.text() == p.TECLA_IZQUIERDA:
                self.senal_tecla.emit('L')
            elif event.text() == p.TECLA_DERECHA:
                self.senal_tecla.emit('R')
            elif event.text() == p.TECLA_SALTAR:
                self.senal_tecla.emit('Jump')
            elif event.text() == p.TECLA_PAUSAR:
                self.pausar()
        if len(self.cheats) < 3:
            self.cheats.append(event.text())
        else:
            self.cheats.pop(0)
            self.cheats.append(event.text())
        if self.cheats == ['v','i','d']:
            self.senal_tecla.emit('vidas')
        elif self.cheats == ['n','i','v']:
            self.senal_tecla.emit('nivel')
        

    def mostrar_ventana(self, usuario):
        self.show()
        self.puntaje_count.setText('0')
        self.senal_enviar_usuario.emit(usuario)
        self.senal_iniciar_juego.emit()


    def init_gui(self):

        self.setWindowIcon(QIcon(p.RUTA_ICONO))
        self.setWindowTitle("DCCossy Frog")

        self.pausa_button.clicked.connect(self.pausar)

        self.salir_button.clicked.connect(self.salir_menu_inicio)
        
        self.logo = QPixmap(p.RUTA_LOGO)
        self.foto_rana.setPixmap(self.logo)
        self.foto_rana.setScaledContents(True)

        #cargar pasto
        self.pasto = QPixmap(p.RUTA_PASTO)
        self.game_map.setPixmap(self.pasto)
        self.game_map.setScaledContents(True)

        self.map_box = QVBoxLayout()
        self.map_box.setGeometry(QRect(10,10,580,790))

        self.stack = QStackedWidget()

        self.cargar_nivel()
    
    def salir_menu_inicio(self):
        self.senal_inicio_menu.emit()
        self.hide()
        self.detener_game.emit('Xd')
    
    def pausar(self):
        self.senal_pausa.emit(-1)
    
    def post_nivel(self, dict):
        self.hide()
        for auto in self.dic_auto_skin:
            self.dic_auto_skin[auto].hide()
        for tabla in self.dic_tablones:
            self.dic_tablones[tabla].hide()
        self.senal_post_nivel.emit(dict)

    def cargar_nivel(self):

        self.dic_auto_skin = dict()
        self.dic_tablones = dict()
        self.dic_power_ups = dict()

        self.coin_skin = QPixmap(p.RUTA_MONEDA)
        self.reloj_skin = QPixmap(p.RUTA_RELOJ)
        self.calavera_skin = QPixmap(p.RUTA_CALAVERA)
        self.vidas_skin = QPixmap(p.RUTA_VIDA)
        self.power_list = [self.vidas_skin, self.coin_skin, self.calavera_skin, self.reloj_skin]
        #
        
        self.monedas.setPixmap(self.coin_skin)
        self.monedas.setScaledContents(True)
        self.tiempo.setPixmap(self.reloj_skin)
        self.tiempo.setScaledContents(True)
        self.vidas.setPixmap(self.vidas_skin)
        self.vidas.setScaledContents(True)

        # carretera 1
        self.carretera1 = QLabel('', self)
        self.pixeles_carretera = QPixmap(p.RUTA_SKIN_CARRETERA)
        self.carretera1.setPixmap(self.pixeles_carretera)
        self.carretera1.setScaledContents(True)
        self.carretera1.resize(600,150)
        self.carretera1.move(0,100)

        #rio
        self.rio1 = QLabel('', self)
        self.pixeles_rio = QPixmap(p.RUTA_SKIN_RIO)
        self.rio1.setPixmap(self.pixeles_rio)
        self.rio1.setScaledContents(True)
        self.rio1.resize(600, 210)
        self.rio1.move(0, 295)

        #carretera 2
        self.carretera2 = QLabel('', self)
        self.pixeles_carretera = QPixmap(p.RUTA_SKIN_CARRETERA)
        self.carretera2.setPixmap(self.pixeles_carretera)
        self.carretera2.setScaledContents(True)
        self.carretera2.resize(600,150)
        self.carretera2.move(0,550)

        #cargamos autos
        #amarillo
        self.auto_amarillo = [QPixmap(p.RUTA_AUTO_AMARILLO_LEFT),
         QPixmap(p.RUTA_AUTO_AMARILLO_RIGHT)]
        #azul
        self.auto_azul = [QPixmap(p.RUTA_AUTO_AZUL_LEFT), QPixmap(p.RUTA_AUTO_AZUL_RIGHT)]
        #blanco
        self.auto_blanco = [ QPixmap(p.RUTA_AUTO_BLANCO_LEFT), QPixmap(p.RUTA_AUTO_BLANCO_RIGHT)]
        #morado
        self.auto_morado = [QPixmap(p.RUTA_AUTO_MORADO_LEFT), QPixmap(p.RUTA_AUTO_MORADO_RIGHT)]
        #negro
        self.auto_negro = [ QPixmap(p.RUTA_AUTO_NEGRO_LEFT), QPixmap(p.RUTA_AUTO_NEGRO_RIGHT)]
        #plata
        self.auto_plata = [ QPixmap(p.RUTA_AUTO_PLATA_LEFT),QPixmap(p.RUTA_AUTO_PLATA_RIGHT)]
        #rojo
        self.auto_rojo = [QPixmap(p.RUTA_AUTO_ROJO_LEFT), QPixmap(p.RUTA_AUTO_ROJO_RIGHT)]

        self.pix_autos = [
            self.auto_amarillo, self.auto_azul,
            self.auto_blanco, self.auto_morado, self.auto_negro,
            self.auto_plata, self.auto_rojo
        ]
        self.tablones_skin = QPixmap(p.RUTA_TABLONES)
        #cargar tablones 
        self.cargar_tablones()
        self.cargar_power_up()
        #cargar rana
        self.cargar_rana()
        #cargar autos
        self.cargar_autos()
        #cargo barra 
        self.cargar_barra()

    def actualizar_timer(self, dict):
        if self.ronda != dict['ronda']:
            self.ronda = dict['ronda']
            self.show()
        if dict['input_movimiento'] != None:
            if dict['rana'].isjumping:
                self.salto_rana(dict['new_pos'], dict['rana_dir'])
            elif dict['input_movimiento'] != 'Jump' and dict['rana'].isjumping == False:
                self.avanzar_rana(dict['new_pos'], dict['rana_dir'])
            elif dict['rana'].isjumping == False and not dict['rana'].cold_down:
                self.avanzar_rana(dict['new_pos'], dict['rana_dir'])
        self.tiempo_count.setText(str(dict['jugador'].tiempo)+ 's')
        self.actualizar_power_up(dict['power_ups'])
        self.actualizar_auto(dict['carretera1'], dict['carretera2'])
        self.actualizar_muerte(*dict['choco'])
        self.actualizar_tablones(dict['rio'])
        self.nivel_count.setText(str(dict['ronda']))
        self.vidas_count.setText(
            str(dict['jugador'].vidas) if dict['jugador'].vidas >= 0 else '0'
            )
        self.monedas_count.setText(str(dict['jugador'].monedas_ronda))

    def cargar_power_up(self):
        self.objects = [QLabel('', self) for x in range(4)]
        num = 0
        for label in self.objects:
            label.setPixmap(self.power_list[num])
            label.setScaledContents(True)
            label.setGeometry(10,10, p.SIZE_OBJECTS * 0.5, p.SIZE_OBJECTS * 0.5)
            num += 1
        
    def actualizar_power_up(self, power_up):
        for objeto in power_up.objetos:
            if objeto not in self.dic_power_ups:
                self.dic_power_ups[objeto] = self.objects.pop(0)
        for power in self.dic_power_ups:
            self.dic_power_ups[power].move(power.hitbox.x()+ p.SIZE_OBJECTS * 0.5,
             power.hitbox.y() + p.SIZE_OBJECTS * 0.5)
        
    def salto_rana(self, posicion, direccion):
        self.timer = QTimer()
        self.timer.setInterval(1000 * 0.08)
        self.timer.timeout.connect(self.timer_jump_tick)
        self.subclick_jump = 0
        self.isjumping = True
        self.nueva_posicion_salto = posicion
        self.direccion = direccion
        self.ciclo_jumping = self.pix_rana_jump.copy()
        self.timer.start()
    
    def timer_jump_tick(self):
        self.subclick_jump += 1
        if self.direccion == 'U':
            tr = QTransform()
            tr.rotate(0)
            self.ciclo_jumping[0] = self.ciclo_jumping[0].transformed(tr)
            self.rana_skin_label.setPixmap(self.ciclo_jumping[-1])
           
        elif self.direccion == 'D':
            tr = QTransform()
            tr.rotate(180)
            self.ciclo_jumping[0] = self.ciclo_jumping[0].transformed(tr)
            self.rana_skin_label.setPixmap(self.ciclo_jumping[0])
            self.rotar_animacion(self.ciclo_jumping)
            
        elif self.direccion == 'L':
            tr = QTransform()
            tr.rotate(270)
            self.ciclo_jumping[0] = self.ciclo_jumping[0].transformed(tr)
            self.rana_skin_label.setPixmap(self.ciclo_jumping[0])
            self.rotar_animacion(self.ciclo_jumping)
            
        elif self.direccion == 'R':
            tr = QTransform()
            tr.rotate(90)
            self.ciclo_jumping[0] = self.ciclo_jumping[0].transformed(tr)
            self.rana_skin_label.setPixmap(self.ciclo_jumping[0])
            self.rotar_animacion(self.ciclo_jumping)

        self.rana_skin_label.move(self.nueva_posicion_salto.x() - 5,
         self.nueva_posicion_salto.y() - 5)

        if self.subclick_jump == 7:
            self.isjumping = False
            self.timer.stop()
            if self.direccion == 'U':
                self.rana_skin_label.setPixmap(self.pix_rana_up[0])
                
            elif self.direccion == 'D':
                self.rana_skin_label.setPixmap(self.pix_rana_down[0])
            
            elif self.direccion == 'L':
                self.rana_skin_label.setPixmap(self.pix_rana_left[0])
                
            elif self.direccion == 'R':
                self.rana_skin_label.setPixmap(self.pix_rana_right[0])
        
    def actualizar_muerte(self,choco, rana):
        self.rana_skin_label.move(rana.x(), rana.y())

    def actualizar_auto(self,carretera_1, carretera_2):
        for pista in carretera_1.pistas:
            for auto in pista.autos:
                if auto not in list(self.dic_auto_skin.keys()):
                    if pista.direccion == 1:
                        self.dic_auto_skin[auto] = self.autos_right.pop()
                    if pista.direccion == 0:
                        self.dic_auto_skin[auto] = self.autos_left.pop()
                        
        for pista in carretera_2.pistas:
            for auto in pista.autos:
                if auto not in list(self.dic_auto_skin.keys()):
                    if pista.direccion == 1:
                        self.dic_auto_skin[auto] = self.autos_right.pop()
                    if pista.direccion == 0:
                        self.dic_auto_skin[auto] = self.autos_left.pop()
        
        for auto in self.dic_auto_skin:
            self.dic_auto_skin[auto].move(auto.hitbox.x() , auto.hitbox.y() )

    def actualizar_tablones(self, rio):
        for linea in rio.lineas:
            for tablon in linea.tablones:
                if tablon not in list(self.dic_tablones.keys()):
                    self.dic_tablones[tablon] = self.tablones.pop()
        
        for tablon in self.dic_tablones:
            self.dic_tablones[tablon].move(tablon.hitbox.x() , tablon.hitbox.y() )
    
    def cargar_tablones(self):
        self.tablones = [
            QLabel('', self) for x in range( p.NUM_TABLONES * 20)
        ]
        for a in self.tablones:
            a.setPixmap(self.tablones_skin)
            a.setScaledContents(True)
            a.setGeometry(600, 100, p.LARGO_TABLON, p.ANCHO_TABLON)

    def cargar_barra(self):
        self.barra_principal = QLabel('',self)
        self.barra_principal.setGeometry(600,0,100,800)
        self.barra_principal.setPixmap(self.logo)
        self.barra_principal.setScaledContents(True)
        self.barra_principal.setStyleSheet('background-color: #036639')

    def cargar_autos(self):
        self.autos_left = [
            QLabel('', self) for x in range( p.NUM_AUTOS * 30)
        ]
        for a in self.autos_left:
            a.setPixmap(random.choice(self.pix_autos)[0])
            a.setScaledContents(True)
            a.setGeometry(600, 100, p.LARGO_CAR, p.ANCHO_CAR)
        self.autos_right = [
            QLabel('', self) for x in range( p.NUM_AUTOS * 30)
        ]
        for a in self.autos_right:
            a.setPixmap(random.choice(self.pix_autos)[1])
            a.setScaledContents(True)
            a.setGeometry(600, 500, p.LARGO_CAR, p.ANCHO_CAR)

    def cargar_rana(self):
        self.rana_skin_label = QLabel('', self)
        #rana stay
        self.pixeles_rana = QPixmap(p.RUTA_SKIN_RANA_STILL)
        #rana left
        self.pix_rana_left = [QPixmap(p.RUTA_SKIN_RANA_LEFT_1), 
        QPixmap(p.RUTA_SKIN_RANA_LEFT_2),QPixmap(p.RUTA_SKIN_RANA_LEFT_3)]
        #RANA RIGHT
        self.pix_rana_right = [QPixmap(p.RUTA_SKIN_RANA_RIGHT_1),
        QPixmap(p.RUTA_SKIN_RANA_RIGHT_2), QPixmap(p.RUTA_SKIN_RANA_RIGHT_3)]
        #RANA UP
        self.pix_rana_up = [QPixmap(p.RUTA_SKIN_RANA_UP_1), 
        QPixmap(p.RUTA_SKIN_RANA_UP_2), QPixmap(p.RUTA_SKIN_RANA_UP_3)]
        #RANA DOWN
        self.pix_rana_down = [QPixmap(p.RUTA_SKIN_RANA_DOWN_1), QPixmap(p.RUTA_SKIN_RANA_DOWN_2),
        QPixmap(p.RUTA_SKIN_RANA_DOWN_3)]
        #RANA JUMP
        self.pix_rana_jump = [QPixmap(p.RUTA_SKIN_JUMP_1),  QPixmap(p.RUTA_SKIN_JUMP_1),
         QPixmap(p.RUTA_SKIN_JUMP_2), QPixmap(p.RUTA_SKIN_JUMP_2), QPixmap(p.RUTA_SKIN_JUMP_3),
         QPixmap(p.RUTA_SKIN_JUMP_3), QPixmap(p.RUTA_SKIN_JUMP_3)]

        self.rana_skin_label.setPixmap(self.pixeles_rana)
        self.rana_skin_label.setScaledContents(True)
        self.rana_skin_label.resize(p.SIZE_FROG, p.SIZE_FROG)
        self.rana_skin_label.move(*p.POS_INICIO)
    
    
    def avanzar_rana(self, new_posicion, direccion):
        if direccion == 'U':
            self.rana_skin_label.setPixmap(self.pix_rana_up[0])
            self.rotar_animacion(self.pix_rana_up)
        elif direccion == 'D':
            self.rana_skin_label.setPixmap(self.pix_rana_down[0])
            self.rotar_animacion(self.pix_rana_down)
        elif direccion == 'L':
            self.rana_skin_label.setPixmap(self.pix_rana_left[0])
            self.rotar_animacion(self.pix_rana_left)
        elif direccion == 'R':
            self.rana_skin_label.setPixmap(self.pix_rana_right[0])
            self.rotar_animacion(self.pix_rana_right)
        self.rana_skin_label.move(new_posicion.x() - 5, new_posicion.y() - 5)

    def cargar_carretera(self):
        self.carretera1 = QLabel('', self)
        self.pixeles_carretera = QPixmap(p.RUTA_SKIN_CARRETERA)
        self.carretera.setPixmap(self.pixeles_carretera)
        self.carretera.setScaledContents(True)
        self.carretera.setScaledContents(True)
    def rotar_animacion(self,lista):
        lista.append(lista.pop(0))
    def salir(self):
        self.close()
    