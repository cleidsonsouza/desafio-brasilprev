from random import randint

class Jogador: 
    
    # Valor do bônus para quem completar uma volta no tabuleiro
    bonus = 100
    
    def __init__(self, saldo, posicao, comportamento):
        self._saldo = saldo
        self._posicao = posicao
        self._comportamento = comportamento        
        self._propriedades = []        
       
    @property
    def saldo(self):
        return self._saldo
        
    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo
    
    @property
    def posicao(self):
        return self._posicao
        
    @posicao.setter
    def posicao(self, posicao):
        self._posicao = posicao    
        
    @property
    def comportamento(self):
        return self._comportamento
        
    @comportamento.setter
    def comportamento(self, comportamento):
        self._comportamento = comportamento
    
    
    # Movimenta jogador no tabuleiro
    def movimentar_jogador(self, dado, num_propriedades): 
        posicao_anterior = self._posicao         
        self._posicao = (self._posicao + dado) % num_propriedades                 
        if self._posicao == 0 or (self._posicao - posicao_anterior) < 0:            
            self._saldo += self.bonus     
    
    # Joga o dado
    def jogar_dado(self):
        return randint(1,6)
    
    # Efetua pagamento de aluguel
    def pagar_aluguel(self, proprietario, valor_aluguel):
        if self != proprietario:
            proprietario._saldo += valor_aluguel
            self._saldo -= valor_aluguel
    
    # Efetua compra de propriedade
    def comprar_propriedade(self, propriedade):         
        self._propriedades.append(propriedade)       
        self._saldo -= propriedade._custo_venda
       
    # Verifica se propriedade está disponível para compra
    def propriedade_disponivel(self, jogadores):
        for jogador in jogadores: 
            for propriedade in jogador._propriedades:
                if self._posicao == propriedade._ordem_tabuleiro:                
                    return False
        return True    
    
    # Obtém informações sobre o proprietário e valor do aluguel da prop.
    def info(self, jogadores):
        for jogador in jogadores: 
            for propriedade in jogador._propriedades:
                if self._posicao == propriedade._ordem_tabuleiro:                
                    return [jogador, propriedade._valor_aluguel]
        return 0
    
    # Efetua jogada    
    def jogar(self, jogadores, propriedades):                                 
                     
        # Obtém o valor do dado
        dado = self.jogar_dado()
        
        # Movimenta jogador no tabuleiro           
        self.movimentar_jogador(dado, len(propriedades))
        
        # Obtém propriedade onde o jogador parou
        prop = propriedades[self._posicao]
        
        # Verifica se a propriedade onde o jogador parou possui proprietário
        propriedade_disponivel = self.propriedade_disponivel(jogadores)
                              
        # Define condições dos jogadores p/ efetuarem a compra da propriedade
        impulsivo_comprar = True
        exigente_comprar = prop._valor_aluguel > 50
        cauteloso_comprar = (self._saldo - prop._custo_venda) >= 80
        aleatorio_comprar = randint(1,100) > 50
        
        # Efetua compra de propriedades ou pagamento de aluguel    
        if (propriedade_disponivel and self._saldo >= prop._custo_venda and 
                (self._comportamento == 'aleatório' and aleatorio_comprar or
                 self._comportamento == 'cauteloso' and cauteloso_comprar or
                 self._comportamento == 'exigente' and exigente_comprar or
                 self._comportamento == 'impulsivo' and impulsivo_comprar)):
            # Se algum jogador atender às condições, comprar a propriedade
            self.comprar_propriedade(prop)       
        elif not propriedade_disponivel:
            proprietario, valor_aluguel = self.info(jogadores)
            if self._saldo >= valor_aluguel:
                self.pagar_aluguel(proprietario, valor_aluguel)
            else:
                proprietario._saldo += self._saldo 
                # Retorna 0 se o jogador não puder prosseguir no jogo
                return 0
        # Retorna 0 se o jogador não puder prosseguir no jogo
        return 1
                