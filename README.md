# Juego-Python: Space Invaders Redux

## Descripción
Space Invaders Redux es un juego de disparos en 2D creado con PyGame. Controlas una nave espacial que debe defenderse de oleadas de enemigos alienígenas. A medida que derrotas a los enemigos, nuevos aparecen en pantalla. El juego cuenta con un sistema de menús para iniciar el juego o salir, junto con una detección de colisiones que permite al jugador disparar y destruir enemigos.

## Instalación
1. Clona este repositorio en tu máquina local.
 ```bash
https://github.com/JorgePertuzM/Juego-Python-Space-Invaders-Redux.git
```

3. Asegúrate de tener Python instalado.
4. Instala la librería `pygame` utilizando el siguiente comando:
 ```bash
pip install pygame
```
## Estructura LUA 
 ```bash
SpaceInvadersRedux/
│
├── main.py
├── player.py
├── enemy.py
├── bullet.py
├── menu.py
├── README.md
│
├── assets/
│   ├── images/
│   │   ├── spaceship.png
│   │   ├── enemy.png
│   │   └── background.jpg
│   ├── sounds/
│   │   ├── shoot.wav
│   │   ├── explosion.wav
│   │   └── background.mp3
│   └── fonts/
│       └── arcade.ttf
│
└── config/
    └── settings.py
```


## Ejecución
Para ejecutar el juego, navega al directorio del proyecto y ejecuta el siguiente comando:
python main.py


## Controles
- **Flecha Izquierda:** Mover la nave a la izquierda.
- **Flecha Derecha:** Mover la nave a la derecha.
- **Enter:** Seleccionar opciones en el menú.
- **Barra Espaciadora:** La nave dispara una bala.
- **Flecha Arriba/Abajo:** Navegar por las opciones del menú.

## Funcionalidades
- **Menú principal:** Navega entre opciones para iniciar el juego o salir.
- **Sistema de disparo:** El jugador puede disparar balas para destruir a los enemigos.
- **Oleadas de enemigos:** Los enemigos aparecen en oleadas, y el jugador debe eliminarlos todos para avanzar.
- **Detección de colisiones:** Colisiones entre balas y enemigos, así como entre enemigos y la nave del jugador.
- **Mensaje de victoria:** Al derrotar a todos los enemigos, aparece un mensaje de victoria.

## Mejoras futuras
- **Puntuación:** Añadir un sistema de puntuación para registrar cuántos enemigos han sido destruidos.
- **Niveles de dificultad:** Implementar diferentes niveles de dificultad que alteren la velocidad de los enemigos o la cantidad de balas disponibles.
- **Nuevas armas:** Introducir diferentes tipos de armas y power-ups para el jugador.

## Contribuciones
Este proyecto es de código abierto y se aceptan contribuciones. Si encuentras algún error o tienes alguna mejora, no dudes en abrir un issue o enviar un pull request.
