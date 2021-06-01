'''Nome: João Pedro Rodrigues Alves; RA: 42083605'''

import random


def main():
    print("===================Bem vindo ao Batalha Naval====================\n-------------------------Regras do Jogo:-------------------------\n-> Você deverá fornecer um valor "
    "referente a linha e depois\noutro valor referente a coluna, que formará o par ordenado \nem que você irá tentar acertar umas das embarcações do inimigo;"
    "\n\n-> Você irá jogar contra o computador;\n\n-> Quem destruir todas as embarcações do inimigo primeiro, \nvence o jogo!"
    "\n-----------------------------------------------------------------\n")
    
    #Matriz geral para representar o mar
    oceano = [['a' for i in range(10)] for j in range(10)]

    #Dicionários
    strikeGroup = []
    portaAvioes = { 'nome': 'Porta-aviões',
                    'comprimento': 5,
                    'sigla': 'p',
                    'quantidade': 1}
    strikeGroup.append(portaAvioes)

    cruzadores = {  'nome': 'Cruzador',
                    'comprimento': 4,
                    'sigla': 'c',
                    'quantidade': 2}
    strikeGroup.append(cruzadores)

    destroyers = {  'nome': 'Destroyer',
                    'comprimento': 3,
                    'sigla': 'd',
                    'quantidade': 3}
    strikeGroup.append(destroyers)

    submarinos = {  'nome': 'Submarino',
                    'comprimento': 2,
                    'sigla': 's',
                    'quantidade': 3}
    strikeGroup.append(submarinos)
    
    #Função que posiciona de forma aleatória as embarcações
    posicionaEmbarcacao(strikeGroup, oceano)
    #Definição do mapa do jogador
    reticuladoPlayer = oceano
    print("-> Mapa do jogador: \n")
    retBatalha(oceano)
    print("\n")
    #Definição do mapa do computador
    posicionaEmbarcacao(strikeGroup, oceano)
    reticuladoPC = oceano
    #Função que inicia o jogo
    jogabilidade(reticuladoPlayer, reticuladoPC)


def retBatalha(oceano):
    for linha in range(len(oceano)):
        for coluna in range(len(oceano[linha])):
            if coluna == 9:
                print(oceano[linha][coluna])
            else:
                print(oceano[linha][coluna], end=' ')


def randomico(max, direcao, oceano):
    if direcao == 'horizontal':
        # (Linha, coluna)
        return random.randint(0, len(oceano) - 1), random.randint(0, max)
    else:
        return random.randint(0, max), random.randint(0, len(oceano) - 1)


def posicionaEmbarcacaoHelper(tamanhoEmbarcacao, oceano):
    ok = False
    HORIZONTAL = 0
    VERTICAL = 1
    
    if random.randint(0, 1) == HORIZONTAL:
        direcao = 'horizontal'
    else:
        direcao = 'vertical'
    
    while not ok:
        sortedLinha, sortedColuna = randomico((len(oceano) - 1) - tamanhoEmbarcacao, direcao, oceano)
        if direcao == 'horizontal':
            for coluna in range(sortedColuna, sortedColuna + tamanhoEmbarcacao, 1):
                if oceano[sortedLinha][coluna] == 'a':
                    ok = True
                else:
                    ok = False
                    break
        else:
            for linha in range(sortedLinha, sortedLinha + tamanhoEmbarcacao):
                if oceano[linha][sortedColuna] == 'a':
                    ok = True
                else:
                    ok = False
                    break
    return sortedLinha, sortedColuna, direcao


def posicionaEmbarcacao(strikeGroup, oceano):
    for embarcacao in strikeGroup:
        for i in range(embarcacao.get('quantidade')):
            #Tupla
            sortedLinha, sortedColuna, direcao = posicionaEmbarcacaoHelper(embarcacao.get('comprimento'), oceano)
            if direcao == 'horizontal':
                for coluna in range(sortedColuna, sortedColuna + embarcacao.get('comprimento')):
                    oceano[sortedLinha][coluna] = embarcacao.get('sigla')
            else:
                for linha in range(sortedLinha, sortedLinha + embarcacao.get('comprimento')):
                    oceano[linha][sortedColuna] = embarcacao.get('sigla')


def jogabilidade(reticuladoPlayer, reticuladoPC):
    #Definição dos contadores da quantidade de acertos de cada jogador
    contPlayer = []
    contPC = []
    #Laço infinito
    while True:
        vezPlayer(reticuladoPC, contPlayer)
        #Se o jogador acertou todas as embarcações ele ganha o jogo
        if len(contPlayer) == 28:
            print("\nParabéns! Você ganhou!")
            #Laço infinito é quebrado
            break
        #Se não, ele passa a vez para o computador
        else:
            print("\nVez do computador:")
        
        vezPC(reticuladoPlayer, contPC)
        #Se o computador acertou todas as embarcações ele ganha o jogo
        if len(contPC) == 28:
            print("\nQue pena, você perdeu...tente novamente)")
            #Laço infinito é quebrado
            break
        #Se não, ele passa a vez para o jogador
        else:
            print("\nSua vez:")        
    print("========================Fim de jogo!========================")


def vezPlayer(reticuladoPC, contPlayer):
    #Definição das coordenadas da tentativa do jogador
    x = int(input("Digite um valor para linha: "))
    y = int(input("Digite um valor para coluna: "))
    #Se as coordenadas cairem na "água" o jogador errou
    if reticuladoPC[x][y] == 'a':
        print("Você errou!")
    #Se não, ele acertou uma embarcação e marca uma posição no contador
    else:
        print("Você acertou um ", reticuladoPC[x][y], "parabéns!!!")
        #Como essa coordenada foi atingida, ela passa a ser água
        reticuladoPC[x][y] = 'a'
        return contPlayer.append(1)


def vezPC(reticuladoPlayer, contPC):
    #Definição das coordenadas da tentativa aleátoria do computador
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    #O jogador recebe a tentativa do computador
    print("Chute do computador: (", x, ",", y, ")")
    #Se as coordenadas cairem na "água" o computador errou
    if reticuladoPlayer[x][y] == 'a':
        print("O computador errou!")
    #Se não, ele acertou uma embarcação e marca uma posição no contador
    else:
        print("O computador acertou um ", reticuladoPlayer[x][y], "seu, na posição (" , x,",", y, ")!!!")
        #Como essa coordenada foi atingida, ela passa a ser água
        reticuladoPlayer[x][y] = 'a'
        return contPC.append(1)


main()
