"""Tests for the Hero class: movement and boundary clamping."""
import pygame
import pytest
from hero import Hero

SCREEN_WIDTH = 800
HERO_STEP = 5


@pytest.fixture
def hero_instance():
    pygame.init()
    hero = Hero()
    yield hero
    pygame.quit()


def test_hero_moving_left(hero_instance):
    """Hero moves left when move_left() is called and update_position() is ticked."""
    initial_x = hero_instance.x
    hero_instance.move_left()
    hero_instance.update_position()
    assert hero_instance.x < initial_x
    assert hero_instance.rect.x < initial_x


def test_hero_moving_right(hero_instance):
    """Hero moves right when move_right() is called and update_position() is ticked."""
    initial_x = hero_instance.x
    hero_instance.move_right()
    hero_instance.update_position()
    assert hero_instance.x > initial_x
    assert hero_instance.rect.x > initial_x


def test_hero_stop_moving(hero_instance):
    """Hero stops after stop_moving() — further update_position() calls don't move it."""
    hero_instance.move_left()
    hero_instance.stop_moving()
    initial_x = hero_instance.x
    hero_instance.update_position()
    assert hero_instance.x == initial_x


def test_hero_reach_left_boundary(hero_instance):
    """Hero cannot move past the left edge of the screen."""
    hero_instance.x = 0
    hero_instance.move_left()
    hero_instance.update_position()
    assert hero_instance.x == 0


def test_hero_reach_right_boundary(hero_instance):
    """Hero cannot move past the right edge of the screen."""
    hero_instance.x = SCREEN_WIDTH - hero_instance.width
    hero_instance.move_right()
    hero_instance.update_position()
    assert hero_instance.x == SCREEN_WIDTH - hero_instance.width


def test_hero_rect_stays_in_sync(hero_instance):
    """rect.topleft must match (x, y) exactly after update_position() (both are int)."""
    hero_instance.move_right()
    hero_instance.update_position()
    assert hero_instance.rect.topleft == (hero_instance.x, hero_instance.y)

