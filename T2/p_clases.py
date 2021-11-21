from PyQt5.QtCore import QObject, QPoint, QTimer, Qt, pyqtSignal, QRect, qrand

import parametros as p

import random 

class Jugador:
    def __init__(self, usuario):
        self.usuario = usuario
        self.monedas = 0
        self.puntaje = 0

        self.tiempo = 0

        self.monedas_ronda = 0
        self.vidas = p.VIDAS_INICIO
    def seterar_monedad(self, monedas):
        self.monedas = monedas
    def setear_puntaje(self, puntaje):
        self.puntaje = puntaje

class Pasto(QObject):
    def __init__(self, x, y , largo, ancho):
        super().__init__()
        self.hitbox = QRect(x,y,largo, ancho)

class Rana(QObject):
    
    def __init__(self):
        super().__init__()
        self.direccion = 'U'
        self.posibles_direcciones = {
            'U': (0 ,-1 * p.MOVIMIENTO),
            'D': (0, p.MOVIMIENTO),
            'L': (-1 * p.MOVIMIENTO, 0),
            'R': (p.MOVIMIENTO, 0)
        }
        self.hitbox = QRect(*p.POS_INICIO, p.SIZE_FROG - 10 , p.SIZE_FROG - 10)
        self.isjumping = False
        self.istablon = False
        self.cold_down = False
        self.ganador = False
    
    def jump(self):
        self.timer = QTimer()
        self.timer.setInterval(1000 * 0.05)
        self.timer.timeout.connect(self.timer_jump_tick)
        self.subclick_jump = 0
        self.isjumping = True

        self.timer.start()
    
    def timer_jump_tick(self):
        self.subclick_jump+= 1
        if self.subclick_jump == p.PIXELES_SALTO:
            self.isjumping = False
            self.timer.stop()

            self.instanciar_cold_down()
        else:
            self.avanzar()

    def instanciar_cold_down(self):
        self.timer_cold_down = QTimer()
        self.timer_cold_down.setInterval(1000* 0.7)
        self.timer_cold_down.timeout.connect(self.timer_jump_cold_down_tick)
        self.subtick_cold_down = 0

        self.timer_cold_down.start()

    def timer_jump_cold_down_tick(self):
        self.subtick_cold_down += 1
        if self.subtick_cold_down == 1:
            self.cold_down = False
            self.timer_cold_down.stop()
        
    def cambiar_direccion(self, nueva_direccion):
        if nueva_direccion.upper() in 'UDLR':
            self.direccion = nueva_direccion
        self.avanzar()
    
    def avanzar(self):
        if 10 <= self.hitbox.translated(*self.posibles_direcciones[self.direccion]).x() <= 560:
            if 10 <= self.hitbox.translated(*self.posibles_direcciones[self.direccion]).y() <= 760:
                self.hitbox = self.hitbox.translated(*self.posibles_direcciones[self.direccion])
    def volver(self, jugador):
        self.hitbox.moveTo(*p.POS_INICIO)
        jugador.vidas -= 1

class Rio(QObject):
    def __init__(self, x, y,largo, ancho):
        super().__init__()
        self.hitbox = QRect(x,y,largo,ancho)
        self.direccion_prin = random.choice([0,1])
        self.direccion_sec = 1 if self.direccion_prin == 0 else 0
        self.linea_1 = Linea(self.direccion_sec, self.hitbox, 0)
        self.linea_2 = Linea(self.direccion_prin,self.hitbox,1)
        self.linea_3 = Linea(self.direccion_sec, self.hitbox,2)
        self.lineas = [self.linea_1, self.linea_2, self.linea_3]

