import pygame

class Bullet:
    def __init__(self, x, y):
        self.image = pygame.Surface((5, 20))
        self.image.fill((255, 255, 255))  # Color blanco para la bala
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = -10  # La bala se moverá hacia arriba

    def move(self):
        self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def is_off_screen(self):
        return self.rect.y < 0
