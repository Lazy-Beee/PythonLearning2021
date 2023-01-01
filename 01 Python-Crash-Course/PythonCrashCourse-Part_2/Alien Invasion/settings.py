class Settings:
    """A class to store all settings for game"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 5
        self.pause_after_hit = 0.5

        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 5
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 10

        # Alien settings
        self.alien_drop_speed = 10

        # How fast the game speeds up
        self.speed_up_scale = 1.1

        # How quick the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throught the game"""
        self.ship_speed = 0.1
        self.alien_speed = 0.1
        self.bullet_speed = 0.3
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien points"""
        self.ship_speed *= self.speed_up_scale
        self.alien_speed *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale

        self.alien_points = int(self.score_scale * self.alien_points)