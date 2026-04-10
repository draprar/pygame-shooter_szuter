import pygame
from constants import BALL_STEP, BALL_WIDTH, BALL_HEIGHT


class Ball:
    def __init__(self, hero):
        self.image = pygame.image.load('img/ball.png')
        self.width = BALL_WIDTH
        self.height = BALL_HEIGHT
        self.x, self.y = 0, 0
        self.step = BALL_STEP
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.was_fired = False
        self.hero = hero

    def fire(self):
        if not self.was_fired:  # prevent re-firing mid-flight
            self.was_fired = True
            self.x = self.hero.x + self.hero.width / 2 - self.width / 2
            self.y = self.hero.y - self.height
            self.update_rect()

    def update_position(self):
        if self.was_fired:
            self.y -= self.step
            self.update_rect()

    def is_out_of_screen(self):
        # BUG FIX: old formula `self.y + self.hero.y < 0` was wrong;
        # ball is off-screen when its top passes above y=0
        return self.y < 0

    def reset(self):
        self.was_fired = False
        self.update_rect()

    def update_rect(self):
        self.rect.topleft = (self.x, self.y)

    def is_collision(self, alien):
        return self.rect.colliderect(alien.rect)

