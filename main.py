import pygame
from player import Player
from enemy import Enemy
from menu import show_menu

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders Redux")

# Configuración del fondo
background = pygame.image.load('assets/images/background.jpg')

# Configuración de FPS
clock = pygame.time.Clock()
fps = 60

# Crear instancia del jugador
player = Player(screen_width // 2, screen_height - 70)

# Función para crear una nueva ola de enemigos
def create_enemies():
    enemies = []
    for i in range(5):
        for j in range(3):
            enemies.append(Enemy(100 + i * 100, 50 + j * 70))
    return enemies

# Crear la primera ola de enemigos
enemies = create_enemies()

# Función para mostrar el mensaje de victoria
def show_victory_message():
    font = pygame.font.SysFont(None, 55)
    text = font.render("¡Victoria! Presiona cualquier tecla para continuar", True, (255, 255, 255))
    screen.blit(text, (screen_width // 4, screen_height // 2))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                waiting = False

# Bucle principal del juego
def main_game():
    running = True
    player_health = 3  # Añadido: Sistema de salud para el jugador

    while running:
        # Limpiar la pantalla
        screen.fill((0, 0, 0))

        # Dibujar el fondo
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()

        # Movimiento del jugador
        player.move()
        player.draw(screen)

        # Movimiento y dibujo de enemigos
        if len(enemies) == 0:
            show_victory_message()
            enemies.extend(create_enemies())  # Crear una nueva ola de enemigos

        for enemy in enemies[:]:
            enemy.move()
            enemy.draw(screen)

            # Detección de colisiones entre balas y enemigos
            for bullet in player.bullets[:]:
                if enemy.rect.colliderect(bullet.rect):
                    enemies.remove(enemy)
                    player.bullets.remove(bullet)

            if enemy.rect.colliderect(player.rect):
                player_health -= 1  # Reducir la salud del jugador
                enemies.remove(enemy)  # Eliminar al enemigo que colisionó

                if player_health <= 0:
                    running = False  # Termina el juego si se acaba la salud

        # Actualizar la pantalla
        pygame.display.flip()
        clock.tick(fps)

    # Mostrar el menú al terminar el juego
    show_menu(screen, main_game)

# Mostrar menú y comenzar el juego
show_menu(screen, main_game)

pygame.quit()
