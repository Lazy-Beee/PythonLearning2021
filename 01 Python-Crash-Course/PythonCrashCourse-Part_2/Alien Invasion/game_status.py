class GameStatus:
    """Track status of game"""

    def __init__(self, ai_game):
        """Initializing status"""
        self.settings = ai_game.settings
        self.game_active = False
        self.reset_status()

        # Never reset high score
        self.high_score = 0
        with open("text_files/ai_game_all_time_record.txt", "r+") as f:
            self.all_time_high = int(f.read())

    def reset_status(self):
        """Initializing status that can change during game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
