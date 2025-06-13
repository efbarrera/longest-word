"""
Módulo que define la clase Game para el juego de la palabra más larga.
Incluye métodos para generar un tablero y validar palabras.
"""

import random
from collections import Counter

class Game:
    """
    Clase para representar el juego de la palabra más larga.
    Permite generar un tablero y validar palabras ingresadas por el jugador.
    """

    def __init__(self):
        self.grid = self._generate_grid()

    def _generate_grid(self, size=9) -> list:
        """Genera un tablero aleatorio de letras mayúsculas del tamaño dado."""
        letters = 'abcdefghijklmnopqrstuvwxyz'
        return [random.choice(letters).upper() for _ in range(size)]

    def is_valid(self, word: str) -> bool:
        """
        Retorna True si y solo si la palabra es válida, dada la grid del juego.
        """
        if not word:
            return False

        word = word.upper()
        word_count = Counter(word)
        grid_count = Counter(self.grid)

        for letter, count in word_count.items():
            if grid_count[letter] < count:
                return False

        return True
