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
    pygame.init()
    ball = Ball(hero_instance)
    yield ball
    pygame.quit()


@pytest.fixture
def alien_instance():
    pygame.init()
    alien = Alien(ALIEN_SPEED)
    yield alien
    pygame.quit()


def test_collision(ball_instance, alien_instance):
    ball_instance.rect.x = 100
    alien_instance.rect.x = 100
    ball_instance.rect.y = 200
    alien_instance.rect.y = 200

    assert ball_instance.rect.colliderect(alien_instance.rect)
