import pygame
import numpy as np
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game, direction):
        """Create a bullet object at the ship'd current location"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store bullet position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Store bullet direction
        self.dir = direction

    def update(self):
        """Move the bullet on the screen"""
        # dir = 0 -> moving left
        if self.dir == 0:
            self.x -= self.settings.bullet_speed
            self.rect.x = self.x
        # dir = 1 -> moving up-left
        elif self.dir == 1:
            self.x -= self.settings.bullet_speed / np.sqrt(2)
            self.rect.x = self.x
            self.y -= self.settings.bullet_speed / np.sqrt(2)
            self.rect.y = self.y
        # dir = 2 -> moving up
        elif self.dir == 2:
            self.y -= self.settings.bullet_speed
            self.rect.y = self.y
        # dir = 3 -> moving up-right
        elif self.dir == 3:
            self.x += self.settings.bullet_speed / np.sqrt(2)
            self.rect.x = self.x
            self.y -= self.settings.bullet_speed / np.sqrt(2)
            self.rect.y = self.y
        # dir = 4 -> moving right
        elif self.dir == 4:
            self.x += self.settings.bullet_speed
            self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)