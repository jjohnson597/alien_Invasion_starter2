import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, game: "AlienInvasion"):
        """Initialize statistics and load saved scores."""
        self.game = game
        self.settings = game.settings

        # Highest score earned during this running session.
        self.max_score = 0

        self._init_saved_scores()
        self.reset_stats()

    def _init_saved_scores(self):
        """Load the saved high score or create a new score file."""
        self.path = self.settings.scores_file

        try:
            if self.path.exists() and self.path.stat().st_size > 0:
                contents = self.path.read_text(encoding="utf-8")
                scores = json.loads(contents)
                self.hi_score = scores.get("hi_score", 0)
            else:
                self.hi_score = 0
                self.save_scores()

        except (OSError, json.JSONDecodeError):
            self.hi_score = 0
            self.save_scores()

    def save_scores(self):
        """Write the permanent high score to the JSON file."""
        scores = {
            "hi_score": self.hi_score
        }

        contents = json.dumps(
            scores,
            indent=4
        )

        try:
            self.path.parent.mkdir(
                parents=True,
                exist_ok=True
            )
            self.path.write_text(
                contents,
                encoding="utf-8"
            )
        except OSError as error:
            print(f"Unable to save score: {error}")

    def reset_stats(self):
        """Reset statistics for a new game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def update(self, collisions):
        """Update scoring after aliens are destroyed."""
        self._update_score(collisions)
        self._update_max_score()
        self._update_hi_score()

    def _update_score(self, collisions):
        """Add points for every alien destroyed."""
        for aliens_hit in collisions.values():
            self.score += (
                len(aliens_hit)
                * self.settings.alien_points
            )

    def _update_max_score(self):
        """Track the best score during this game session."""
        if self.score > self.max_score:
            self.max_score = self.score

    def _update_hi_score(self):
        """Update and save the permanent high score."""
        if self.score > self.hi_score:
            self.hi_score = self.score
            self.save_scores()

    def update_level(self):
        """Advance to the next level."""
        self.level += 1