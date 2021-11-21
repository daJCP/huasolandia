
from PyQt5.QtCore import QObject, pyqtSignal

import parametros as p

class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(tuple)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_nombre(self, nombre_usuario):
        usuario = nombre_usuario.strip()
        is_alphanumeric = usuario.isalnum()
        worked = False
        if (p.MIN_CARACTERES <= len(usuario) <= p.MAX_CARACTERES) and is_alphanumeric == True:
            self.senal_abrir_juego.emit(usuario)
            worked = True
        self.senal_respuesta_validacion.emit((usuario, worked))
