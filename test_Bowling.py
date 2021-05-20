import pytest

from Bowling import Game


@pytest.fixture
def game():
    return Game()

def test_can_create_a_game(game):
    assert game is not None

def test_score(game):
    assert game.score == 0

def test_takedown_pins(game):
    game.takedown(3)
    assert game.score == 3

def test_guter_game(game):
    roll_many(game,20,0)
    assert game.score == 0

def test_simple_game(game):
    roll_many(game,20,1)
    assert game.score == 20

def roll_many(game, times, pins):
    for _ in range(0,times):
        game.takedown(pins)

def test_game_with_spare(game):
    game.takedown(0)
    game.takedown(0)
    game.takedown(8)
    game.takedown(2)
    game.takedown(3)
    game.takedown(4)
    roll_many(game,16,0)

    assert game.score == 20