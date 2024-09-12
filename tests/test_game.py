import pytest
import pygame
from game import Game


@pytest.fixture
def game_instance():
    pygame.init()
    game = Game()
    yield game
    pygame.quit()


def test_game_initialization(game_instance):
    assert isinstance(game_instance, Game)


def test_screen_size(game_instance):
    assert game_instance.screen.get_size() == (800, 600)
