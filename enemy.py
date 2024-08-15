import pygame

class Enemy:
    def __init__(self, x, y):
        # Cargar y escalar la imagen del enemigo
        self.image = pygame.image.load('assets/images/enemy.png')
        self.image = pygame.transform.scale(self.image, (50, 50))  # Cambia el tamaño aquí
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 2
        self.direction = 1

    def move(self):
        self.rect.x += self.speed * self.direction
        if self.rect.left <= 0 or self.rect.right >= 800:
            self.direction *= -1
            self.rect.y += 40  # Bajar un nivel al cambiar de dirección

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)