class Linea(QObject):
    def __init__(self, direccion, rio_hitbox, posicion):
        super().__init__()
        self.hitbox = QRect(rio_hitbox.x(), rio_hitbox.y()+ ((rio_hitbox.height() // 3) * posicion), rio_hitbox.width() ,rio_hitbox.height() // 3 )
        self.direccion = direccion
        if self.direccion == 1:
            self.aparicion = QPoint(self.hitbox.x() - 100, self.hitbox.y() + 10)
        else:
            self.aparicion = QPoint(self.hitbox.x() + 600, self.hitbox.y() + 10)
        
        self.tablones = []
        self.tick_cold_down = 0
        self.cold_down = random.choice([1, 2, 1.75, 1.4])
        self.timer_principal = QTimer()
        self.instanciar_timer_principal()

    def generar_tablon(self):
        if len(self.tablones) < 10:
            self.tablones.append(Tablon(self.aparicion, self.direccion))
        else:
            self.tablones[0].hitbox.moveTo(self.aparicion)
            self.tablones.append(self.tablones.pop(0))

    def instanciar_timer_principal(self):
        if self.tick_cold_down < self.cold_down:
            self.timer_cold_down_aparicion = QTimer()
            self.timer_cold_down_aparicion.setInterval(1000 * 0.1)
            self.timer_cold_down_aparicion.timeout.connect(self.timer_cold_down_aparicion_tick)
            self.timer_cold_down_aparicion.start()
        elif self.tick_cold_down >= self.cold_down:
            self.timer_cold_down_aparicion.stop()
            self.timer_principal = QTimer()
            self.timer_principal.setInterval(1000 * p.TIEMPO_TABLAS)
            self.timer_principal.timeout.connect(self.generar_tablon)
            self.subtick = 0

            self.timer_principal.start()

    def timer_cold_down_aparicion_tick(self):
        self.tick_cold_down += 0.05
        if self.tick_cold_down >= self.cold_down:
            self.instanciar_timer_principal()

class Tablon(QObject):
    def __init__(self, aparicion, direccion):
        super().__init__()
        self.islive = True
        self.aparicion = aparicion
        self.direccion = direccion
        self.hitbox = QRect(aparicion.x() , aparicion.y(), p.LARGO_TABLON , p.ANCHO_TABLON - 10)

    def avanzar(self, rana):
        if self.islive:
            if  self.direccion == 1 and self.hitbox.x() >= 600:
                self.hitbox.moveTo(self.aparicion.x(), -200)
            elif self.direccion == 0 and self.hitbox.x()< -100:
                self.hitbox.moveTo(self.aparicion.x(), -200)
            if self.direccion == 1:
                self.hitbox = self.hitbox.translated(5, 0)
                if rana.hitbox.intersects(self.hitbox):
                    rana.hitbox = rana.hitbox.translated(5,0)
            elif self.direccion == 0:
                self.hitbox = self.hitbox.translated(-5, 0)
                if rana.hitbox.intersects(self.hitbox):
                    rana.hitbox = rana.hitbox.translated(-5,0)
    def kill(self):
        self.islive = False
        self.hitbox.moveTo(0, -1000)
        
class Carretera(QObject):

    def __init__(self, x,y,largo,ancho):
        super().__init__()
        self.hitbox = QRect(x,y,largo,ancho)
        self.direccion_prin = random.choice([0,1])
        self.direccion_sec = 1 if self.direccion_prin == 0 else 0
        self.pista_1 = Pista(random.choice([0,1]), self.hitbox, 0)
        self.pista_2 = Pista(random.choice([0,1]),self.hitbox,1)
        self.pista_3 = Pista(random.choice([0,1]), self.hitbox,2)
        self.pistas = [self.pista_1, self.pista_2, self.pista_3]
 
class Pista(QObject):

    def __init__(self, direccion, carretera, posicion):
        super().__init__()
        self.hitbox = QRect(carretera.x(), carretera.y()+ ((carretera.height() // 3) * posicion), carretera.width() ,carretera.height() // 3 )
        self.direccion = direccion
        if self.direccion == 1:
            self.aparicion = QPoint(self.hitbox.x() - 100, self.hitbox.y() - 15)
        else:
            self.aparicion = QPoint(self.hitbox.x() + 600, self.hitbox.y() -15)

        self.autos = []
        self.tick_cold_down = 0
        self.cold_down = random.choice([1, 2, 3, 2.5])
        self.timer_principal = QTimer()
        self.instanciar_timer_principal()
        

    def generar_auto(self):
        if len(self.autos) < p.NUM_AUTOS:
            self.autos.append(Auto(self.aparicion, self.direccion))
        else:
            self.autos[0].hitbox.moveTo(self.aparicion.x(), self.aparicion.y())
            self.autos.append(self.autos.pop(0))
    
    def instanciar_timer_principal(self):
        if self.tick_cold_down < self.cold_down:
            self.timer_cold_down_aparicion = QTimer()
            self.timer_cold_down_aparicion.setInterval(1000 * 0.1)
            self.timer_cold_down_aparicion.timeout.connect(self.timer_cold_down_aparicion_tick)
            self.timer_cold_down_aparicion.start()
        elif self.tick_cold_down >= self.cold_down:
            self.timer_cold_down_aparicion.stop()
            self.timer_principal = QTimer()
            self.timer_principal.setInterval(1000 * p.TIEMPO_AUTOS)
            self.timer_principal.timeout.connect(self.generar_auto)
            self.subtick = 0

            self.timer_principal.start()

    def timer_cold_down_aparicion_tick(self):
        self.tick_cold_down += 0.05
        if self.tick_cold_down >= self.cold_down:
            self.instanciar_timer_principal()
        
class Auto(QObject):

    def __init__(self, aparicion, direccion):
        super().__init__()
        self.islive = True
        self.aparicion = aparicion
        self.direccion = direccion
        self.hitbox = QRect(aparicion.x(), aparicion.y(), p.LARGO_CAR - 5 , p.ANCHO_CAR)
    
    def avanzar(self):
        if self.islive:
            if  self.direccion == 1 and self.hitbox.x() >= 600:
                self.hitbox.moveTo(self.aparicion.x() -50 , -100)
            elif self.direccion == 0 and self.hitbox.x()< -100:
                self.hitbox.moveTo(self.aparicion.x() , -100)
            if self.direccion == 1:
                self.hitbox = self.hitbox.translated(10, 0)
            elif self.direccion == 0:
                self.hitbox = self.hitbox.translated(-10, 0)
        
class PowerUps(QObject):
    def __init__(self):
        self.tamano = (p.SIZE_OBJECTS, p.SIZE_OBJECTS)
        self.objetos = [VidaExtra(self.tamano), Monedas(self.tamano),
        Calaveras(self.tamano), Relojes(self.tamano)]
        self.objeto_activo = None
class VidaExtra(QObject):
    def __init__(self, tamano):
        super().__init__()
        self.hitbox = QRect(-10, -10000, *tamano)
    def accion(self, data):
        data['jugador'].vidas += 1
class Monedas(QObject):
    def __init__(self, tamano):
        super().__init__()
        self.hitbox = QRect(-10, -10000, *tamano)
    def accion(self, data):
        data['jugador'].monedas_ronda += p.CANTIDAD_MONEDAS
class Calaveras(QObject):
    def __init__(self, tamano):
        super().__init__()
        self.hitbox = QRect(-10, -1000, *tamano)
    def accion(self, data):
        velocidad, timer = data['velocidad_calavera']
        timer.stop()
        velocidad = velocidad * 1.05
        timer.setInterval(1000 * (1 / velocidad))
        timer.start()

class Relojes(QObject):
    def __init__(self, tamano):
        super().__init__()
        self.hitbox = QRect(-10, -10000, *tamano)
    def accion(self, data):
        data['jugador'].tiempo = data['jugador'].tiempo + int( 10 * (data['jugador'].tiempo / data['duracion_ronda']))
        