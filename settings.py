import pathlib
class Settings:


    def __init__(self):
        self.name: str = "Alien Invasion"
        self.screen_width = 1200
        self.screen_height = 800
        self.FPS = 60
        self.bg_file = pathlib.Path.cwd() / "Assets" / "images" / "Starbasesnow.png"
        
        self.ship_file = pathlib.Path.cwd() / "Assets" / "images" / "ship2(no bg).png"
        self.ship_width = 40
        self.ship_height = 60

        self.bullet_file = pathlib.Path.cwd() / "Assets" / "images" / "laserBlast.png"
        self.laser_sound = pathlib.Path.cwd() / "Assets" / "sound" / "laser.mp3"
        self.impact_sound = pathlib.Path.cwd()/ "Assets"/ "sound"/ "impactSound.mp3"
        self.bullet_color = (255, 0, 0)

        self.alien_file = pathlib.Path.cwd() / "Assets" / "images" / "enemy_4.png"
        self.alien_width = 40
        self.alien_height = 40
        self.alien_direction = 1

        self.font_file = pathlib.Path.cwd()/ "Assets"/ "Fonts"/ "Silkscreen"/ "Silkscreen-Regular.ttf"
        self.button_width = 200
        self.button_height = 50
        self.button_color = (0, 135, 50)
        self.text_color = (255, 255, 255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.difficulty_scale = 1.1
        self.initialize_dynamic_settings()
        self.scores_file = (pathlib.Path.cwd()/ "Assets"/ "file"/ "scores.json")

    def initialize_dynamic_settings(self):
        """Initialize settings that change during gameplay."""
        self.ship_speed = 5
        self.ship_limit = 3

        self.bullet_width = 25
        self.bullet_height = 80
        self.bullet_speed = 7
        self.bullet_amount = 5

        self.alien_speed = 1
        self.alien_drop_speed = 40
        self.alien_points = 50

    def increase_difficulty(self):
        """Increase settings after completing a level."""
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.alien_speed *= self.difficulty_scale
        self.alien_points = int(self.alien_points * self.difficulty_scale)
        
        