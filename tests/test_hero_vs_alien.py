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


def test_collision(hero_instance, alien_instance):
    hero_instance.rect.x = 50
    alien_instance.rect.x = 50
    hero_instance.rect.y = 100
    alien_instance.rect.y = 100
    assert hero_instance.rect.colliderect(alien_instance.rect)
