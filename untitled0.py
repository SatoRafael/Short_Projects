### Modelando a Ruína do Jogador pelo método Random Walk
import numpy as np
from numpy import random 
from matplotlib import pyplot as plt

#criando lista vazia que conterá as jogadas 
jogadas = []
teto = 10000 #Objetivo do jogo

#Loop do jogo
for i in range(10): #Faremos este número de simulações
    dinheiro = [1000] #Quantia inicial
    for j in range(100): #Número de jogadas que o jogador fará
            ultima = dinheiro[-1] #Escolhe o último valor da lista
            if ultima != 0: 
                roleta = np.random.choice(2, p = [20/38,18/38]) #Jogadas, onde 0 = fracasso e 1 = sucesso.  
                if roleta == 1:
                    ultima = min(teto, ultima + 1) #Os valores não ultrapassam nosso teto (objetivo)
                else:
                    ultima = max(0, ultima - 1) #Os valores não ficam abaixo de 0 (Perda total)
            elif ultima == teto:
                ultima = teto #Caso chegue ao teto, o jogador para...
            else:
                ultima = 0 #... Ou o contrário
            dinheiro.append(ultima) #Adiciona a última jogada ao histórico
    jogadas.append(dinheiro) #Adiciona o histórico à lista de simualações

jogadas_array = np.array(jogadas) #Transforma a lista de listas em array
jogadas_t = np.transpose(jogadas_array) #Transpõe o array

plt.plot(jogadas_t) #Visualizando as simulações
plt.show()

final = jogadas_t[-1,:] #Extraindo as últimas jogadas de cada simulação

plt.hist(final) #Verificando a frequência da distribuição dos resultados
plt.show()
