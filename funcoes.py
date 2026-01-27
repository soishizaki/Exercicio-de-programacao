import random

def cria_pecas():
    lista = []
    for i in range(7):
        for j in range(i,7):
            lista.append([i,j])
    random.shuffle(lista)
    return lista
# fizemos juntas a função cria_pecas

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
    