import pygame
import sys

def show_menu(screen, start_game):
    # Fuente y colores
    font = pygame.font.Font(None, 74)
    text_color = (255, 255, 255)
    bg_color = (0, 0, 0)

    # Opciones del menú
    options = ["Start Game", "Exit"]
    selected = 0

    while True:
        screen.fill(bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                if event.key == pygame.K_RETURN:
                    if selected == 0:
                        start_game()
                    elif selected == 1:
                        pygame.quit()
                        sys.exit()

        # Mostrar las opciones del menú
        for i, option in enumerate(options):
            color = text_color if i == selected else (100, 100, 100)
            text = font.render(option, True, color)
            text_rect = text.get_rect(center=(400, 300 + i * 100))
            screen.blit(text, text_rect)

        pygame.display.flip()
