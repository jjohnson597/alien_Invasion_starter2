import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class HUD:
    """Display game statistics on the screen."""

    def __init__(self, game: "AlienInvasion"):
        """Initialize the HUD."""
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.game_stats

        self.font = pygame.font.Font(
            self.settings.font_file,
            self.settings.HUD_font_size
        )

        # Create a smaller ship image for the lives display.
        ship_image = pygame.image.load(
            self.settings.ship_file
        )

        self.life_image = pygame.transform.scale(
            ship_image,
            (
                self.settings.ship_width // 2,
                self.settings.ship_height // 2
            )
        )

        self.prep_images()

    def prep_images(self):
        """Prepare all HUD text images."""
        self.prep_score()
        self.prep_hi_score()
        self.prep_level()

    def prep_score(self):
        """Render the current score."""
        rounded_score = round(self.stats.score, -1)
        score_text = f"Score: {rounded_score:,}"

        self.score_image = self.font.render(
            score_text,
            True,
            self.settings.text_color
        )

        self.score_rect = self.score_image.get_rect()
        self.score_rect.top = 15
        self.score_rect.right = (
            self.screen_rect.right - 20
        )

    def prep_hi_score(self):
        """Render the saved high score."""
        rounded_hi_score = round(
            self.stats.hi_score,
            -1
        )

        hi_score_text = (
            f"High Score: {rounded_hi_score:,}"
        )

        self.hi_score_image = self.font.render(
            hi_score_text,
            True,
            self.settings.text_color
        )

        self.hi_score_rect = (
            self.hi_score_image.get_rect()
        )

        self.hi_score_rect.top = 15
        self.hi_score_rect.centerx = (
            self.screen_rect.centerx
        )

    def prep_level(self):
        """Render the current level."""
        level_text = f"Level: {self.stats.level}"

        self.level_image = self.font.render(
            level_text,
            True,
            self.settings.text_color
        )

        self.level_rect = (
            self.level_image.get_rect()
        )

        self.level_rect.right = (
            self.screen_rect.right - 20
        )

        self.level_rect.top = (
            self.score_rect.bottom + 10
        )

    def draw_lives(self):
        """Draw one miniature ship for each remaining life."""
        for ship_number in range(
            self.stats.ships_left
        ):
            x_position = (
                20
                + ship_number
                * (self.life_image.get_width() + 10)
            )

            self.screen.blit(
                self.life_image,
                (x_position, 15)
            )

    def draw(self):
        """Draw the full HUD."""
        self.screen.blit(
            self.score_image,
            self.score_rect
        )

        self.screen.blit(
            self.hi_score_image,
            self.hi_score_rect
        )

        self.screen.blit(
            self.level_image,
            self.level_rect
        )

        self.draw_lives()