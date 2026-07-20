import pygame
from typing import TYPE_CHECKING

from alien import Alien

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class AlienFleet:
    def __init__(self, game: "AlienInvasion"):
        self.game = game
        self.settings = game.settings

        self.aliens = pygame.sprite.Group()

        self.alien_direction = self.settings.alien_direction
        self.alien_drop_speed = self.settings.alien_drop_speed

        self.create_fleet()

    def create_fleet(self):
        """Create the full fleet of aliens."""
        alien_width = self.settings.alien_width
        alien_height = self.settings.alien_height
        screen_width = self.settings.screen_width
        screen_height = self.settings.screen_height

        fleet_width, fleet_height = self.calculate_fleet_size(
            alien_width,
            alien_height,
            screen_width,
            screen_height
        )

        x_offset, y_offset = self.calculate_fleet_offsets(
            alien_width,
            alien_height,
            screen_width,
            fleet_width,
            fleet_height
        )

        for row in range(fleet_height):
            for col in range(fleet_width):
                if row % 2 == 0 or col % 2 == 0:
                    continue

                current_x = x_offset + (col * alien_width)
                current_y = y_offset + (row * alien_height)

                self._create_alien(current_x, current_y)

    def calculate_fleet_size(
            self,
            alien_width,
            alien_height,
            screen_width,
            screen_height
    ):
        """Calculate the fleet dimensions."""
        fleet_width = screen_width // alien_width

        if fleet_width % 2 == 0:
            fleet_width -= 1
        else:
            fleet_width -= 2

        half_screen = screen_height // 2
        fleet_height = half_screen // alien_height

        if fleet_height % 2 == 0:
            fleet_height -= 1
        else:
            fleet_height -= 2

        return fleet_width, fleet_height

    def calculate_fleet_offsets(
            self,
            alien_width,
            alien_height,
            screen_width,
            fleet_width,
            fleet_height
    ):
        """Calculate offsets that center the fleet."""
        fleet_horizontal_spacing = fleet_width * alien_width
        x_offset = (
            screen_width - fleet_horizontal_spacing
        ) // 2

        fleet_vertical_spacing = fleet_height * alien_height
        half_screen = self.settings.screen_height // 2
        y_offset = (
            half_screen - fleet_vertical_spacing
        ) // 2

        return x_offset, y_offset

    def _create_alien(self, current_x, current_y):
        """Create one alien and add it to the group."""
        new_alien = Alien(
            self,
            current_x,
            current_y
        )

        self.aliens.add(new_alien)

    def update_fleet(self):
        """Check edges and update every alien."""
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        """Check whether any alien reached an edge."""
        for alien in self.aliens:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.alien_direction *= -1
                break

    def _drop_alien_fleet(self):
        """Drop the entire fleet."""
        for alien in self.aliens:
            alien.y += self.alien_drop_speed
            alien.rect.y = alien.y
    
    def check_collisions(self, other_group):
        """Check collisions between aliens and another sprite group."""
        return pygame.sprite.groupcollide(self.aliens,other_group,True,True)


    def check_fleet_bottom(self):
        """Return True if an alien reaches the bottom of the screen."""
        screen_rect = self.game.screen.get_rect()

        for alien in self.aliens:
            if alien.rect.bottom >= screen_rect.bottom:
                return True

        return False

    def draw(self):
        """Draw every alien."""
        for alien in self.aliens:
            alien.draw_alien()