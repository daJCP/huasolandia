import os
# Aqui se encuentras los parametros del juego

WINDOW_SIZE = (600, 200, 300, 500)

MIN_CARACTERES = 3

MAX_CARACTERES = 10

DURACION_RONDA_INICIAL = 120 #segundos

SIZE_FROG = 30

PIXELES_SALTO = 4

MOVIMIENTO = 15

TIMER_PRINCIPAL = 0.25

### pag4
VIDAS_INICIO = 3

POS_INICIO = (260, 760)

CARRETERA_1_GEOMETRY = (0,100,600,150)

CARRETERA_2_GEOMETRY = (0,550,600,150)

RIO_GEOMETRY = (0, 295, 600, 190)

PASTO_WIN_GEOMETRY = (0,0,600,80)

TIMER_PRINCIPAL = 0.001

#autos
LARGO_CAR = 100

ANCHO_CAR = 50

TIEMPO_AUTOS = 2

VELOCIDAD_AUTOS = 25

NUM_AUTOS = 2

#tablones

TIEMPO_TABLAS = 4

ANCHO_TABLON = 40

NUM_TABLONES = 10

LARGO_TABLON = 100

VELOCIDAD_TRONCOS = 20

#objetos
SIZE_OBJECTS = 40
CANTIDAD_MONEDAS = 5
TIEMPO_OBJETO = 10

#controles
TECLA_ARRIBA = 'w'
TECLA_ABAJO = 's'
TECLA_DERECHA = 'd'
TECLA_IZQUIERDA = 'a'
TECLA_SALTAR = ' '
TECLA_PAUSAR = 'p'

#cheat
VIDAS_TRAMPA = 10

#dificultad

PONDERADOR_DIFICULTAD = 0.85

#Rutas
RUTA_MUSICA = os.path.join('canciones','musica.wav')

RUTA_VIDA = os.path.join('sprites','Objetos','Corazon.png')

RUTA_MONEDA = os.path.join('sprites','Objetos','Moneda.png')

RUTA_RELOJ = os.path.join('sprites','Objetos','Reloj.png')

RUTA_CALAVERA = os.path.join('sprites','Objetos','Calavera.png')

RUTA_UI_VENTANA_POST = os.path.join('frontend','Ventana_post_nivel.ui')

RUTA_UI_VENTANA_JUEGO = os.path.join('frontend','Ventana_juego.ui')

RUTA_UI_VENTANA_RANKING = os.path.join('frontend','Ventana_ranking.ui')

RUTA_ICONO = os.path.join('sprites','Personajes','Rojo\down_1.png')

RUTA_ICONO = os.path.join('sprites','Personajes','Rojo','down_1.png')

RUTA_LOGO = os.path.join('sprites','Logo.png')

RUTA_PASTO = os.path.join('sprites','Mapa','Areas','pasto.png')

RUTA_SKIN_CARRETERA = os.path.join('sprites','Mapa','Areas','carretera.png')

RUTA_SKIN_RIO = os.path.join('sprites','Mapa','Areas','Rio.png')

RUTA_SKIN_RANA_STILL= os.path.join('sprites','Personajes','Verde','still.png')

#TABLONES
RUTA_TABLONES = os.path.join('sprites','Mapa','elementos','Tronco.png')

#RANA LEFT
RUTA_SKIN_RANA_LEFT_1 = os.path.join('sprites','Personajes','Verde','left_1.png')
RUTA_SKIN_RANA_LEFT_2 = os.path.join('sprites','Personajes','Verde','left_2.png')
RUTA_SKIN_RANA_LEFT_3 = os.path.join('sprites','Personajes','Verde','left_3.png')

#RANA RIGHT
RUTA_SKIN_RANA_RIGHT_1 = os.path.join('sprites','Personajes','Verde','Right_1.png')
RUTA_SKIN_RANA_RIGHT_2 = os.path.join('sprites','Personajes','Verde','Right_2.png')
RUTA_SKIN_RANA_RIGHT_3 = os.path.join('sprites','Personajes','Verde','Right_3.png')

#Rana up
RUTA_SKIN_RANA_UP_1 = os.path.join('sprites','Personajes','Verde','Arriba_1.png')
RUTA_SKIN_RANA_UP_2 = os.path.join('sprites','Personajes','Verde','Arriba_2.png')
RUTA_SKIN_RANA_UP_3 = os.path.join('sprites','Personajes','Verde','Arriba_3.png')

#rana down
RUTA_SKIN_RANA_DOWN_1 = os.path.join('sprites','Personajes','Verde','down_1.png')
RUTA_SKIN_RANA_DOWN_2 = os.path.join('sprites','Personajes','Verde','down_2.png')
RUTA_SKIN_RANA_DOWN_3 = os.path.join('sprites','Personajes','Verde','down_3.png')

#rana jump
RUTA_SKIN_JUMP_1 = os.path.join('sprites','Personajes','Verde','jump_1.png')
RUTA_SKIN_JUMP_2 = os.path.join('sprites','Personajes','Verde','jump_2.png')
RUTA_SKIN_JUMP_3 = os.path.join('sprites','Personajes','Verde','jump_3.png')

#autos
RUTA_AUTO_AMARILLO_LEFT = os.path.join('sprites','Mapa','Autos','Amarillo_left.png')
RUTA_AUTO_AMARILLO_RIGHT = os.path.join('sprites','Mapa','Autos','Amarillo_right.png')

RUTA_AUTO_AZUL_LEFT = os.path.join('sprites','Mapa','Autos','Azul_left.png')
RUTA_AUTO_AZUL_RIGHT = os.path.join('sprites\Mapa\Autos\Azul_right.png')

RUTA_AUTO_BLANCO_LEFT = os.path.join('sprites','Mapa','Autos','Blanco_left.png')
RUTA_AUTO_BLANCO_RIGHT = os.path.join('sprites','Mapa','Autos','Blanco_right.png')

RUTA_AUTO_MORADO_LEFT = os.path.join('sprites','Mapa','Autos','morado_left.png')
RUTA_AUTO_MORADO_RIGHT = os.path.join('sprites','Mapa','Autos\morado_right.png')

RUTA_AUTO_NEGRO_LEFT = os.path.join('sprites','Mapa','Autos','_Negro_left.png')
RUTA_AUTO_NEGRO_RIGHT = os.path.join('sprites','Mapa','Autos','_Negro_right.png')

RUTA_AUTO_PLATA_LEFT = os.path.join('sprites','Mapa','Autos','plata_left.png')
RUTA_AUTO_PLATA_RIGHT = os.path.join('sprites','Mapa','Autos','plata_right.png')

RUTA_AUTO_ROJO_LEFT = os.path.join('sprites','Mapa','Autos','Rojo_left.png')
RUTA_AUTO_ROJO_RIGHT = os.path.join('sprites','Mapa','Autos','Rojo_right.png')

# Estilo
stylesheet_boton = """QPushButton {
    background-color: #fd9500;
    border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: beige;
    font: bold 14px;
    min-width: 4em;
    padding: 6px;
    color: white;
}
QPushButton:pressed {
    background-color: rgb(64, 58, 4);
    border-style: inset;
}"""
