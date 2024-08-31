import pygame
import math
from constants import SCREEN_WIDTH, ALIEN_SPEED
from random import randint, uniform


class Alien:
    def __init__(self):
        self.image = pygame.image.load('images/alien.png')
        self.width, self.height = self.image.get_size()
        self.x, self.y = randint(0, SCREEN_WIDTH - self.width), 0
        self.speed = ALIEN_SPEED
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.angle = math.radians(uniform(9, 180))
        self.dirx = self.speed * math.cos(self.angle)
        self.diry = max(0, self.speed * math.sin(self.angle))

    def update_position(self):
        self.x += self.dirx
        self.y += self.diry

    def increase_speed(self):
        self.speed += 0.1

    def reset(self):
        self.increase_speed()

    def topleft(self):
        self.rect.topleft = (self.x, self.y)

    def reach_hero(self, hero):
        return self.rect.colliderect(hero)
