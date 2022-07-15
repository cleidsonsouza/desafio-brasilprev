from random import random, randint, sample, shuffle

class Propriedade:
    
    def __init__(self, custo_venda, valor_aluguel, ordem_tabuleiro):
        self._custo_venda = custo_venda
        self._valor_aluguel = valor_aluguel
        self._ordem_tabuleiro = ordem_tabuleiro 
      
    @property
    def custo_venda(self):
        return self._custo_venda
        
    @custo_venda.setter
    def custo_venda(self, custo_venda):
        self._custo_venda = custo_venda
         
    @property
    def valor_aluguel(self):
        return self._valor_aluguel
        
    @valor_aluguel.setter
    def valor_aluguel(self, valor_aluguel):
        self._valor_aluguel = valor_aluguel
           
    @property
    def ordem_tabuleiro(self):
        return self._ordem_tabuleiro
    
    @ordem_tabuleiro.setter
    def ordem_tabuleiro(self, ordem_tabuleiro):
        self._ordem_tabuleiro = ordem_tabuleiro            