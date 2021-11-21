import sys

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtMultimedia
from frontend.ventana_ranking import VentanaRanking
import parametros as p
from backend.logica_inicio import LogicaInicio
from backend.logica_juego import LogicaJuego
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_post_nivel import VenPost



if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])

    musica_file = p.RUTA_MUSICA

    musica = QtMultimedia.QSound(musica_file)
    musica.loops()
    musica.play()

    # Instanciación de ventanasw
    tamano_ventana = QRect(*p.WINDOW_SIZE)
    ventana_inicio = VentanaInicio(tamano_ventana)
    ventana_juego = VentanaJuego()
    ventana_post = VenPost()
    ventana_ranking = VentanaRanking()

    # Instanciación de lógica
    logica_inicio = LogicaInicio()
    logica_juego = LogicaJuego()
    # Conexiones de señales 

    # Ventana Inicio
    logica_inicio.senal_respuesta_validacion.connect(
        ventana_inicio.recibir_validacion
    )

    logica_inicio.senal_abrir_juego.connect(
        ventana_juego.mostrar_ventana
    )

    ventana_inicio.senal_enviar_login.connect(
        logica_inicio.comprobar_nombre
    )

    ventana_juego.senal_enviar_usuario.connect(
        logica_juego.setear_usuario
    )

    # Ventana Juego

    ventana_juego.senal_iniciar_juego.connect(
        logica_juego.iniciar_juego
    )

    ventana_juego.senal_tecla.connect(
        logica_juego.movimiento_direccion
    )

    logica_juego.senal_datos_timer.connect(
        ventana_juego.actualizar_timer
    )

    logica_juego.senal_pasar_etapa.connect(
        ventana_juego.post_nivel
    )
    
    ventana_juego.senal_pausa.connect(
        logica_juego.pausar
    )

    ventana_post.senal_siguiente_ronda.connect(
        logica_juego.iniciar_nueva_ronda
    )

    ventana_juego.senal_inicio_menu.connect(
        ventana_inicio.mostrar
    )

    ventana_juego.detener_game.connect(
        logica_juego.salir_juego
    )

    ventana_juego.senal_post_nivel.connect(
        ventana_post.datos
    )

    ventana_post.senal_volver_menu.connect(
        ventana_inicio.mostrar
    )

    ventana_inicio.senal_ventana_ranking.connect(
        ventana_ranking.mostrar
    )

    ventana_ranking.senal_volver.connect(
        ventana_inicio.mostrar
    )

    ventana_inicio.mostrar()
    app.exec()
