import sys
import pygame
from hero import Hero
from alien import Alien
from ball import Ball
from menu import Menu
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_IMAGE_PATH, GAME_CAPTION, ALIEN_SPEED_EASY, \
    ALIEN_SPEED_NORMAL, ALIEN_SPEED_HARD


class Game:
    def __init__(self):
        pygame.display.set_caption(GAME_CAPTION)
        self.screen_width, self.screen_height = SCREEN_WIDTH, SCREEN_HEIGHT
        self.background_image = pygame.image.load(BACKGROUND_IMAGE_PATH)
        self.background_image = pygame.transform.scale(self.background_image, (self.screen_width, self.screen_height))
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.game_font = pygame.font.Font(None, 30)
        self.game_score = 0
        self.alien_speed = None

        self.hero = None
        self.alien = None
        self.ball = None

        self.game_is_running = True

    def run(self):
        self.show_menu()
        while self.game_is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                self.handle_key_events(event)
            self.update_game_state()
            self.draw_screen()

        self.show_game_over()

    def show_menu(self):
        menu = Menu(self.screen)
        menu.display_menu()
        choice, difficulty = menu.get_user_choice()

        if difficulty == 'E':
            self.alien_speed = ALIEN_SPEED_EASY
        elif difficulty == 'N':
            self.alien_speed = ALIEN_SPEED_NORMAL
        elif difficulty == 'H':
            self.alien_speed = ALIEN_SPEED_HARD

        if choice == 1:
            hero_image_path = menu.choose_hero_image()
            if hero_image_path:
                self.hero = Hero(hero_image_path)
            else:
                self.hero = Hero()
        else:
            self.hero = Hero()

        self.alien = Alien(self.alien_speed)
        self.ball = Ball(self.hero)

    def handle_key_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.hero.move_left()
            if event.key == pygame.K_RIGHT:
                self.hero.move_right()
            if event.key == pygame.K_SPACE:
                self.ball.fire()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.hero.stop_moving()

    def update_game_state(self):
        self.hero.update_position()
        self.alien.update_position()
        self.ball.update_position()

        if self.ball.is_out_of_screen():
            self.ball.reset()

        if self.ball.is_collision(self.alien):
            self.ball.reset()
            self.alien.reset()
            self.game_score += 1

        if self.alien.reach_screen_width():
            self.alien.change_direction()

        if self.alien.reach_screen_height():
            self.alien.reset()

        if self.alien.reach_hero(self.hero):
            self.game_is_running = False

    def draw_screen(self):
        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.hero.image, (self.hero.x, self.hero.y))
        self.screen.blit(self.alien.image, (self.alien.x, self.alien.y))
        if self.ball.was_fired:
            self.screen.blit(self.ball.image, (self.ball.x, self.ball.y))
        self.show_game_score()
        self.show_legend()
        pygame.display.update()

    def show_game_score(self):
        game_score_text = self.game_font.render(f"Your score is: {self.game_score}", True, 'white')
        self.screen.blit(game_score_text, (20, 20))

    def show_legend(self):
        hero_movement_left = self.game_font.render("Move Left: Left Arrow Key", True, 'white')
        hero_movement_right = self.game_font.render("Move Right: Right Arrow Key", True, 'white')
        fire_ball = self.game_font.render("Fire: Spacebar", True, 'white')
        self.screen.blit(hero_movement_left, (500, 20))
        self.screen.blit(hero_movement_right, (500, 40))
        self.screen.blit(fire_ball, (500, 60))

    def show_game_over(self):
        game_over_text = self.game_font.render("Game Over", True, 'red')
        game_over_rectangle = game_over_text.get_rect()
        game_over_rectangle.center = (self.screen_width / 2, self.screen_height / 2)
        self.screen.blit(game_over_text, game_over_rectangle)
        pygame.display.update()
        pygame.time.wait(500)
