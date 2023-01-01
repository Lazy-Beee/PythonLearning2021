import sys
from time import sleep

import pygame
from settings import Settings
from ship import Ship
from bullets import Bullet
from alien import Alien
from game_status import GameStatus
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize game, and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.screen_rect = self.screen.get_rect()

        self.status = GameStatus(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.bullet_dir = 0
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start main loop of the game"""
        while True:
            self._check_events()

            if self.status.game_active:
                self.ship.update()
                self._update_bullet()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        """Respond to keyboard and mouth events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.sb.check_all_records()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos, False)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self.sb.check_all_records()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._check_play_button((0, 0), True)
        elif event.key == pygame.K_c:
            self.sb.clear_record()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to bullet group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self, self.bullet_dir)
            self.bullets.add(new_bullet)
            self._update_bullet_direction()

    def _update_bullet_direction(self):
        """Record and change bullet direction"""
        self.bullet_dir += 1
        if self.bullet_dir >= 5:
            self.bullet_dir -= 5

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Draw score information
        self.sb.show_score()

        # Draw play button if game is inactive
        if not self.status.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _update_bullet(self):
        """Update bullets and get rid of old bullets"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0 or bullet.rect.right < 0 or \
                    bullet.rect.left > self.screen_rect.right:
                self.bullets.remove(bullet)
        # Check collisions and remove destroyed aliens
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Check if any bullet has hit alien. If so, remove the hit alien"""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens,
                                                True, True)
        if collisions:
            for aliens in collisions.values():
                # noinspection PyTypeChecker
                self.status.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()

        # Start new level if all aliens are shoot down
        if not self.aliens:
            self._start_new_level()

    def _start_new_level(self):
        """Start a new level of game"""
        # Destroy existing bullets and create a new fleet
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()

        # Increase level
        self.status.level += 1
        self.sb.prep_level()

    def _create_fleet(self):
        """Create a fleet of aliens"""
        # Make an alien and find the number of aliens in a row
        # Space between aliens is equal to one aline width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # determine the number of rows
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (4 * alien_height)
                             - ship_height)
        number_aliens_y = available_space_y // (2 * alien_height)

        # Create each row of aliens
        for alien_row in range(number_aliens_y):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, alien_row)

    def _create_alien(self, alien_number, alien_row):
        """Create an alien and place it in a row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.y = alien_height * 2 + 2 * alien_height * alien_row
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _update_aliens(self):
        """Check if the fleet is at an edge and then update the position of all
        aliens on the screen"""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions
        # noinspection PyTypeChecker
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for alien reaching the bottom
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """Respond if an alien has reached the edge of screen"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change fleet direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Respond to the ship being hit by alien"""
        if self.status.ships_left > 0:
            # Decrement ship_left and update display
            self.status.ships_left -= 1
            self.sb.prep_ships()
            # Clear existing aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            # Create new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            # Pause
            sleep(self.settings.pause_after_hit)
        else:
            self.status.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if any alien has reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _check_play_button(self, mouse_pos, p_pressed):
        """Start a new game when player clicks play button"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if (button_clicked or p_pressed) and not self.status.game_active:
            # Check if there's a new high score
            self.sb.check_all_records()

            # Start game
            self._start_game()

    def _start_game(self):
        """Prepare the game for starting"""
        # Reset game statistics
        self.status.reset_status()
        self.status.game_active = True
        self.sb.prep_images()
        self.settings.initialize_dynamic_settings()

        # Get rid of aliens and bullets
        self.aliens.empty()
        self.bullets.empty()

        # Create new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()

        # Hide mouse cursor
        pygame.mouse.set_visible(False)


if __name__ == '__main__':
    # Make game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()