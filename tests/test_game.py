import pytest
import sys
import os
from collections import Counter

# Agregar el directorio src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.game import Game
import string

class TestGame:
    def test_game_initialization(self):
        # setup
        game = Game()
        # exercise
        grid = game.grid
        # verify
        #assert grid is not None
        assert isinstance(grid, list)
        assert len(grid) == 9
        for i in grid:
            assert i in string.ascii_uppercase, f"'{i}' no es valido"
        # teardown

    def test_word_is_valid(self):
        game = Game()
        grid = game.grid

        game.grid = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']  # Fijar el grid para pruebas

        # valid case
        assert game.is_valid("ABC") is True, "La palabra 'ABC' debería ser válida"

        assert game.is_valid("XYZ") is False, "La palabra 'XYZ' no debería ser válida"

        assert game.is_valid("AAA") is False, "La palabra 'AAA' no debería ser válida"

    def test_empty_word(self):
        # setup
        game = Game()
        game.grid = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

        # empty word
        assert game.is_valid("") is False, "Una palabra vacía no debería ser válida"

    def test_case_insensitivity(self):
        # setup
        game = Game()
        game.grid = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

        # case insensitivity
        assert game.is_valid("abc") is True, "La palabra 'abc' debería ser válida sin importar mayúsculas/minúsculas"

    def test_unknown_word_is_invalid(self):
        """A word that is not in the English dictionary should not be valid"""
        game = Game()
        game.grid = list('KWIENFUQW') # Force the grid to a test case:
        assert game.is_valid('FEUN') is False
