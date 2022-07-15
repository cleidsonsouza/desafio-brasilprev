import pytest
from codigo.jogador import Jogador

obj = Jogador(1.1, 1, 'impulsivo')

def test_jogar_dado():
    assert Jogador.jogar_dado(obj) >= 1 and Jogador.jogar_dado(obj) <= 6