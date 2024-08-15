# Juego-Python: Space Invaders Redux

## Descripción
Space Invaders Redux es un juego de disparos en 2D creado con PyGame. Controlas una nave espacial que debe defenderse de oleadas de enemigos alienígenas. A medida que derrotas a los enemigos, nuevos aparecen en pantalla. El juego cuenta con un sistema de menús para iniciar el juego o salir, junto con una detección de colisiones que permite al jugador disparar y destruir enemigos.

## Instalación
1. Clona este repositorio en tu máquina local.
'''
    git remote add origin https://github.com/JorgePertuzM/Juego-Python-Space-Invaders-Redux.git
'''
2. Asegúrate de tener Python instalado.
3. Instala la librería `pygame` utilizando el siguiente comando:
'''
    pip install pygame
'''


## Estructura LUA 
SpaceInvadersRedux/
│
├── main.py               -- Archivo principal que inicia y controla el juego
├── player.py             -- Clase para manejar la nave espacial del jugador
├── enemy.py              -- Clase para manejar los enemigos
├── bullet.py             -- Clase para manejar los proyectiles del jugador
├── menu.py               -- Funciones para mostrar y manejar el menú principal
├── README.md             -- Archivo de documentación con instrucciones y descripción del proyecto
│
├── assets/               -- Directorio para almacenar todos los recursos del juego
│   ├── images/           -- Imágenes del juego (nave, enemigos, fondo, etc.)
│   │   ├── spaceship.png
│   │   ├── enemy.png
│   │   └── background.jpg
│   ├── sounds/           -- Efectos de sonido y música de fondo
│   │   ├── shoot.wav
│   │   ├── explosion.wav
│   │   └── background.mp3
│   └── fonts/            -- Fuentes personalizadas (opcional)
│       └── arcade.ttf
│
└── config/               -- Directorio opcional para configuraciones adicionales
    └── settings.py       -- Configuración de variables globales (tamaño de pantalla, FPS, etc.)



## Ejecución
Para ejecutar el juego, navega al directorio del proyecto y ejecuta el siguiente comando:
'''
    python main.py
'''


## Controles
- **Flecha Izquierda:** Mover la nave a la izquierda.
- **Flecha Derecha:** Mover la nave a la derecha.
- **Enter:** Seleccionar opciones en el menú.
- **Barra Espaciadora:** La nave dispara una bala.

## Contribuciones
Este proyecto es de código abierto y se aceptan contribuciones. Si encuentras algún error o tienes alguna mejora, no dudes en abrir un issue o enviar un pull request.
