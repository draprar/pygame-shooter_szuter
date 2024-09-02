import pygame
from constants import BALL_STEP


class Ball:
    def __init__(self, hero):
        self.image = pygame.image.load('img/ball.png')
        self.width, self.height = self.image.get_size()
        self.x, self.y = 0, 0
        self.step = BALL_STEP
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.was_fired = False
        self.hero = hero

    def fire(self):
        self.was_fired = True
        self.x = self.hero.x + self.hero.width / 2 - self.width / 2
        self.y = self.hero.y - self.height

    def update_position(self):
        if self.was_fired:
            self.y -= self.step

    def is_out_of_screen(self):
        return self.y + self.hero.y < 0

    def reset(self):
        self.was_fired = False

    def topleft(self):
        self.rect.topleft = (self.x, self.y)

    def is_collision(self, alien):
        return self.rect.colliderect(alien.rect)

