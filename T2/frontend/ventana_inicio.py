from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout,
)

import parametros as p


class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(str)
    senal_ventana_ranking = pyqtSignal()
    

    def __init__(self, tamano_ventana):
        super().__init__()
        self.init_gui(tamano_ventana)

    def init_gui(self, tamano_ventana):
        self.setWindowIcon(QIcon(p.RUTA_ICONO))

        # COMPLETAR
        self.setGeometry(tamano_ventana)
        self.setMaximumSize(p.WINDOW_SIZE[2], p.WINDOW_SIZE[3])
    
        self.usuario_label = QLabel('Escriba su nombre de usuario:', self)
        self.usuario_form = QLineEdit('',self)

        usuario_box = QVBoxLayout() #usuario
        usuario_box.addWidget(self.usuario_label)
        usuario_box.addWidget(self.usuario_form)

        self.logo_label = QLabel(self)
        self.logo_label.setGeometry(0, 0, 400, 400)
        self.logo_label.setMaximumSize(400,400)
        logo = QPixmap(p.RUTA_LOGO)
        self.logo_label.setPixmap(logo)
        self.logo_label.setScaledContents(True)
        
        self.ingresar_button = QPushButton('Iniciar', self)
        self.ingresar_button.clicked.connect(self.enviar_login)

        self.ranking_button = QPushButton('Ranking', self)
        self.ranking_button.clicked.connect(self.ventana_ranking)

        panel_box = QVBoxLayout()
        panel_box.addLayout(usuario_box)
        panel_box.addWidget(self.ingresar_button)
        panel_box.addWidget(self.ranking_button)

        ventana_vbox = QVBoxLayout()
        ventana_vbox.addStretch(1)
        ventana_vbox.addWidget(self.logo_label)
        ventana_vbox.addStretch(1)
        ventana_vbox.addLayout(panel_box)
        ventana_vbox.addStretch(1)

        self.setLayout(ventana_vbox)

        self.agregar_estilo()

    def ventana_ranking(self):
        self.hide()
        self.senal_ventana_ranking.emit()

    def enviar_login(self):
        usuario = (self.usuario_form.text())
        self.senal_enviar_login.emit(usuario)

    def agregar_estilo(self):
        self.setStyleSheet("background-color: #2dbd6e")
        self.usuario_form.setStyleSheet("background-color: #000000;"
                                        "border-radius: 5px;"
                                        "color: white")
        self.ingresar_button.setStyleSheet(p.stylesheet_boton)
        self.ranking_button.setStyleSheet(p.stylesheet_boton)

    def recibir_validacion(self, tupla_respuesta):
        if tupla_respuesta[1]:
            self.ocultar()
        else:
            self.usuario_form.setText("")
            self.usuario_form.setPlaceholderText("Usuario inválido!")

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.hide()
