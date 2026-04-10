"""Tests for Ball vs Alien collision detection and ball physics."""
import pygame
import pytest
from ball import Ball
from alien import Alien
from hero import Hero

ALIEN_SPEED = 1


@pytest.fixture
def hero_instance():
    pygame.init()
    hero = Hero()
    yield hero
    pygame.quit()


@pytest.fixture
def ball_instance(hero_instance):
    ball = Ball(hero_instance)
    yield ball


@pytest.fixture
def alien_instance():
    pygame.init()
    alien = Alien(ALIEN_SPEED)
    yield alien
    pygame.quit()


def test_collision_when_overlapping(ball_instance, alien_instance):
    """Collision detected when ball and alien rects overlap."""
    ball_instance.rect.topleft = (100, 200)
    alien_instance.rect.topleft = (100, 200)
    assert ball_instance.rect.colliderect(alien_instance.rect)


def test_no_collision_when_far_apart(ball_instance, alien_instance):
    """No collision when ball and alien are far from each other."""
    ball_instance.rect.topleft = (0, 500)
    alien_instance.rect.topleft = (700, 0)
    assert not ball_instance.rect.colliderect(alien_instance.rect)


def test_ball_not_fired_initially(ball_instance):
    """Ball must not be in flight at creation."""
    assert ball_instance.was_fired is False


def test_ball_fires_once(ball_instance):
    """Calling fire() twice should not reset the in-flight ball."""
    ball_instance.fire()
    first_y = ball_instance.y
    ball_instance.fire()  # second call should be ignored
    assert ball_instance.y == first_y


def test_ball_moves_up_when_fired(ball_instance):
    """Ball y decreases (moves toward top) after each update_position() tick."""
    ball_instance.fire()
    y_before = ball_instance.y
    ball_instance.update_position()
    assert ball_instance.y < y_before


def test_ball_out_of_screen(ball_instance):
    """is_out_of_screen() returns True when ball y < 0."""
    ball_instance.was_fired = True
    ball_instance.y = -1
    assert ball_instance.is_out_of_screen()


def test_ball_reset(ball_instance):
    """reset() must mark ball as not fired."""
    ball_instance.fire()
    ball_instance.reset()
    assert ball_instance.was_fired is False

