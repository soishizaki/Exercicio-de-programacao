import random

def cria_pecas():

    lista = []
    for i in range(7):
        for j in range(i,7):
            lista.append([i,j])
    random.shuffle(lista)
    return lista

