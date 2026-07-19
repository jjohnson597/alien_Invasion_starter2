import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from alien import Alien
    
class AlienFleet:
    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.aliens = pygame.sprite.Group()
        self.alien_direction = self.settings.alien_direction
        self.alien_drop_speed = self.settings.alien_drop_speed

        self.create_fleet()

    def create_fleet(self):
        alien_width = self.settings.alien_width
        screen_width = self.settings.screen_width

        fleet_width = self.calculate_fleet_size(alien_width, screen_width)

        half_screen = self.settings.screen_width // 2
        fleet_horizontal_spacing = (fleet_width * alien_width)
        x_offset = (screen_width - fleet_horizontal_spacing) // 2

        for col in range(fleet_width):
            current_x = x_offset + (col * alien_width)
            self._create_alien(self, current_x, 10)


    def calculate_fleet_size(self, alien_width, screen_width):
        fleet_width = screen_width // alien_width
        if fleet_width % 2 == 0:
            fleet_width -= 1
        else:
            fleet_width -= 2

        return fleet_width

    def _create_alien(self, current_x, current_y):
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)

    def draw(self):
        alien: "Alien"
        for alien in self.fleet:
            alien.draw_alien()

        