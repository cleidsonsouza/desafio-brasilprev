import os
import numpy as np
import matplotlib.pyplot as plt

from jogador import Jogador
from propriedade import Propriedade
from random import random, randint, sample, shuffle

# Define função que apresenta os resultados, apenas numéricos, das simulações
def mostrar_resultados(vencedores, time_out, turnos):    
        
        # Calcula o percentual de vitórias por comportamento de jogador 
        percentual_vitorias = [
            round(vencedores.count('impulsivo')/3, 2),
            round(vencedores.count('exigente' )/3, 2),
            round(vencedores.count('cauteloso')/3, 2),
            round(vencedores.count('aleatório')/3, 2)            
        ]
             
        # Apresenta os resultados do desafio
        print(f'Partidas que terminaram com time out: {time_out}/300')
        print(f'Média de turnos por partida: {int(round(np.mean(turnos)))}')    
        
        print(f'Vitórias comport. Impulsivo: {percentual_vitorias[0]:.2f}%')
        print(f'Vitórias comport. Exigente : {percentual_vitorias[1]:.2f}%')
        print(f'Vitórias comport. Cauteloso: {percentual_vitorias[2]:.2f}%')
        print(f'Vitórias comport. Aleatório: {percentual_vitorias[3]:.2f}%')
    
        comportamento_vencedor = (
            percentual_vitorias.index(max(percentual_vitorias)))
        
        if comportamento_vencedor == 0:
            print('Comportamento que mais vence: IMPULSIVO')
        elif comportamento_vencedor == 1:
            print('Comportamento que mais vence: EXIGENTE')
        elif comportamento_vencedor == 2:
            print('Comportamento que mais vence: CAUTELOSO')
        else:        
            print('Comportamento que mais vence: ALEATÓRIO')

# Define função que apresenta os resultados, por gráficos, das simulações
def mostrar_resultados_graficos(vencedores, time_out, turnos):  
    
    # Apresenta gráfico da quatidade de partidas que terminaram com time out
    fig, ax = plt.subplots()
    plt.bar(0.25, time_out, color='black', width=0.1)
    plt.bar(0.25, 0, color='white', width=0.5)
    plt.title('Time outs das Simulações')
    plt.ylabel('Time outs das Simulações')
    plt.show()
    
    # Apresenta gráfico de turnos por simulação
    fig, ax = plt.subplots()
    plt.plot(turnos, '-b')
    plt.title('Quantidade de Turnos por Simulação')
    plt.xlabel('Simulação')
    plt.ylabel('Quantidade de Turnos')
    plt.show()
    
    # Apresenta gráfico da média de turnos por partida
    fig, ax = plt.subplots()
    plt.bar(0.25, np.mean(turnos), color='blue', width=0.1)
    plt.bar(0.25, 0, color='white', width=0.5)
    plt.title('Média de turnos por partida')
    plt.ylabel('Média de turnos por partida')
    plt.show()
        
    # Apresenta percentual de vitórias por comportamento de jogadores
    fig, ax = plt.subplots()
    plt.bar(1, vencedores.count('impulsivo'), color='gray', width=0.5)
    plt.bar(2, vencedores.count('exigente'), color='pink', width=0.5)
    plt.bar(3, vencedores.count('cauteloso'), color='green', width=0.5)
    plt.bar(4, vencedores.count('aleatório'), color='blue', width=0.5)
    plt.title('Percentual de Vitórias por comportamento')
    plt.xlabel('Comportamento')
    plt.ylabel('Percentual de Vitórias (nas Simulações)')
    plt.xticks([1, 2, 3, 4], ['Impulsivo','Exigente','Cauteloso','Aleatório'])
    plt.show()


if __name__ == '__main__':   

    # Limpa a tela
    os.system('clear')
    
    # Inicializa variáveis    
    num_jogadores = 4
    num_propriedades = 20
    num_simulacoes = 300
    
    saldo_inicial = 300
    posicao_inicial = 0
        
    rodadas = 0 
    time_out = 0 
    turnos = [] 
    vencedores = []
    
    comportamento = ['impulsivo', 'exigente', 'cauteloso', 'aleatório']
    
    # Decisões de projeto
    custo_maximo_venda = 350 # Baseado no saldo inicial dos jogadores
    percentual_aluguel = 0.3 # Como é jogo, não correponde ao percentual real 
            
    for s in range(num_simulacoes):
        
        # Cria propriedades        
        propriedades = []                           
        for posicao in range(num_propriedades):
            custo_venda = round(random() * custo_maximo_venda, 2)
            valor_aluguel = round(custo_venda * percentual_aluguel, 2)      
            propriedades.append(
                Propriedade(custo_venda, valor_aluguel, posicao))    
        
        # Cria jogadores
        jogadores = []            
        for jogador in range(num_jogadores):
            jogadores.append(Jogador(
                saldo_inicial, posicao_inicial, comportamento[jogador]))      
        
        # Embaralha ordem dos jogadores
        shuffle(jogadores)        
        
        # Define variável de controle
        jogadores_ativos = len(jogadores)
        
        # Simula rodadas do jogo
        while rodadas <= 1000 and jogadores_ativos > 1:
            cont = 0
            while cont < jogadores_ativos > 1:  
                if not jogadores[cont].jogar(jogadores, propriedades):
                    #diponibilizar_propriedades(jogadores[cont]._propriedades)
                    del jogadores[cont]   # Eliminar_jogador(jogadores[cont]._propriedades)
                    jogadores_ativos -= 1
                else:
                    cont += 1 
            rodadas += 1    
        else: # Se a rodada for encerrada...           
            vencedor = jogadores[0]
            if jogadores_ativos > 1:   
               for i in range(1, jogadores_ativos):
                   if vencedor._saldo < jogadores[i]._saldo:
                       vencedor = jogadores[i]  
               time_out += 1
            vencedores.append(vencedor._comportamento)  
            
        # Armazena o número de turnos (rodadas) da partida
        turnos.append(rodadas-1)
        
        # Reinicia a contagem do número de rodadas
        rodadas = 0 
    
    # Chama função que apres. os resultados, apenas numéricos, das simulações
    mostrar_resultados(vencedores, time_out, turnos)
    
    # Chama função que apresenta os resultados, por gráficos, das simulações
    mostrar_resultados_graficos(vencedores, time_out, turnos)
    