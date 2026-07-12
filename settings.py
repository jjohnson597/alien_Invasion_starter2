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
        

