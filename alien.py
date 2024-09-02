import pygame
import math
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ALIEN_SPEED
from random import randint, uniform


class Alien:
    def __init__(self):
        self.image = pygame.image.load('img/alien.png')
        self.width, self.height = self.image.get_size()
        self.x, self.y = randint(0, SCREEN_WIDTH - self.width), 0
        self.speed = ALIEN_SPEED
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.angle = math.radians(uniform(0, 180))
        self.dirx = self.speed * math.cos(self.angle)
        self.diry = max(0, self.speed * math.sin(self.angle))

    def update_position(self):
        self.x += self.dirx
        self.y += self.diry

    def reach_screen_width(self):
        return self.x < 0 or self.x > SCREEN_WIDTH - self.width

    def change_direction(self):
        self.dirx *= -1
        self.x = max(0, min(self.x, SCREEN_WIDTH - self.width))

    def reach_screen_height(self):
        return self.y >= SCREEN_HEIGHT

    def increase_speed(self):
        self.speed += 0.1

    def reset(self):
        self.increase_speed()
        self.x, self.y = randint(0, SCREEN_WIDTH - self.width), 0
        self.angle = math.radians(uniform(0, 180))
        self.dirx = self.speed * math.cos(self.angle)
        self.diry = max(0, self.speed * math.sin(self.angle))

    def update_rect(self):
        self.rect.topleft = (self.x, self.y)

    def reach_hero(self, hero):
        self.update_rect()
        return self.rect.colliderect(hero)
