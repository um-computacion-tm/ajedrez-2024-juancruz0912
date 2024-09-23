# Juego del Ajedrez

## Funcionalidad del Juego

El juego se desarrolla de la siguiente manera:

1. **Ingreso de Nombres:**
   Al iniciar el juego, cada jugador debe ingresar su nombre.

2. **Movimiento de Piezas:**
   Durante su turno, cada jugador puede mover una de sus piezas. El formato para ingresar el movimiento es el siguiente:
   - **Tipo de Pieza:** El nombre de la pieza a mover, por ejemplo, 'Peon 1'.
   - **Columna y Fila:** El número entero que representa la fila en la que se encuentra la pieza y la letra que representa la columna de destino, por ejemplo, 'a2' (fila 2, columna a)

   Por ejemplo, para mover un peón a la fila 3 y columna 'D', el jugador debe ingresar: 
   - Peon 4
   - d3
   
    En cualquier caso en el que se quiera elegir otra ficha, se ingresa **0 (cero)** en vez de ingresar la fila y la columna

3. **Validación de Movimiento:**
El juego valida que el movimiento sea legal según las reglas del ajedrez. Si el movimiento es inválido, se solicitará al jugador que ingrese un nuevo movimiento.

4. **Finalización del Juego:**
El juego continúa hasta que se detecta un jaque mate o uno de los dos jugadores se quede sin fichas o en el caso en el que los jugadores ya no quieran jugar se ingresa **0 (cero)** en vez de ingresar la proxima pieza a mover

## Como empezar a Jugar
1. Tener instalado docker en el dispositivo
 en caso de no tenerlo, ejecutar el siguiente comando:
```
 $ sudo apt install docker
```
2. Luego, ejecutar los siguientes comandos:
 ```
 2. Crear imagen de Docker
$ docker buildx build -t ajedrez /ruta/al/directorio

3. Ejecutar tests y jugar.
$ docker run -i ajedrez
 ```

# Pruebas
### CircleCI 
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-juancruz0912/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-juancruz0912/tree/main)

### Maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/5d63cfc20b1b40812bfd/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-juancruz0912/maintainability)

### Test Coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/5d63cfc20b1b40812bfd/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-juancruz0912/test_coverage)

## Trabajado por
- **Alumno:**
 Juan Cruz Rupcic
- **Legajo:** 
 63410

