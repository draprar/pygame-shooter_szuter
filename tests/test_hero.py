import pygame
import pytest
from game import Hero

SCREEN_WIDTH = 800
HERO_STEP = 5


@pytest.fixture
def hero_instance():
    pygame.init()
    hero = Hero()
    yield hero
    pygame.quit()


def hero_moving_left(hero_instance):
    initial_position = hero_instance.rect.x
    hero_instance.move_left()
    assert hero_instance.rect.x < initial_position


def hero_moving_right(hero_instance):
    initial_position = hero_instance.rect.x
    hero_instance.move_right()
    assert hero_instance.rect.x > initial_position


def hero_reach_left_boundary(hero_instance):
    hero_instance.rect.x = 0
    hero_instance.move_left()
    assert hero_instance.rect.x == 0


def hero_reach_right_boundary(hero_instance):
    hero_instance.rect.x = SCREEN_WIDTH - hero_instance.rect.width
    hero_instance.move_right()
    assert hero_instance.rect.x == SCREEN_WIDTH - hero_instance.rect.width
