import pygame


class Ship():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/ship2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Atualiza a posição da espaçonave de acordo com a flag de
movimento"""
        if self.moving_right:
            self.rect.centerx += 1
