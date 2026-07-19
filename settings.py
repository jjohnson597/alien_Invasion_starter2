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
        self.ship_speed = 5

        self.bullet_file = pathlib.Path.cwd() / "Assets" / "images" / "laserBlast.png"
        self.laser_sound = pathlib.Path.cwd() / "Assets" / "sound" / "laser.mp3"
        self.bullet_width = 25
        self.bullet_height = 80
        self.bullet_speed = 7
        self.bullet_color = (255, 0, 0)
        self.bullet_amount = 5

        self.alien_file = pathlib.Path.cwd() / "Assets" / "images" / "enemy_4.png"
        self.alien_width = 40
        self.alien_height = 40
        self.alien_speed = 2
        self.alien_direction = 1
        self.alien_drop_speed = 40
        

