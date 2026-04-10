"""Tests for the Game class: initialisation and screen parameters."""
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
    """Game object should be created without errors."""
    assert isinstance(game_instance, Game)


def test_screen_size(game_instance):
    """Display surface should match the constants-defined resolution."""
    assert game_instance.screen.get_size() == (800, 600)


def test_initial_score_is_zero(game_instance):
    """Score must start at 0."""
    assert game_instance.game_score == 0


def test_game_is_running_on_start(game_instance):
    """game_is_running flag must be True right after __init__."""
    assert game_instance.game_is_running is True
