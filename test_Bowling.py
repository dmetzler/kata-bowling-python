import pytest

from Bowling import Game


@pytest.fixture
def game():
    return Game()

def test_can_create_a_game(game):
    assert game is not None

