import pygame
from bullet import Bullet

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load('assets/images/spaceship.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5
        self.bullets = []

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.bullets.append(bullet)

    def update_bullets(self, screen):
        for bullet in self.bullets[:]:
            bullet.move()
            if bullet.is_off_screen():
                self.bullets.remove(bullet)
            else:
                bullet.draw(screen)

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)
        self.update_bullets(surface)
