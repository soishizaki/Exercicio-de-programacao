import random

def cria_pecas():
    lista = []
    for i in range(7):
        for j in range(i,7):
            lista.append([i,j])
    random.shuffle(lista)
    return lista

def inicia_jogo(jogadores, pecas):
    monte = pecas
    dici = {"jogadores": {}, "mesa": []}
    for i in range(jogadores):
        dici["jogadores"][i] = monte[0:7]
        monte = monte[7:]
    dici["monte"] = monte
    return dici

def verifica_ganhador(dicionario):
    ganhador = -1

    for jogador in dicionario:
        if len(dicionario[jogador]) == 0:
            ganhador = jogador
    return ganhador

def conta_pontos(lista):
    soma = 0
    for elemento in lista:
        soma += elemento[0] + elemento[1]
    return soma

def posicoes_possiveis(mesa, pecas):
    pecas_possiveis = []

    if len(mesa) == 0:
        return list(range(len(pecas)))
    
    for i in range(len(pecas)):
        if pecas[i][0] == mesa[0][0] or pecas[i][1] == mesa[0][0] or pecas[i][0] == mesa[-1][1] or pecas[i][1] == mesa[-1][1]:
            pecas_possiveis.append(i)

    return pecas_possiveis

def adiciona_na_mesa(peca, mesa):
    if len(mesa) == 0:
        return [peca]
    if peca[1] == mesa[0][0]:
        mesa = [peca] + mesa
        return mesa
    if peca[0] == mesa[0][0]:
        mesa = [[peca[1], peca[0]]] + mesa
        return mesa
    if peca[0] == mesa[-1][1]:
        mesa = mesa + [peca]
        return mesa
    if peca[1] == mesa[-1][1]:
        mesa = mesa + [[peca[1], peca[0]]]
        return mesa

    return mesa




    