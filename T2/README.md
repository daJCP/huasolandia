# Tarea X: Nombre de la tarea :school_satchel:

## Consideraciones generales :octocat:

### Cosas implementadas y no implementadas :white_check_mark: :x:

* <Flujo del programa<sub>1</sub>>: Hecha completa
    *  <Personaje<sub>1.2</sub>>: Hecha completa 
    *  <Areas de juego<sub>1.2</sub>>: Hecha completa 
    *  <Mapa<sub>1.2</sub>>: Hecha completa 
    *  <Objetos especiales<sub>1.3</sub>>: Hecha completa 
    *  <Dificultad<sub>1.4</sub>>: Hecha completa 
    *  <Puntaje y vidas<sub>1.5</sub>>: Hecha completa 
* <Interfaz grafica<sub>2</sub>>: Hecha completa
    * <Modelacion del programa<sub>2.1</sub>>: Hecha completa 
    * <Ventanas<sub>2.2</sub>>: Hecha complpeta
        * <Inicio<sub>2.2.1</sub>>: Hecha completa
        * <Ranking<sub>2.2.1</sub>>: Hecha completa
        * <Juego<sub>2.2.1</sub>>: Hecha completa
        * <Post - Nivel<sub>2.2.1</sub>>: Hecha completa
* <Interaccion con el usuario<sub>3</sub>>: Hecha completa
   * <Movimiento<sub>3.1</sub>>: Hecha completa
   * <Salto<sub>3.2</sub>>: Hecha completa
   * <Click<sub>3.3</sub>>: Hecha completa
   * <Cheatcodes<sub>3.3</sub>>: Hecha completa
   * <Pausa<sub>3.4</sub>>: Hecha completa
* <Archivos<sub>4</sub>>: Hecha completa
   * <Sprites<sub>4.1</sub>>: Hecha completa
   * <Canciones<sub>4.2</sub>>: Hecha completa
   * <puntajes.txt<sub>4.3</sub>>: Hecha completa
   * <parametros.py<sub>4.4</sub>>: Hecha completa
* <Bonus<sub>5</sub>>: Hecha incompleta
   * <Ventana de Tienda<sub>5.1</sub>>: No completada
   * <Canciones<sub>5.2</sub>>: Hecha completa
   * <checkpoint<sub>5.3</sub>>: No completada

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:

Backend:
1. ```logica_juego.py``` en ```backend```
2. ```logica_inicio.py``` en ```backend```
3. ```logica_clases.py``` en ```backend```

Frontend:
1. ```ventana_ranking.py``` en ```frontend```
2. ```Ventana_ranking.ui``` en ```frontend```
3. ```Ventana_post_nivel.ui``` en ```frontend```
4.```ventana_post_nivel.py``` en ```frontend```
5.```Ventana_juego.ui``` en ```frontend```
6.```ventana_juego.py``` en ```frontend```
7. ```ventana_inicio.py``` en ```frontend```

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```choice```
2. ```os```: ```join```
3. ```pyqt5```: todo para el proceso de interfaces graficas

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```p_clases.py```: Contiene las clases que estructuran la logica del juego


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Supuse que el puntaje solo se guarda en el archivo ranking cuando pierdes, es decir, jugaste pero perdiste, no cuenta salirse
o cerrar el juego 

2. El volumen esta al maximo si es una molestia al momento de jugar recomiendo desactivarla.

------
