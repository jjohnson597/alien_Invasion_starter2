import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Alien(Sprite):
    def __init__(self, game: 'AlienInvasion', x: float, y: float):
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings
        self.boundaries = game.screen.get_rect()

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, (self.settings.alien_width, self.settings.alien_height))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        temp_speed = self.settings.alien_speed
        self.x += temp_speed
        self.rect.x += temp_speed

    def draw_alien(self):
        self.screen.blit(self.image, self.rect)
        
