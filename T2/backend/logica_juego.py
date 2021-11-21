from PyQt5.QtCore import QObject, QPoint, QTimer, Qt, pyqtSignal, QRect

from PyQt5.QtWidgets import QAbstractItemView, QBoxLayout

import parametros as p

from p_clases import (
    Jugador, Rio, Carretera, Rana, Pasto, PowerUps
)

import random 

class LogicaJuego(QObject):
    
    senal_timer_actualizar_nivel= pyqtSignal(str)
    senal_datos_timer = pyqtSignal(dict)
    senal_pasar_etapa = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.ronda = 1
        self.usuario = None
        self.power_up = PowerUps()

        self.velocidad_autos = p.VELOCIDAD_AUTOS
        self.velocidad_troncos = p.VELOCIDAD_TRONCOS
        self.duracion_ronda = p.DURACION_RONDA_INICIAL

        self.velocidad_calavera = None

        self.input_direccion = None
        self.choco = False

    def setear_usuario(self, usuario):
        self.usuario = usuario
        self.jugador = Jugador(usuario)
    
    def iniciar_ronda(self, ronda):
        if self.ronda != 1:
            self.duracion_ronda = int(self.duracion_ronda * p.PONDERADOR_DIFICULTAD)
            self.velocidad_troncos = self.velocidad_troncos * (2/(1+ p.PONDERADOR_DIFICULTAD))
            self.velocidad_autos = self.velocidad_autos * (2/(1+ p.PONDERADOR_DIFICULTAD))
        self.velocidad_calavera = self.velocidad_troncos
        self.puntaje_ronda = 0
        self.jugador.monedas_ronda = 0
        self.instanciar_timer_principal()
        self.isGanador = False
        self.timer_principal.start()
        self.timer_tiempo.start()
        self.timer_velocidad_troncos.start()
        self.timer_velocidad_autos.start()
        self.timer_velocidad_troncos.start()
        self.timer_objetos.start()
    #ticks del juego
    def instanciar_timer_principal(self):
        self.rana = Rana()
        self.carretera1 = Carretera(*p.CARRETERA_1_GEOMETRY)
        self.carretera2 = Carretera(*p.CARRETERA_2_GEOMETRY)
        self.rio = Rio(*p.RIO_GEOMETRY)
        self.pasto = Pasto(*p.PASTO_WIN_GEOMETRY)

        self.timer_principal = QTimer()
        self.timer_tiempo = QTimer()
        self.timer_principal.setInterval(1000 * p.TIMER_PRINCIPAL)
        self.timer_tiempo.setInterval(1000)
        self.timer_principal.timeout.connect(self.timer_principal_tick)
        self.timer_tiempo.timeout.connect(self.reloj)
        self.subtick = 0
        self.segundo_anterior = None
        self.jugador.tiempo = self.duracion_ronda
        self.isPaused = -1

        self.timer_velocidad_autos = QTimer()
        self.timer_velocidad_autos.setInterval(1000 * (1 / self.velocidad_autos))
        self.timer_velocidad_autos.timeout.connect(self.timer_velocidad_autos_tick)

        self.timer_velocidad_troncos = QTimer()
        self.timer_velocidad_troncos.setInterval(1000 * (1 / self.velocidad_troncos))
        self.timer_velocidad_troncos.timeout.connect(self.timer_velocidad_troncos_tick)
    
        self.timer_objetos = QTimer()
        self.timer_objetos.setInterval(1000 * p.TIEMPO_OBJETO)
        self.timer_objetos.timeout.connect(self.timer_objetos_tick)

    def timer_objetos_tick(self):
        if self.power_up.objeto_activo == None:
            self.power_up.objeto_activo = random.choice(self.power_up.objetos)
            a = 1
            while a == 1:
                x_random = random.randint(0, 600 - p.SIZE_OBJECTS )
                y_random = random.randint(0, 800 - p.SIZE_OBJECTS ) 
                self.power_up.objeto_activo.hitbox.moveTo(x_random, y_random)
                if not self.power_up.objeto_activo.hitbox.intersects(self.rio.hitbox):
                    if not self.power_up.objeto_activo.hitbox.intersects(self.pasto.hitbox):
                        a = 0
        else:
            self.power_up.objeto_activo.hitbox.moveTo(0, -100)
            self.power_up.objeto_activo = random.choice(self.power_up.objetos)
            a = 1
            while a == 1:
                x_random = random.randint(0, 600 - p.SIZE_OBJECTS ) 
                y_random = random.randint(0, 800 - p.SIZE_OBJECTS ) 
                self.power_up.objeto_activo.hitbox.moveTo(x_random, y_random)
                if not self.power_up.objeto_activo.hitbox.intersects(self.rio.hitbox):
                    if not self.power_up.objeto_activo.hitbox.intersects(self.pasto.hitbox):
                        a = 0

    def timer_velocidad_troncos_tick(self):
        for linea in self.rio.lineas:
            for tablon in linea.tablones:
                tablon.avanzar(self.rana)
    
    def timer_velocidad_autos_tick(self):
        for pista in self.carretera1.pistas:
            for auto in pista.autos:
                auto.avanzar()
        for pista in self.carretera2.pistas:
            for auto in pista.autos:
                auto.avanzar()

    def reloj(self):
        self.jugador.tiempo -= 1
        if self.jugador.tiempo == 0:
            self.detener_juego()
    
    def iniciar_juego(self):
        self.ronda = 1
        self.iniciar_ronda(self.ronda)
    
    def detener_juego(self):
        self.timer_principal.stop()
        self.timer_tiempo.stop()
        self.timer_velocidad_troncos.stop()
        self.timer_velocidad_autos.stop()
        self.timer_velocidad_troncos.stop()
        self.timer_objetos.stop()
        # #actualizamos data
        self.puntaje_ronda = (self.jugador.vidas * 100 + self.jugador.tiempo * 50) * self.ronda
        self.jugador.monedas += self.jugador.monedas_ronda
        self.jugador.puntaje += self.puntaje_ronda
        self.data = {
            'usuario': self.usuario,
            'jugador': self.jugador,
            'new_pos': self.rana.hitbox,
            'tiempo': self.jugador.tiempo,
            'rana_dir': self.rana.direccion,
            'input_movimiento': self.input_direccion,
            'choco':(self.choco, self.rana.hitbox),
            'rana': self.rana,
            'rio': self.rio,
            'ronda': self.ronda,
            'isGanador': self.isGanador,
            'puntaje_ronda': self.puntaje_ronda,
            'monedas_ronda': self.jugador.monedas_ronda
        }
        if self.isGanador == False:
            self.guardar_ranking()
        # #mandamos la señal
        self.senal_pasar_etapa.emit(self.data)
    
    def pausar(self, num):
        self.isPaused = self.isPaused * num
        if self.isPaused == 1:
            self.timer_principal.stop()
            self.timer_tiempo.stop()
            self.timer_velocidad_troncos.stop()
            self.timer_velocidad_autos.stop()
            self.timer_velocidad_troncos.stop()
            self.timer_objetos.stop()
            for pista in self.carretera1.pistas:
                pista.timer_principal.stop()
            for pista in self.carretera2.pistas:
                pista.timer_principal.stop()
            for pista in self.rio.lineas:
                pista.timer_principal.stop()
        else:
            self.timer_principal.start()
            self.timer_tiempo.start()
            self.timer_velocidad_troncos.start()
            self.timer_velocidad_autos.start()
            self.timer_velocidad_troncos.start()
            for pista in self.carretera1.pistas:
                pista.timer_principal.start()
            for pista in self.carretera2.pistas:
                pista.timer_principal.start()
            for pista in self.rio.lineas:
                pista.timer_principal.start()

    def reanudar_juego(self):
        self.timer_principal.start()
        self.timer_tiempo.start()
        self.timer_velocidad_troncos.start()
        self.timer_velocidad_autos.start()
        self.timer_velocidad_troncos.start()
        self.timer_objetos.start()
    
    def salir_juego(self):
        self.timer_principal.stop()
        self.timer_tiempo.stop()
        self.timer_velocidad_troncos.stop()
        self.timer_velocidad_autos.stop()
        self.timer_velocidad_troncos.stop()
        self.timer_objetos.stop()
    
    def timer_principal_tick(self):
        self.subtick += (0.1 * 1000)
        self.segundo = self.subtick // (10000 * 100)
        if self.input_direccion != None and self.rana.isjumping == False:
            if self.input_direccion == 'Jump':
                if self.rana.cold_down == False:
                    self.rana.cold_down = True
                    self.rana.jump()
            elif self.input_direccion == 'P':
                self.pausar(-1)
            elif self.input_direccion == 'vidas':
                self.jugador.vidas += p.VIDAS_TRAMPA
            elif self.input_direccion == 'nivel':
                self.isGanador = True
                self.detener_juego()
            else:
                self.rana.cambiar_direccion(self.input_direccion)
    
        #revisar colision con autos
        self.choco = self.colision()
        self.data = {
            'new_pos': self.rana.hitbox,
            'jugador': self.jugador,
            'tiempo': self.jugador.tiempo,
            'rana_dir': self.rana.direccion,
            'input_movimiento': self.input_direccion,
            'carretera1': self.carretera1,
            'carretera2': self.carretera2,
            'choco':(self.choco, self.rana.hitbox),
            'rana': self.rana,
            'rio': self.rio,
            'ronda': self.ronda,
            'isGanador': self.isGanador,
            'power_ups': self.power_up,
            'duracion_ronda': self.duracion_ronda,
            'velocidad_calavera': (self.velocidad_calavera, self.timer_velocidad_troncos),
            'puntaje_ronda': self.puntaje_ronda,
            'monedas_ronda': self.jugador.monedas_ronda
        }

        
        self.enviar_dato_timer(
            self.data
        )

        self.input_direccion = None
        self.segundo_anterior = self.segundo

        if self.jugador.vidas < 0:
            self.detener_juego()

        self.ganador()
    
    def iniciar_nueva_ronda(self, event):
        self.ronda += 1
        self.iniciar_ronda(self.ronda)

    def ganador(self):
        if self.rana.hitbox.intersects(self.pasto.hitbox):
            self.isGanador = True
            self.detener_juego()

    def guardar_ranking(self):
        with open('ranking.txt', 'a') as file:
            file.write(f'{self.jugador.usuario}, {self.jugador.puntaje}\n')

    def colision(self):
        for pista in self.carretera1.pistas:
            for auto in pista.autos:
                if auto.hitbox.intersects(self.rana.hitbox):
                    self.rana.volver(self.jugador)
                    return True
        for pista in self.carretera2.pistas:
            for auto in pista.autos:
                if auto.hitbox.intersects(self.rana.hitbox):
                    self.rana.volver(self.jugador)
                    return True
        esta_en_tronco = False
        for lineas in self.rio.lineas:
            for tablon in lineas.tablones:
                if tablon.hitbox.intersects(self.rana.hitbox):
                    esta_en_tronco = True
        self.rana.istablon = esta_en_tronco            
        la_1 = self.rana.istablon == False
        if self.rana.hitbox.intersects(self.rio.hitbox) and self.rana.isjumping == False and la_1:
            self.rana.volver(self.jugador)
        if self.rana.hitbox.x() < - 30 or self.rana.hitbox.x() > 610:
            self.rana.volver(self.jugador)
        if self.power_up.objeto_activo != None:
            if self.rana.hitbox.intersected(self.power_up.objeto_activo.hitbox):
                self.power_up.objeto_activo.accion(self.data)
                self.power_up.objeto_activo.hitbox.moveTo(0,-1000)

    def movimiento_direccion(self, event):
        if event == None:
            self.input_direccion = None
        else:
            self.input_direccion = event

    def enviar_dato_timer(self, dict):
        self.senal_datos_timer.emit(dict)

    