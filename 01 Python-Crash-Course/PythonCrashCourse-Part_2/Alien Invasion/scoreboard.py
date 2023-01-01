import pygame.font
from ship import Ship
from pygame.sprite import Group

class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, ai_game):
        """Initialize score-keeping attributes"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.status = ai_game.status

        # Set font
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 24)

        # Preparing the initial score image
        self.prep_images()

    def prep_images(self):
        self.prep_score()
        self.prep_ships()
        self.prep_instruction()
        self.prep_high_score()
        self.prep_all_time_high()
        self.prep_level()

    def prep_score(self):
        """Turn score into a rendered image"""
        rounded_score = round(self.status.score, -1)
        score_str = "SCORE: " + "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.settings.bg_color)
        # Display score at top right corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.screen_rect.top + Ship(
            self.ai_game).rect.height + 10

    def prep_high_score(self):
        """Turn high score into a rendered image"""
        rounded_high_score = round(self.status.high_score, -1)
        high_score_str = "HIGHEST SCORE: " + "{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color,
                                                 self.settings.bg_color)
        # Display score at top right corner
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.left + 20
        self.high_score_rect.top = self.screen_rect.top + Ship(
            self.ai_game).rect.height + 10

    def prep_level(self):
        """Turn the level into a rendered image"""
        level_str = "LEVEL: " + str(self.status.level)
        self.level_image = self.font.render(level_str, True, self.text_color,
                                            self.settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_instruction(self):
        """Turn the game instructions into a rendered image"""
        ins_str = "Press 'P': Start Game. Press 'Q': Quit. Press 'C': Clear " \
                  "Records."
        self.ins_image = self.font.render(ins_str, True, self.text_color,
                                          self.settings.bg_color)

        self.ins_rect = self.ins_image.get_rect()
        self.ins_rect.left = self.screen_rect.left + 10
        self.ins_rect.bottom = self.screen_rect.bottom - 10

    def prep_all_time_high(self):
        """Turn all time high score into a rendered image"""
        rounded_all_time_high = round(self.status.all_time_high, -1)
        all_time_high_str = "ALL-TIME HIGHEST: " + "{:,}".format(int(
            rounded_all_time_high))
        self.all_time_high_image = self.font.render(all_time_high_str, True,
                                                    self.text_color,
                                                    self.settings.bg_color)

        self.all_time_high_rect = self.all_time_high_image.get_rect()
        self.all_time_high_rect.left = self.high_score_rect.left
        self.all_time_high_rect.top = self.high_score_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships left"""
        self.ships = Group()
        for ship_number in range(self.status.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = (self.screen_rect.left + ship_number *
                           ship.rect.width)
            ship.rect.y = 10
            self.ships.add(ship)

    def check_high_score(self):
        """Check if there's a new high score"""
        if self.status.score > self.status.high_score:
            self.status.high_score = self.status.score
            self.prep_high_score()

    def check_all_time_high_score(self):
        """Compare current score to all-time highest and record accordingly"""
        if self.status.all_time_high < self.status.high_score:
            self.status.all_time_high = self.status.high_score
            with open("text_files/ai_game_all_time_record.txt", "r+") as f:
                f.write(str(self.status.high_score))
            self.prep_all_time_high()

    def check_all_records(self):
        """Check current high score and all-time high score"""
        self.check_high_score()
        self.check_all_time_high_score()

    def clear_record(self):
        """Clear highest score and all-time highest"""
        self.status.high_score = 0
        self.status.all_time_high = 0
        with open("text_files/ai_game_all_time_record.txt", "w") as f:
            f.write("0")
        # Display updated record
        self.prep_high_score()
        self.prep_all_time_high()
        self.show_score()

    def show_score(self):
        """Draw score to screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
        self.screen.blit(self.all_time_high_image, self.all_time_high_rect)

        if not self.status.game_active:
            self.screen.blit(self.ins_image, self.ins_rect)
