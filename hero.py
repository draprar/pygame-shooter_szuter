import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, HERO_STEP, HERO_MAX_WIDTH, HERO_MAX_HEIGHT


class Hero:
    def __init__(self, image_path='img/hero.png'):
        self.image = pygame.image.load(image_path)
        entry_width, entry_height = self.image.get_size()

        if entry_width > HERO_MAX_WIDTH or entry_height > HERO_MAX_HEIGHT:
            scale_factor = min(HERO_MAX_WIDTH / entry_width, HERO_MAX_HEIGHT / entry_height)
            new_width = int(entry_width * scale_factor)
            new_height = int(entry_height * scale_factor)
            self.image = pygame.transform.scale(self.image, (new_width, new_height))
        else:
            new_width, new_height = entry_width, entry_height

        self.width, self.height = new_width, new_height
        # Use integer division so self.x/y are always int → rect stays pixel-exact
        self.x = (SCREEN_WIDTH - self.width) // 2
        self.y = SCREEN_HEIGHT - self.height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.step = HERO_STEP
        self.is_moving_left, self.is_moving_right = False, False

    def move_left(self):
        self.is_moving_left = True

    def move_right(self):
        self.is_moving_right = True

    def stop_moving(self):
        self.is_moving_left = False
        self.is_moving_right = False

    def update_position(self):
        if self.is_moving_left and self.x >= self.step:
            self.x -= self.step
        if self.is_moving_right and self.x <= SCREEN_WIDTH - self.width - self.step:
            self.x += self.step

        self.rect.topleft = (self.x, self.y)
