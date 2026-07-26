import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet
from game_stats import GameStats
from button import Button
from hud import HUD



class AlienInvasion:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.settings = Settings()

        # Create the screen before any objects that use it.
        self.screen = pygame.display.set_mode(
            (
                self.settings.screen_width,
                self.settings.screen_height
            )
        )
        pygame.display.set_caption(self.settings.name)

        self.bg_image = pygame.image.load(
            self.settings.bg_file
        )
        self.bg = pygame.transform.scale(
            self.bg_image,
            (
                self.settings.screen_width,
                self.settings.screen_height
            )
        )

        self.running = True
        self.clock = pygame.time.Clock()

        self.game_stats = GameStats(self)

        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.hud = HUD(self)

        self.play_button = Button(self, "Play")
        self.game_active = False

        self.laser_sound = pygame.mixer.Sound(
            self.settings.laser_sound
        )
        self.laser_sound.set_volume(0.7)

        self.impact_sound = pygame.mixer.Sound(
            self.settings.impact_sound
        )
        self.impact_sound.set_volume(0.7)


    def run_game(self):
        """Run the main game loop."""
        while self.running:
            self.check_events()

            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()

            self._update_screen()
            self.clock.tick(self.settings.FPS)
    
    def _check_collisions(self):
        """Check collisions involving the ship, aliens, and bullets."""
        if self.ship.check_collisions(self.alien_fleet.aliens):
            self._check_game_status()

        elif self.alien_fleet.check_fleet_bottom():
            self._check_game_status()

        collisions = self.alien_fleet.check_collisions(
            self.ship.arsenal.arsenal
        )

        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)

            self.game_stats.update(collisions)
            self.hud.prep_score()
            self.hud.prep_hi_score()

        if self.alien_fleet.check_destroyed_status():
            self._reset_level()
            self.settings.increase_difficulty()
            self.game_stats.update_level()
            self.hud.prep_level()


    def restart_game(self):
        """Reset the game and begin active gameplay."""
        self.settings.initialize_dynamic_settings()

        self.game_stats.reset_stats()
        self.hud.prep_images()
        self._reset_level()

        self.game_active = True
        pygame.mouse.set_visible(False)

    def _quit_game(self):
        """Save scores and close the game."""
        self.game_stats.save_scores()
        self.running = False
        pygame.quit()
        sys.exit()

    def _check_game_status(self):
        """Subtract a ship or stop the game."""
        self.game_stats.ships_left -= 1

        if self.game_stats.ships_left > 0:
            self._reset_level()
            pygame.time.wait(500)
        else:
            self.game_active = False


    def _reset_level(self):
        """Clear the current level and create a new fleet."""
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.aliens.empty()
        self.alien_fleet.create_fleet()

        self.ship.rect.midbottom = self.ship.boundaries.midbottom
        self.ship.x = float(self.ship.rect.x)

    def _update_screen(self):
        self.screen.blit(self.bg, (0, 0))

        self.ship.draw()
        self.alien_fleet.draw()
        self.hud.draw()

        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)

        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit_game()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_button_clicked(self):
        """Start the game when the Play button is clicked."""
        mouse_pos = pygame.mouse.get_pos()

        if (
            self.play_button.check_clicked(mouse_pos)
            and not self.game_active
        ):
            self.restart_game()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        elif event.key == pygame.K_q:
            self._quit_game()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
