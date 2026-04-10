"""Tests for Hero vs Alien collision detection."""
import pygame
import pytest
from hero import Hero
from alien import Alien

ALIEN_SPEED = 1


@pytest.fixture
def hero_instance():
    pygame.init()
    hero = Hero()
    yield hero
    pygame.quit()


@pytest.fixture
def alien_instance():
    pygame.init()
    alien = Alien(ALIEN_SPEED)
    yield alien
    pygame.quit()


def test_collision_when_overlapping(hero_instance, alien_instance):
    """Collision is detected when hero and alien rects fully overlap."""
    hero_instance.rect.topleft = (50, 100)
    alien_instance.rect.topleft = (50, 100)
    assert hero_instance.rect.colliderect(alien_instance.rect)


def test_no_collision_when_far_apart(hero_instance, alien_instance):
    """No collision when hero and alien are far from each other."""
    hero_instance.rect.topleft = (0, 500)
    alien_instance.rect.topleft = (700, 0)
    assert not hero_instance.rect.colliderect(alien_instance.rect)


def test_reach_hero_uses_rect(hero_instance, alien_instance):
    """Alien.reach_hero() must use hero.rect, not the Hero object directly."""
    alien_instance.rect.topleft = (hero_instance.rect.x, hero_instance.rect.y)
    assert alien_instance.reach_hero(hero_instance)
